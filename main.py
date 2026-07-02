"""
This program is a password manager that can save all your passwords.
It has feautures like adding passwords, updating passwords,
deleting passwords, and getting passwords. It also
remembers all of your data in a file. 
"""

import logging
import time
import random
from Password import Password
passwords = []

#this function generates a random strong password that the user can use 
def generate_recommended(length)-> str:
    rec_password = ""
    #stores alphabet and numbers and symbols in a variable so it will pick randomly each time
    alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    num_sym = "1234567890!@#$%^&*()-_=+\|{};:/?.>"
    for i in range(length):
        choice = random.randint(0,1)
        if choice == 0:
            letter = alphabet[random.randint(0, len(alphabet) - 1)]
            rec_password += letter
        else:
            sym = num_sym[random.randint(0, len(num_sym) - 1)]
            rec_password += sym
    return rec_password
    
    

#updates a password, I think it works
def update_password():
    print("")
    #gets the name of the app from the user 
    app_name = input("What is the name of the app?: ")
    #sets password as None instead of "", better syntax
    password = None
    file_app_name = None
    
    try:
        #opens file and reads line by line to find the password that the user wants
        with open("passwords.txt", "r") as f:
            line = f.readline()
            while(line != ""):
                #makes sure it is not case sensitive
                if ((line.lower()).find(app_name.lower()) != -1):
                    password_line = line.strip()
                    #makes sure it is not assuming that there is a comma
                    password_parts = password_line.split(",", 1)
                    if len(password_parts) > 1:
                        file_app_name = password_parts[0].strip()
                        password = password_parts[1].strip()
                    break
                line = f.readline()
        #if password equals none then it means it doesn't exist
        if password == None:
            print("That app either doesn't exist in your passwords or you entered the name wrong!\n")
            pick_option()
    except FileNotFoundError as err:
        print("File Not Found Error: " + err)
        print(exit)
        exit()
    except Exception as err:
        print("An error occurred.")
        logging.exception(err)
        print(exit)
        exit()
    
    #prints the password and app name they want
    print("Here is the current app name and password:")
    temp = Password(file_app_name, password)
    print(temp.toString())
        
    #sets the new name and/or password to the current
    new_name = file_app_name
    new_password = password
        
        
    while(True):
        #asks the user whether they would like to change
        #the app name or the password
        check = input("Would you like to change the app name or the password (n or p): ")
        print("")           
        if check.upper() == "N":
            new_name = input("What would you like the new name to be?: ")
            break
        elif check.upper() == "P":
            length = random.randint(8, 12)
            rec = generate_recommended(length)
            print("Recommended: " + rec)
            use_rec = input("Would you like to use the recommended password?(yes or no): ")
            while(True):
                if use_rec.upper() == "YES":
                    new_password = rec
                    break
                elif use_rec.upper() == "NO":
                    new_password = input("What would you like the new password to be?: ")
                    break
                else:
                    print("That is not a valid response!")
                    print("Recommended: " + rec)
                    use_rec = input("Would you like to use the recommended password?(yes or no): ")
                    continue
            break
        #if the user does not respond with n or p, then
        #it asks the question again and reports back
        else:
            print("That is not a valid response!")
            continue
    #adds new variable to put in the correct format on the file
    new_line = new_name + "," + new_password
    #sets an updated variable to false
    updated = False
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
        with open("passwords.txt", "w") as x:
        #goes line by line and splits into parts to check
        #if app name matches the user input
            for line in lines:
                line_parts = line.split(",", 1)
                if len(line_parts) > 1:
                    appname = line_parts[0]
            #if it doesn't match, it writes it to the file
                if (appname.strip()).lower() != file_app_name.lower():
                    x.write(line)
            #if it does match, it sets deleted to true, doesn't write
                else: 
                    x.write(new_line + '\n')
                    updated = True
        if updated:
                print("Password wass successfully updated!")
                pick_option()
        else:
            print("An error occurred when trying to update your password.")
            pick_option()
    except FileNotFoundError as err:
        print("File Not Found Error: " + err)
        print(exit)
        exit()
    except Exception as err:
        print("An error occurred.")
        logging.exception(err)
        print(exit)
        exit()
        
        
def get_password():
    print("")
    #gets the name of the app from the user 
    app_name = input("What is the name of the app?: ")
    #sets password as non instead of "" better syntax
    password = None
    
    try:
        #opens file and reads line by line to find the password that the user wants
        with open("passwords.txt", "r") as f:
            line = f.readline()
            while(line != ""):
                #makes sure it is not case sensitive
                if ((line.lower()).find(app_name.lower()) != -1):
                    password_line = line.strip()
                    #makes sure it is not assuming that there is a comma
                    password_parts = password_line.split(",", 1)
                    if len(password_parts) > 1:
                        password = password_parts[1].strip()
                    break
                line = f.readline()
        #if password equals none then it means it doesn't exist
        if password == None:
            print("That app either doesn't exist in your passwords or you entered the name wrong!\n")
            pick_option()
            
        #prints the password and app name they want
        print("Here is the password for " + app_name + ": " + password)
        print("")
        pick_option()
    except FileNotFoundError as err:
        print("File Not Found Error: " + err)
        print(exit)
        exit()
    except Exception as err:
        print("An error occurred.")
        logging.exception(err)
        print(exit)
        exit()



