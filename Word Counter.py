def count_words(text):
    """
    This function takes a string input and returns the number of words in it.
    Words are separated by spaces.
    """
    words = text.split()
    return len(words)

def main():
    """
    Main function to handle user input, process the word count, and display the output.
    """
    print("\n📖 Welcome to the Word Counter Program 📖")
    print("Enter a sentence or paragraph below:")

    # Taking user input
    text = input("> ").strip()

    # Error handling: Check if input is empty
    if not text:
        print("⚠️ Error: No text entered. Please provide a valid input.")
        return

    # Counting words
    word_count = count_words(text)

    # Displaying output
    print(f"\n✅ Word Count: {word_count} words")

if __name__ == "__main__":
    main()
