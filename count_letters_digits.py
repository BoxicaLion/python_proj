def main():
    fileName = "text.txt"
    file = openLoadCloseFile(fileName)
    countUpper(file)
    countLower(file)
    countDigit(file)
    countwhitespace(file)


def openLoadCloseFile(file):
    myString = ''
    with open(file, encoding="utf8", errors='ignore') as f:
        myString = f.read()
        f.close
    return myString

def countUpper(string):
    isupper = 0
    for i in string:
        if i.isupper():
            isupper+=1
    print("Uppercase letters:",isupper)

def countLower(string):
    sentCount = 0
    for i in string:
        if i.islower():
            sentCount+=1
    print("Lowercase letters:",sentCount)

def countDigit(string):
    sentCount = 0
    for i in string:
        if i.isdigit():
            sentCount+=1
    print("Digits:",sentCount)

def countwhitespace(string):
    sentCount = 0
    for i in string:
        if i.count(" ") or i.count("\n"):
            sentCount+=1
    print("Spaces:",sentCount)

main()






