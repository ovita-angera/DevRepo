# after setting up your environment
# The guessing game
def main():
    from random import randint
    guessed = False
    number = randint(0, 100)
    guesses = 0
    
    while not guessed:
        ans = input("Try to guess the number I am thinking of:\n")
        
        guesses += 1
        
        try:
            if int(ans) == number:
                print("Congrats! You guessed it correctly.")
                print("It took you {} guesses!".format(guesses))
                break
            
            elif int(ans) > number:
                print("The number is lower than what you guessed\n")
            
            elif int(ans) < number:
                print("The number is greater than what you guessed\n")
                
        except:
            print("The value you entered is not a number")
            

# execution block
if __name__ == "__main__":
    main()
        