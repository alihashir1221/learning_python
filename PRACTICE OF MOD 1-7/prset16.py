#Write a function that checks whether a word is a palindrome.
def is_palindrome(word):
    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    
    # Check if the word is equal to its reverse
    return word == word[::-1]