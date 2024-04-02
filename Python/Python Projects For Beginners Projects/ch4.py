# the hangman project

def main():
    # import
    from random import choice

    # declare the game variables
    words = ['tree', 'basket', 'chair', 'paper', 'python']
    word = choice(words)
    guessed, lives, game_over = [], 7, False

    # generate the hidden word
    guesses = ["_"]*len(word)

    # the game loop
    while not game_over:
        # output the game information
        hidden_word = " ".join(guesses)
        print("Your guessed letters: {}".format(guessed))
        print("Word to guess: {}".format(hidden_word))
        print("Lives: {}".format(lives))
        
        ans = input("Type quit or guess a letter: ").lower()
        
        if ans == "quit":
            print("Thanks for playing.")
            game_over = True
        elif ans in word and ans not in guessed:
            print("You guessed it correctly!")
            
            for i in range(len(word)):
                if word[i] == ans:
                    guesses[i] = ans
        elif ans in guessed:
            print("You already guessed that. Try again")
        else:
            lives -= 1
            print("Incorrect, you lost a life.")

            if ans not in guessed:
                guessed.append(ans)
        if lives <= 0:
            print("You lost all your lives, you lost!")
            game_over = True
        elif word == "".join(guesses):
            print("Congratulations, you guessed it correctly!")
            game_over = True
            
if __name__ == "__main__":
    main()