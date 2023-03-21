print("Write into console.txt")
file = open("C:\\Users\\10710516\\OneDrive - LTI\\Desktop\\JBL\\Python_Files\\ConsoleApp\\console.txt","a")
running = True
while running:
    text = str(input("Enter text: "))
    text += "\n"
    file.write(text)
    file.close()
    print("want to continue, press c; want to quit, press q")
    userinput = str(input())
    if userinput == "c":
        file = open("C:\\Users\\10710516\\OneDrive - LTI\\Desktop\\JBL\\Python_Files\\ConsoleApp\\console.txt","a")
        continue
    else:
        running = False
        print("Thank you")