# 整理Allen與Viki對話，統計各自講的字數及貼圖數程式

def split_file(filename):
    chat_in_VA = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            chat_in_VA.append(line.strip())
    return chat_in_VA


def word_count(Lines):
    word_count_Allen = 0
    word_count_Viki = 0
    for line in Lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "Allen":
            for m in s[2:]:
                word_count_Allen += len(m)
        elif name == "Viki":
            for m in s[2:]:
                word_count_Viki += len(m)
    return word_count_Allen, word_count_Viki


def sticker_count(Lines):
    sticker_count_Allen = 0
    sticker_count_Viki = 0
    for line in Lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "Allen":
            if s[2] == "貼圖":
                sticker_count_Allen +=1
        elif name == "Viki":
            if s[2] == "貼圖":
                sticker_count_Viki +=1
    return sticker_count_Allen, sticker_count_Viki


def write_file(filename, Lines):
    with open(filename, "w", encoding="utf-8-sig") as f:
        for line in Lines:
            f.write(line + "\n")

def main():
    chat_in_VA = split_file("Line_Viki.txt")
    word_count_Allen, word_count_Viki = word_count(chat_in_VA)
    sticker_count_Allen, sticker_count_Viki = sticker_count(chat_in_VA)
    # write_file("output.txt", chat_out)
    print(chat_in_VA)
    print("__________")
    print("Allen說了", word_count_Allen, "個字。")
    print("Viki說了", word_count_Viki, "個字。")
    print("__________")
    print("Allen貼了", sticker_count_Allen, "個圖。")
    print("Viki貼了", sticker_count_Viki, "個圖。")

main()