
# global list variable
cart = [] # an empty list that resembles a customer cart before it is picked

# ***** Create a function to add items to the cart *****
def addItem(item):
    cart.append(item)
    print("{} has been added.".format(item))

# ***** Create a function to remove items from the cart *****
def removeItem():
    try:
        method = int(input("1. by item name\n2. by item number:\n"))
        if method == 1:
            name = input("Item: ").title()
            cart.remove(name)
            print("{} has been removed.".format(name))
        elif method == 2:
            number = int(input("Item number: ")) - 1
            cart.remove(cart[number])
            print("{} has been removed.".format(cart[number]))
        else:
            print("Error: Invalid option!")
    except:
        print("Sorry, we could not remove that item.")

# ***** Create a function to show items in the cart *****
def showCart():
    if cart:
        print("Here is your cart:")
        for item in range(len(cart)):
            print("{}). {}".format(item + 1, cart[item]))
    else:
        print("Your cart is empty.")

# ***** Create a function to clear items from the cart *****
def clearCart():
    cart.clear()
    print("Your cart is empty.")


## define the main function
def main():
    done = False
    while not done:
        ans = input("quit/add/remove/show/clear: ").lower()

        # base case
        if ans == "quit":
            print("Thanks for using our program")
            showCart()
            done = True
        elif ans == "add":
            item = input("What would you like to add? ").title()
            addItem(item)
        elif ans == "remove":
            showCart()
            removeItem()
        elif ans == "show":
            showCart()
        elif ans == "clear":
            clearCart()
        else:
            print("Sorry, that was not an option.")

if __name__ == "__main__":
    main()