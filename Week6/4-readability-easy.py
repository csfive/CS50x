def main():
    text = input("Text: ")

    cnt = w_cnt = s_cnt = 0
    for i in range(len(text)):
        if text[i].isalnum():
            cnt += 1
        if text[i].isspace():
            w_cnt += 1
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            s_cnt += 1

    w_cnt += 1
    l = cnt * 100 / w_cnt
    s = s_cnt * 100 / w_cnt
    grade = round(0.0588 * l - 0.296 * s - 15.8)

    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
