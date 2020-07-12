

def main():

    file = input("Please enter the file name or type QUIT to exit:\n")
    
    if file.lower() == "quit":
        return

    file_exists = True

    try:
        input_file = open(file, 'r')
    except FileNotFoundError:
        file_exists = False

    while not file_exists:
        print("File: " + file + " does not exist.")
        file = input("Please enter the file name again or type QUIT to exit:\n")
        if file.lower() == "quit":
            return
        
        file_exists = True

        try:
            input_file = open(file, 'r')
        except FileNotFoundError:
            file_exists = False

    input_file = open(file, 'r')
    try:
        total = 0.0
        lineCount = 0
        for Line in input_file:
            lineCount +=1
            castedValue = float(Line)
            total += castedValue
            average = total/lineCount
        input_file.seek(0)
        checkFile = input_file.read(1)
        if not checkFile:
            print("File", file, "is empty.", )
        else:
            print("Total: ", format(total, '.3f'),"\nAverage: ", format(average, '.3f'), sep='')
        input_file.close()
    except ValueError:
        print("Error")


main()
