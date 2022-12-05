# Print on-screen the items for the fruit stand
hello = input("Would you like to take a look at our fruit stand today? Y or N: ")

if hello.lower() == 'y':
    print("Awesome and welcome to our fruit stand!")
    print("These are the items we have in store: (1) for Bananas, (2) for Oranges and (3) for Apples.")
    x = int(input("Let us know what fruit you'll be purchasing today: "))

    if (x == 1):
        y = int(input("Tell us how many Bananas you'll be purchasing: "))
        print(f"Your total you'll be: {y * 1.85}")
    elif (x == 2):
        y = int(input("Tell us how many Oranges you'll be purchasing: "))
        print(f"Your total you'll be: {y * 3.60}")
    elif (x == 3):
        y = int(input("Tell us how many Apples you'll be purchasing: "))
        print(f"Your total you'll be: {y * 2.30}")
    else:
        print("Invalid option.")
        
    print("Thanks for your patronage.")
else:
    print("Thanks for your time anyway! Have a nice day.")
