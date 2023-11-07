def new_string(text):
    if text[:2] == "Is":
        return text
    else:
        return "Is" + text
    
text = input("Enter String: ")
print(new_string(text))