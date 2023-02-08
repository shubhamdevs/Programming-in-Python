
sentence = str(input())

word = ""
if len(sentence) % 2 == 0:
    if sentence[-1:] == ".":
        word = sentence[:-1]
    else:
        word = sentence + "."
else:
    word = sentence
    
    
middle = len(word) // 2

substring = word[middle-1:middle+2]

print(substring)

