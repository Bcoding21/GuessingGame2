import time

troll = input("Hello! My name is BDB. Do you want to play a game?: ")
print("It doesnt matter what you enter. LET'S PLAY!\n")
time.sleep(3)
print("First you have to enter the range of numbers to guess from!\n")
time.sleep(3)
low = (input("Enter the lowest number to guess from: "))

while low.isnumeric() != True:
    time.sleep(0.5)
    print("Hmmmmmmm")
    time.sleep(1.5)
    print("Input is not a number")
    time.sleep(1.5)
    low = input("Enter the lowest number to guess from: ")

    
high = input("Enter the highest number to guess from: ")
while high.isnumeric() != True:
    time.sleep(0.5)
    print("Hmmmmmmm")
    time.sleep(1.5)
    print("Input is not a number")
    time.sleep(1.5)
    high = input("Enter the highest number to guess from: ")
    

print("")
mid = int((int(low) + int(high)) // 2)

print("Your number is:", mid,"\n")

is_number = input("Was this your number?(Enter yes/no): ").lower().strip()
while is_number != "yes" and is_number != "no":
    time.sleep(1)
    print("Input has to be \"yes\" or \"no\" answer")
    time.sleep(0.6)
    is_number = input("Was this your number?(Enter yes/no): ").lower().strip()
    
print("")

if is_number == "yes":
    print("That was easy!")

while is_number == "no":
    
    is_higher = input("Is your number higher than my guess?(yes/no): ").lower().strip()
    while is_higher != "yes" and is_number != "no":
        time.sleep(1)
        print("Input has to be \"yes\" or \"no\" answer")
        time.sleep(0.6)
        is_higher = input("Is your number higher than my guess?(yes/no): ").lower().strip()

    if is_higher == "yes":
        low = mid + 1

    if is_higher == "no":
        high = mid - 1

    mid = int((int(low) + int(high)) // 2)

    print("Now I know your number. Your number is:", mid, "\n")

    is_number = input("Was I correct. (Enter yes/no): ")
    while is_number != "yes" and is_number != "no":
        time.sleep(1)
        print("Input has to be \"yes\" or \"no\" answer")
        is_number = input("Was this your number?(Enter yes/no): ").lower().strip()
    print("")

    if (is_number == "yes" and high == low) or is_number == "yes":
        print("That was easy!")


    if high == low and is_number != "yes":
        print("You lied about what your number was. Goodbye!")
        break

    
    


        
