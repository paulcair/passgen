import random
lower = "abcedefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "+=[]?.<>`/\|''~!@#$%^&*()_+|:"
boolean = 0
all = lower + upper + number + symbol

print("Welcome - this is Paul's Random password generator program\n")

while boolean == 0:
    
    length = input("Please select the number of characters desired...")
    
    try:
        int(length)
        length = int(length)
        password = "".join(random.sample(all,length))
        print("\n The password generated is :", password)
        print("\n Have a great day! \n")
        boolean = 1
    except ValueError:
        print("\n Error - Please enter a numerical value - TRY AGAIN\n")


input("Press any key to exit")