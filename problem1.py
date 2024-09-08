def count_words(n, words):
    distinct_words = []
    counts = []
    for word in words:
        # Check if word is already in distinct_words
        if word in distinct_words:
            index = distinct_words.index(word)
            counts[index] += 1  # Increment the count of the existing word
        else:
            distinct_words.append(word)  # Add the word to distinct words
            counts.append(1)  # Initialize its count to 1
    # Output the number of distinct words
    print(len(distinct_words))
    # Output the occurrences of each word
    print(" ".join(map(str, counts)))
# Input number of words
n = int(input().strip())
# Input the words
words = []
for _ in range(n):
    word = input().strip()
    words.append(word)
# Call the function to count words and output results
count_words(n, words)
