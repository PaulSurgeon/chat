# 整理對話程式

def read_file(filename):
    chat_in = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            chat_in.append(line.strip())
    return chat_in

def revise_file(Lines):
    chat_out = []
    person = None
    for line in Lines:
        if line == "Allen":
            person = "Allen"
            continue
        elif line == "Tom":
            person = "Tom"
            continue
        if person:
            chat_out.append(person + ": " + line)
    return chat_out

def write_file(filename, Lines):
    with open(filename, "w", encoding="utf-8-sig") as f:
        for line in Lines:
            f.write(line + "\n")

def main():
    chat_in = read_file("input.txt")
    chat_out = revise_file(chat_in)
    write_file("output.txt", chat_out)
    print(chat_in)
    print("__________")
    print(chat_out)
    print("__________")

main()