def delete_password():
    deleted = False
    #asks the user for the password they would like to delete
    user_pass = input("\nWhat password would you like to delete?: ")
    
    #opens in read mode and reads all lines and puts it in var
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
        #opens password in write which deletes everything in file
        with open("passwords.txt", "w") as x:
            #goes line by line and splits into parts to check
            #if app name matches the user input
            for line in lines:
                line_parts = line.split(",", 1)
                if len(line_parts) > 1:
                    appname = line_parts[0]
                #if it doesn't match, it writes it to the file
                if (appname.strip()).lower() != user_pass.lower():
                    x.write(line)
                #if it does match, it sets deleted to true, does'nt write
                else: 
                    deleted = True
        
        #validation message to let the user know if it deleted it            
        if deleted:
            print(user_pass + " password has been deleted!")
        else:
            print("Could not find the password you were looking to delete")
        pick_option()
    #throws error if it can't open the file for some reason
    except FileNotFoundError as err:
        print("File Not Found Error: " + str(err))
        print(exit)
        exit()
    #not good programming practice to just use the broad range
    #of the exception class so logging it is good
    except Exception as err:
        print("An error occured.")
        logging.exception(err)
        print(exit)
        exit()
    
def create_password():
    print("")
    #gets app name
    app_name = input("What is the name of your platform that you want to create a password on?: ")
    #generates random password and asks the user whether they would want to use it
    length = random.randint(8, 12)
    rec = generate_recommended(length)
    print("Recommended: " + rec)
    use_rec = input("Would you like to use the recommended password?(yes or no):  ")
    #makes sure the user enters yes or no, if they say no
    #it asks what passwrod the user wants to set
    while(True):
        if use_rec.upper() == "YES":
            password = rec
            print("You set the password as: " + password)
            break
        elif use_rec.upper() == "NO":
            password = input("What would you like the password to be?: ")
            print("You set the password as: " + password)
            break
            
        print("Invalid answer, please enter 'yes' or 'no'")
        print("Reccommended: " + rec)
        use_rec = input("Would you like to use the recommended password?(yes or no):  ")
        print("")
        #LOOK AT THIS - do we use the class? 
    new_password = Password(app_name, password)
    print(new_password.toString())
    
    #opens the file and catches if there is an error
    #writes the app name and password to passwords.txt
    try:
        with open("passwords.txt", "a+") as file:
            line = app_name + "," + password
            file.write(line + "\n")
    except FileNotFoundError as err:
        print("File Not Found Error: ", err)
        print(exit)
        exit()
    except Exception as err:
        print("An error occurred.")
        logging.exception(err)
        print(exit)
        exit()
    #confirmation message, goes to pick_option()
    print("Password added!")
    print("------------------------------")
    pick_option()
    
            
        
            
    
    


def pick_option():
    resume = input("Press Enter to continue to options, type exit to stop: \n")
    if resume.upper() == "EXIT":
        exit()
    print("------------------------------")
    print("Here are your options!")
    print("")
    #uses a list to print out options so it reduces lines
    options = ["Update a password", "Find a password", "Delete a password", "Create new password"]
    #for loop to go through the list and print number using var i
    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i])
    print("")
    
    
    
    
    #uses a while loop to make sure the user enters a valid option
    while(True):
        #makes sure anser is an integer
        try:
            choice = int(input("Please pick the number of your choice: "))
            #makes sure the number is in range(even with varying option selection)
            if choice < 1 or choice > len(options):
                print("Invalid choice. Please pick an option between 1 and " + str(len(options)))
                print("")
                continue
            break
        
        except ValueError:
            print("Invalid choice. Please type a number.")
            print("")
    print("")
    print("------------------------------")
    print("")
    
    
    #uses if statements to call whatever option the user chooses and verifies choice
    if choice == 1:
        print("You chose to update a password!")
        update_password()
    elif choice == 2:
        print("You chose to find a password!")
        get_password()
    elif choice == 3:
        print("You chose to delete a password!")
        delete_password()
    else:
        print("You chose to create a password!")
        create_password()
    
            
        
    


#start_manager() starts the program 
def start_manager():
    #creates loading screen by overwriting the lines
    #it also uses time.sleep()
    print("Starting password manager....")
    for i in range(1, 30):
        symbol = "-"*i
        print(symbol, end="\r")
        time.sleep(.1)
    print("")
    
    #opens the file using with and as
    with open("name.txt", "r+") as f:
        name = (f.readline()).strip()
        #if name doesn't exist it asks for the name and welcomes
        
        
        
        if name == "":
            name = input("We have noticed you either " \
            + "haven't given us a name or are new to the program,"\
            + " what is your name?: ")
            #writes new name to the file and welcomes the user
            f.write(name)
            print("")
            print("Welcome, " + name + " to the password manager!")
            
        #else it welcomes back the user cause name exists
        else:
            f.close()
            print("Hello, " + name + "!")
            print("Welcome back!")
    
    #gives a pause time for the user to continue to the next part
    print("")
    pick_option()
    
    
            
start_manager()
