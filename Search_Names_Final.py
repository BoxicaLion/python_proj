def main():
    BoyNamesFile = 'BoyNames.txt'
    GirlNamesFile = 'GirlNames.txt'
    BoyNames = openLoadCloseBoyNamesFile(BoyNamesFile)
    GirlNames = openLoadCloseGirlNamesFile(GirlNamesFile)
    searchName(BoyNames, GirlNames)
    

def openLoadCloseBoyNamesFile(file):
    BoyNamesList = list()
    BoyFile = open(file, 'r')
    for line in BoyFile:
        BoyNamesList.append(line.strip())
    BoyFile.close()
    return BoyNamesList


def openLoadCloseGirlNamesFile(file):
    GirlNamesList = list()
    GirlFile = open(file, 'r')
    for line in GirlFile:
        GirlNamesList.append(line.strip())
    GirlFile.close()
    return GirlNamesList

def searchName(boyNames, girlNames):
    name = input("Enter a name to search or type QUIT to exit:\n")
    formatName = name.capitalize()
    if formatName in boyNames and formatName in girlNames:
        boyNameIndex = boyNames.index(formatName)
        girlNameIndex = girlNames.index(formatName)
        print("The name ",formatName," was found in both lists: boy names (line ",boyNameIndex+1,") and girl names (line ",girlNameIndex+1,").",sep='')
    elif formatName in girlNames:
        girlNameIndex = girlNames.index(formatName)
        print("The name \'",formatName,"' was found in popular girl names list (line ",girlNameIndex+1,").",sep='')
    elif formatName in boyNames:
        boyNameIndex = boyNames.index(formatName)
        print("The name '",formatName,"' was found in popular boy names list (line ",boyNameIndex+1,").",sep='')
    else:
        if formatName != "Quit":
            print("The name '",formatName,"' was not found in either list.",sep='')
    while name != "QUIT" and name != "quit":
        name = input("Enter a name to search or type QUIT to exit:\n")
        formatName = name.capitalize()
        if formatName in boyNames and formatName in girlNames:
            boyNameIndex = boyNames.index(formatName)
            girlNameIndex = girlNames.index(formatName)
            print("The name '",formatName,"' was found in both lists: boy names (line ",boyNameIndex+1,") and girl names (line ",girlNameIndex+1,").",sep='')
        elif formatName in girlNames:
            girlNameIndex = girlNames.index(formatName)
            print("The name \'",formatName,"' was found in popular girl names list (line ",girlNameIndex+1,").",sep='')
        elif formatName in boyNames:
             boyNameIndex = boyNames.index(formatName)
             print("The name '",formatName,"' was found in popular boy names list (line ",boyNameIndex+1,").",sep='')
        else:
            if formatName != "Quit":
                print("The name '",formatName,"' was not found in either list.",sep='')

main()
