from typing import Dict, List


def count_letters(text: str) -> int:
    """Returns the number of letters in the given text."""
    return sum(1 for char in text if char.isalpha())


def count_words(text: str) -> int:
    """Returns the number of words in the given text."""
    return len(text.split())


def count_sentences(text: str, punctuation: List[str]) -> int:
    """Returns the number of sentences in the given text."""
    return sum(1 for char in text if char in punctuation)


def calculate_grade_level(L: float, S: float) -> int:
    """Returns the grade level for the given values of L and S using the Coleman-Liau formula."""
    A = 0.0588
    B = 0.296
    C = 15.8
    index = round(A * L - B * S - C)
    return max(0, min(index, 16))


def get_reading_level(text: str, punctuation: List[str], outputs: Dict[int, str]) -> str:
    """Returns the reading level of the given text using the Coleman-Liau formula."""
    letters_count = count_letters(text)
    words_count = count_words(text)
    sentences_count = count_sentences(text, punctuation)

    L = (letters_count / words_count) * 100
    S = (sentences_count / words_count) * 100

    grade_level = calculate_grade_level(L, S)

    return outputs[grade_level]


def main() -> None:
    """Asks the user to type some text and outputs the grade level for the text according to the Coleman-Liau formula."""
    text = input("Text: ")

    punctuation = [".", "!", "?"]

    outputs = {
        0: "Before Grade 1",
        1: "Grade 1",
        2: "Grade 2",
        3: "Grade 3",
        4: "Grade 4",
        5: "Grade 5",
        6: "Grade 6",
        7: "Grade 7",
        8: "Grade 8",
        9: "Grade 9",
        10: "Grade 10",
        11: "Grade 11",
        12: "Grade 12",
        13: "Grade 13",
        14: "Grade 14",
        15: "Grade 15",
        16: "Grade 16+"
    }

    reading_level = get_reading_level(text, punctuation, outputs)

    print(reading_level)


if __name__ == "__main__":
    main()
