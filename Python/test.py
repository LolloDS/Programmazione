def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou' and char != ' ')

def count_consonants(s):
    return sum(1 for char in s if char.lower() not in 'aeiou' and char != ' ')

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
print("Number of consonants:", count_consonants(s))

