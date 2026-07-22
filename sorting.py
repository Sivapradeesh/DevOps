def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

text = input("Enter a string: ")

print("Original String :", text)
print("Reversed String :", reverse_string(text))
print("Uppercase       :", text.upper())
print("Lowercase       :", text.lower())
print("Character Count :", len(text))
print("Vowel Count     :", count_vowels(text))