#Assumes that there are only single spaces between words

def wordCount(text):
    total = 0
    for i in text:
        if i == ' ':
            total += 1
    print total