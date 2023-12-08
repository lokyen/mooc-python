# Write your solution here

# Please write a program which asks the user which editor they are using. The program should keep on asking until the user types in Visual Studio Code.

while True:
    message = input("Editor: ")
    if "visual studio code" == message.lower():
        print("an excellent choice!")
        break
    elif "word" == message.lower() or "notepage" == message.lower():
        print("awful")
    else:
        print("not good")