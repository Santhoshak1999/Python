def is_vowel(char):
    vowels = "aeiou"
    return char in vowels
    
char = input("Enter a character: ")
print(is_vowel(char))