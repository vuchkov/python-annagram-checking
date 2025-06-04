# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def is_annagram(target_word, check_word):
    if len(target_word) != len(check_word):
        return False
    return sorted(target_word.lower()) == sorted(check_word.lower())

def in_annagram_list(w, words_list):
    res = []
    for cw in words_list:
        if is_annagram(w, cw) and len(w) > 0:
            res.append(cw)
    return res

if __name__ == '__main__':
    words = ["art", "rat", "tar", "part", "tarp", "trap", "rapt", "brag", "grab"]

    s = str(input('Check the word: '))
    target_list = in_annagram_list(s, words)

    print(f"Count: ", len(target_list))
    for s in target_list:
        print(s)
