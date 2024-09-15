def main():
    report = make_report("books/frankenstein.txt")
    print(report)


def sort_on(d, key="num"):
    return d[key]


def make_report(path):
    text = get_book_text(path)
    chars = get_chars(text)
    dicts = []
    for key, value in chars.items():
        if key.isalpha():
            dicts.append({"letter": key, "num": value})
    dicts.sort(reverse=True, key=sort_on)

    words = get_num_words(text)

    report = f"--- Begin report of {path} ---"
    report += f"\r\n{words} words found in the document\r\n\r\n"
    for d in dicts:
        report += f"The '{d["letter"]}' character was found {d["num"]} times\r\n"
    report += "--- End report ---"

    return report


def get_chars(text):
    chars = {}
    for c in text:
        c = c.lower()
        chars[c] = chars.get(c, 0) + 1
    return chars


def get_num_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
