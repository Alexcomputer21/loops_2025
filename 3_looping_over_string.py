# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.
word = input("Give me a word: ")
for letter in word:
    print(letter)



# Challenge:
# Count how many vowels are in the word.
word = input("Enter a word: ")
vowel_count = 0
vowels = "aeiouAEIOU"

for letter in word:
    print(letter)
    if letter in vowels:
        vowel_count += 1
print("Number of vowels: ", vowel_count)