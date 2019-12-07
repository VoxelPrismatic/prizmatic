import os
thing = os.listdir()
global files
files = []
def get_all_files(dir = "."):
    global files
    thing = os.listdir(dir)
    for filename in thing:
        if filename.endswith(".py"):
            files.append(dir+"/"+filename)
        elif "." not in filename:
            get_all_files(dir+"/"+filename)
get_all_files()
for filename in files:
    #print("CHECKING", filename)
    with open(filename, "r") as f:
        txt = f.read()
        if txt.count("(") != txt.count(")"):
            print(filename, "MISSING PARENS")
        if txt.count("[") != txt.count("]"):
            print(filename, "MISSING BRACKS")
        if txt.count("{") != txt.count("}"):
            print(filename, "MISSING CURLYS")
        if txt.count("'") % 2:
            print(filename, "MISSING SINGLE QUOTES")
        if txt.count('"') % 2:
            print(filename, "MISSING DOUBLE QUOTES")
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("class") or line.startswith("def") and not line.endswith(":"):
                print(filename, "\n--------"+line+"\n--------", "MISSING COLON")
