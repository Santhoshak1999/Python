def substring_copy(text, n):
    flen = 2

    if flen > len(text):
        flen = len(text)

    substring = text[:2]
    result = "" #initializing an empty string
    for i in range(0,n):
        result += substring

    return result

print(substring_copy("santhoshak", 3))
print(substring_copy("p", 4))