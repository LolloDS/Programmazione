def initials(a):
    words = a.split()
    result = {}

    for word in words:
        if word[0] in result:
            result[word[0]].append(word)
        else:
            result[word[0]] = [word]

    return result

a = input("Inserisci una stringa: ")
print(initials(a))