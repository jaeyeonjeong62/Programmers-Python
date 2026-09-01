text = input()
result = ""

for i in range(len(text)):
    if text[i].islower():
        result += text[i].upper()
    else:
        result += text[i].lower()

print(result)