import os


pre = open("pre.txt").read()
post = open("post.txt").read()

def add_list(html, list_level, lines, i):
    j = i
    curr_num = 1
    line = lines[j]
    root = " " * (3 * list_level)
    prefix = root + f"{curr_num}. "
    list_o = line.startswith(prefix)
    if list_o:
        html += " " * (4 * list_level) + "<ol>\n"
    else:
        html += " " * (4 * list_level) + "<ul>\n"        
    while True:
        line = lines[j]
        root = " " * (3 * list_level)
        prefix = root + f"{curr_num}. "
        prefix_uo = root + f"- "
        sublist = root + f"   1. "
        sublist_uo = root + f"   - "
        if line.startswith(prefix):
            html += (" " * 4) * (list_level + 1) + '<li class="explain"> ' + line[len(prefix):] + " </li>\n"
            curr_num += 1
            j += 1
        elif line.startswith(prefix_uo):
            html += (" " * 4) * (list_level + 1) + '<li class="explain"> ' + line[len(prefix_uo):] + " </li>\n"
            curr_num += 1
            j += 1
        elif line.startswith(sublist) or line.startswith(sublist_uo):
            html, j = add_list(html, list_level + 1, lines, j)
        elif not line.startswith(root) or line == "":
            break

    if list_o:
        html += " " * (4 * list_level) + "</ol>\n"
    else:
        html += " " * (4 * list_level) + "</ul>\n"        
    return html, j

def make_link(line):
    if "](" not in line:
        return line
    name_start = line.find("[") + 1
    name_end = line.find("]")

    link_start = line.find("(") + 1
    link_end = line.find(")")
    
    name = line[name_start: name_end]
    link = line[link_start: link_end]
    link = link[:-3] + ".html" if link.endswith(".md") else link

    new_line = ""
    new_line += line[:name_start-1]
    new_line += f'<a href="{link}">{name}</a>'
    new_line += line[link_end+1:]
    return make_link(new_line)

def ensure_line(line):
    char, instances_start = "<", []
    index, last_index = line.find(char), - len(char)
    while index != -1:
        instances_start.append(last_index + len(char) + index)
        last_index = instances_start[-1]
        index = line[last_index + len(char):].find(char)

    char, instances_end = ">", []
    index, last_index = line.find(char), - len(char)
    while index != -1:
        instances_end.append(last_index + len(char) + index)
        last_index = instances_end[-1]
        index = line[last_index + len(char):].find(char)

    j_start = 0
    invalid_starts = []
    for i in range(len(instances_start)):
        found = False
        for j in range(j_start, len(instances_end)):
            if instances_start[i] < instances_end[j] and (line[i+1:j].count(" ") == 0):
                found = True
                j_start = j + 1
                break
        if not found:
            invalid_starts.append(i)
    if invalid_starts:
        print("------------------------------------------------------")
        print("handling < sign in following line: ")
        print(line)
        print("------------------------------------------------------")
        for i in invalid_starts[::-1]:
            k = instances_start[i]
            line = line[:k] + "&#60" + line[k+1:]
    return line

def make_word(line: str):
    placements = {
        "`": ["<code>", "</code>"],
        "**": ["<strong>", "</strong>"],
        "*": ["<em>", "</em>"],
    }
    for char, replace_by in placements.items():
        instances = []
        index, last_index = line.find(char), - len(char)
        while index != -1:
            instances.append(last_index + len(char) + index)
            last_index = instances[-1]
            index = line[last_index + len(char):].find(char)

        valid = [1] * len(instances)
        for i in range(1, len(instances)):
            prev, next = instances[i-1], instances[i]
            if (next - prev) == len(char):
                valid[i-1], valid[i] = 0, 0

        instances_filtered = [instances[i] for i in range(len(instances)) if valid[i]]

        for i in range(len(instances_filtered)-1,0,-2):
            next = instances_filtered[i]
            prev = instances_filtered[i-1]
            line = line[:next] + replace_by[1] + line[next+len(char):]
            line = line[:prev] + replace_by[0] + line[prev+len(char):]

    return line

def get_id(name):
    id = name[:]
    while "<" in id:
        place_init = id.find("<")
        place_finish = id.find(">")
        if place_init > place_finish:
            raise Exception(f"Wrong line format: {id}")
        id = id[:place_init] + id[place_finish+1:]
    id = id.replace(".", "")
    id = id.replace('"', "")
    id = id.replace("'", "")
    id = id.replace("`", "")
    id = id.replace(" ", "-")
    id = id.lower()
    return id

def convert(source, dest, folder_level):
    md_lines = open(source).read().split("\n")
    main = ""
    main += pre

    md_lines = [make_link(line) for line in md_lines]
    md_lines = [make_word(line) for line in md_lines]
    md_lines = [ensure_line(line) for line in md_lines]
    i = 0
    while i < len(md_lines):
        line = md_lines[i]
        
        num_hashes = 0
        while line.startswith("#" * (num_hashes + 1)):
            num_hashes += 1
        if num_hashes:
            name = line[num_hashes + 1:]
            id = get_id(name)
            line_add = f'<h{num_hashes} id="{id}" class="guides-h{num_hashes}"> {name} </h{num_hashes}>\n'
            if num_hashes > 4:
                print(line_add)
            main += line_add
            i += 1
            continue

        if line.startswith("```"):
            code_started = i + 1
            code_lan = line[3:]
            j = i + 1
            while md_lines[j] != "```":
                j += 1
            code_end = j
            code = "\n".join(md_lines[code_started: code_end])

            main += f'<pre class="language-{code_lan}">\n'
            main += f'<code>\n'
            main += f"{code}\n"
            main += f'</code>\n'
            main += f'</pre>\n'
            code_started = -1
            code_lan = None
            i = j + 1
            continue
        
        if line.startswith("1. ") or line.startswith("- "):
            list_level = 0
            main, j = add_list(main, list_level, md_lines, i)
            i = j + 1
            continue

        if line.startswith("---"):
            main += f"<hr>\n"
        elif len(line) > 0:
            main += f'<p class="explain">{line}</p>\n'

        else:
            main += "\n"

        i += 1
    main += post

    main = main.replace("</p>\n<p>", "\n")
    main = main.replace("{{css_folder}}", "../" * folder_level)

    folder = os.path.dirname(dest)
    create_folder(folder)

    file = open(dest, "w")
    file.write(main)
    file.close()

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            return True
        except:
            return False
    else:
        return True


def get_files_in_directory(directory_path, suffix=None, recursive=False, return_full_path=False):
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    return_full_path |= recursive
    files = []
    for root, _, filenames in os.walk(directory_path):
        for file_name in filenames:
            if suffix is None or file_name.endswith(suffix):
                if return_full_path:
                    files.append(os.path.join(root, file_name))
                else:
                    files.append(file_name)
        if not recursive:
            break

    return files

def main(source, dest):
    files = get_files_in_directory(source, recursive=True)
    for file in files:
        if not file.endswith(".md"):
            continue
        ext = os.path.splitext(file)
        name = file[len(source):-len(ext)]
        target = dest + name + "html"
        print(name)
        convert(file, target, name.count("/") + 1)

if __name__ == "__main__":
    source = "/workspace/github/python-codes/guides/"
    dest = "/workspace/github/nilbarde.github.io/learning/"

    main(source, dest)
