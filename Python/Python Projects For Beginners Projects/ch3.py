# a calculator program
def main(): 
    # ask the user for the operation they would like to perform
    operation = input("Would you like to add/subtract/multiply/divide? ").lower()
    print("You chose to {}.".format(operation))

    # ask the user for numbers input
    num1 = input("What is your first number? ")
    num2 = input("What is your second number? ")

    print("First number: {}\nSecond number: {}".format(num1, num2))
    reverse_numbers = input("Would you like to reverse the order of the numbers? Yes/No\n").lower()

    if reverse_numbers == "yes":
        dummy = num1
        num1 = num2
        num2 = dummy

    # set up try / except for the mathematical operation
    try: 
        # convert the numbers to floats
        num1, num2 = float(num1), float(num2)

        # perform operation and print result
        if operation == "add":
            result = num1 + num2
            print("{} + {}  = {}".format(num1, num2, result))
        elif operation == "subtract":
            result = num1 - num2
            print("{} - {}  = {}".format(num1, num2, result))
        elif operation == "multiply":
            result = num1 * num2
            print("{} * {}  = {}".format(num1, num2, result))
        elif operation == "divide":
            result = num1 / num2
            print("{} / {}  = {}".format(num1, num2, result))
        else:
            print("Sorry, but '{}' is not an option.".format(operation))
    except:
        print("Error: Improper numbers used, Please try again")
        

if __name__ == "__main__":
    main()