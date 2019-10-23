def main():
    fileName="text.txt"
    file=openLoadCloseFile(fileName)
    average=countAverage(file)

def openLoadCloseFile(file):
    myString=''
    FileName=open(file,'r')
    myString=FileName.read()
    FileName.close
    return myString

def countAverage (string):
    wordCount=string.split()
    sentCount=0
    for i in range(len(wordCount)):
        if"." in wordCount[i]:
            sentCount +=1
            
    print("Average number of words per sentence: ",format((len(wordCount)/sentCount),".2f"))
                                                          
main()
