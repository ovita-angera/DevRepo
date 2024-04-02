# user database using csv files
# set up the necessary imports
import csv
from getpass import getpass
from IPython.display import clear_output

# handle user registration and writing to csv
def registerUser():
    with open('users.csv', mode='a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        print('To register, please enter your info:')
        email = input('E-mail: ')
        password = getpass('Password: ')
        password2 = getpass('Re-type password: ')
        clear_output()

        if password == password2:
            writer.writerow([email, password])
            print('You are now registered')
        else:
            print('Something went wrong. Try again.')

# handling user login 
# ask for user info and return true to login or false if incorrect info
def loginUser():
    print('To log in, please enter your info: ')
    email = input('E-mail: ')
    password = getpass('Password: ')
    clear_output()

    with open('users.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row == [email, password]:
                print('You are now logged in!')
                return True
    print('Something went wrong, try again')
    return False

# define a function to change password
def changePassword():
    print('To change password, enter your info:')
    email = input('E-mail: ')
    password = getpass('Old password: ')
    new_password = getpass('New password: ')
    new_password2 = getpass('Re-type new password: ')
    clear_output()

    with open('users.csv', mode='r') as read_file:
        reader = csv.reader(read_file, delimiter=',')
        lines = list(reader) 
    
    if new_password == new_password2:
        for row in range(len(lines)):
            if lines[row] == [email, password]:
                lines[row] = [email, new_password]
        
        with open('users.csv', mode='w', newline='') as write_file:
            writer = csv.writer(write_file, delimiter=',')
            writer.writerows(lines)
    else:
        print('Sorry, an error occurred, please try again')

def main():
    ## The main loop
    # variables for the main loop
    active = True
    logged_in = False

    # the loop
    while active:
        if logged_in:
            print('1. Logout\n2. Change Password\n3. Quit')
        else:
            print('1. Login\n2. Register\n3. Quit')
        
        choice = input('What would you like to do? ').lower()
        clear_output()

        if choice == 'register' and logged_in == False:
            registerUser()
        elif choice == 'login' and logged_in == False:
            logged_in = loginUser()
        elif choice == 'quit':
            active = False
            print('Thanks for using our software')
        elif choice == 'logout' and logged_in == True:
            logged_in = False
            print('You are now logged out')
        elif choice == 'change password' and logged_in == True:
            changePassword()
            print('You now have a new password')
        else:
            print('Sorry, please try again!')
            
if __name__ == "__main__":
    main()