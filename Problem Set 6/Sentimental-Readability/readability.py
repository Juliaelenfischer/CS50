def count_letters(text):
    # Return the number of letters in text
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count


def count_words(text):
    # Return the number of words in text
    count = len(text.split())
    return count


def count_sentences(text):
    # Return the number of sentences in text
    count = 0
    for char in text:
        if char in ['.', '?', '!']:
            count += 1
    return count


def main():
    # Prompt the user for some text
    text = input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Compute the Coleman-Liau index
    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Print the grade level
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


if __name__ == "__main__":
    main()
