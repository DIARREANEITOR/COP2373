import re


def extract_sentences(text):
    """
    Extracts sentences using regex with look-ahead.
    Sentences can start with capital letters or digits.
    """
    pattern = r"[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)"
    sentences = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
    return sentences


def display_sentences(sentences):
    """
    Displays each sentence and the total count.
    """
    print("\nSentences found:\n")

    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence.strip()}")

    print(f"\nTotal number of sentences: {len(sentences)}")


def main():
    """
    Main driver function.
    """
    print("Enter a paragraph:\n")
    paragraph = input()

    sentences = extract_sentences(paragraph)
    display_sentences(sentences)


# Run the program
if __name__ == "__main__":
    main()