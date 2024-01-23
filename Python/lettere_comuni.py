#def count_common_letters(str1, str2):
 #   return len(set(str1) & set(str2))

#str1 = input("Enter first string: ")
#str2 = input("Enter second string: ")

#print("Number of common letters:", count_common_letters(str1, str2))

def count_common_letters(str1, str2):
    common_letters = []
    for c in str1:
        if c in str2:
            common_letters.append(c)
    count = 0
    for c in common_letters:
        count += 1
    return count

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Number of common letters:", count_common_letters(str1, str2))
