"""
{{note}} This file only allows automatic documentation creation. This file will
#NOT# be included in any of the modules itself
"""
import os
def get_files(lvl = "./", end = "py"):
    ls = []
    if lvl.startswith("./.git") or "__pycache__" in lvl:
        return []
    for d in os.listdir(lvl):
        if d.endswith("." + end):
            ls.append(lvl + d)
        else:
            try:
                ls.extend(get_files(lvl + d + "/", end))
            except Exception:
                pass
    return ls

def get_folders(lvl = "./", end = "py"):
    ls = []
    if lvl.startswith("./.git") or "__pycache__" in lvl:
        return []
    for d in os.listdir(lvl):
        if not d.endswith("." + end):
            ls.append(lvl + d + "/")
            try:
                ls.extend(get_folders(lvl + d + "/", end))
            except Exception:
                pass
    return ls
docs = "/home/priz/GitKraken/prizmatic.docs/doc/"
dirs = get_files()

for file in dirs:
    st = ""
    with open(file) as f:
        curr = ""
        incom = False
        for line in f.readlines():
            if line.strip() == '"""':
                incom = not incom
                indent = ""
                for char in curr:
                    if char != " ":
                        break
                    indent += " "
                curr = curr[len(indent):].replace("\n" + indent, "\n").strip()
                st += curr + "\n"
                curr = ""
                continue
            if incom:
                curr += line

    loc = f"{docs}{file[:-3]}.txt"
    thishere = ""
    for l in loc.split("/")[:-1]:
        try:
            thishere += "/" + l
            os.listdir(thishere)
        except Exception:
            os.mkdir(thishere)
    open(loc, "w+").write(st)
inits = {}

for file in get_files(docs, "txt"):
    folder = "/".join(file.rsplit("/")[:-1])
    if file.endswith("__init__.txt"):
        open(file, "w+").write("__listdir__")
    if file.endswith(".txt"):
        try:
            inits[folder].append(file.split("/")[-1])
        except KeyError:
            inits[folder] = [file.split("/")[-1]]
        open(file, "a").write("\n")

for init in inits:
    open(init + "/dir.txt", "w+").write("\n".join(inits[init]) + "\n")

for file in get_folders(docs, "txt"):
    if file.endswith("/"):
        folder = "/".join(file[:-1].split("/")[:-1]) + "/dir.txt"
        open(folder, "a+").write(file[:-1].split("/")[-1] + ".dir\n")

for file in get_files(docs, "txt"):
    st = open(file).read().strip() + "\n"
    open(file, "w").write(st)
    if file.endswith("dir.txt"):
        st = ""
        for line in open(file).readlines():
            if line != "dir.txt\n":
                st += line
        open(file, "w+").write(st)
