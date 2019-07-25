#!/usr/bin/env python

from password import User
from credentials import Credentials


#create user


def create_user(username, password):
    '''
    Create new user 
    '''

    new_user = User(username, password)
    return new_user


# save user
def save_new_user(username):
    ''''
    saving the new user
    '''
    User.user_list.append(username)


#cofirm user
def confirm_user(username, password):
    confirm_user = User.confirm_user(username, password)

    return confirm_user


#create credentials
def create_credential(account_name, account_uName, account_password):
    new_credential = Credentials(account_name, account_password, account_uName)
    return new_credential


#save credentials

def save_account(Credentials):
    Credentials.save_credential()


#delete Credentials
def delete(Credentials):
    Credentials.delete_credential()


#search Credentials
def search(Credentials):
    return Credentials.find_by_accountname()


#display all credentials
def display_cred():
    return Credentials.display_credentials()


#generate assword
def gennerate_pwd():
    pswd = Credentials.generate_password()
    return pswd


#main function
def main():
    print("Hello \n Welcome to your account manager app. What is your name?")
    my_name = input()

    print(f"Welcome {my_name}! ")
    print('\n')

    while True:
        print("Use these short codes to experience the account manager app:\nca- create an account (For first-timers)\nla- log into an account\nex- exit an account")
        shortcode = input().lower()
        print('\n')

        if shortcode == 'ca':
            print("Your username:")
            u_name = input()
            print("Do you want to autogenerate a password (Choose 'y' or 'n') ?")
            while True:
                choice = input().lower()
                if choice == 'y':
                    accountpassword = User.generate_password()
                    print(f"This is your password- {accountpassword}")
                    break
                elif choice == 'n':
                    print("Enter your password for the account")
                    accountpassword = input()
                    print(f"This is your password- {accountpassword}")
                    break
                else:
                    print(" Please choose 'y' or 'n' ")
            # create and save new user.
            save_new_user(create_user(u_name, accountpassword))
            print('\n')
            print(f"***{u_name} your account has been created***")
            print('\n')

        elif shortcode == 'la':
            print("Enter your username")
            u_name = input()
            print("Enter your password")
            p_word = input()

            if not User.user_list:  # code to check if user list is empty
                print('\n')
                print("***You are not in the system***")

            for user in User.user_list:

                if u_name == user.username and p_word == user.password:

                    print('''
                    ***
                    Login Successful.
                    ***
                    ''')
                    print('\n')

                    print(f"Welcome {u_name}! So, what would you like to do?")

                    while True:
                        print(
                            "Use these short codes : cc - create new credentials, dc - display credenials,  del- delete user credenials, lv -exit the user list")

                        short_code = input().lower()

                        if short_code == 'cc':
                            # print("-" * 10)

                            print("Enter your Account name:")
                            a_name = input()
                            print("Enter your username:")
                            u_name = input()
                            print(
                                "Do you want to autogenerate a password (Choose 'y' or 'n') ?")
                            while True:
                                choice = input().lower()
                                if choice == 'y':
                                    credentialpassword = Credentials.generate_password()
                                    print(
                                        f"This is your password- {credentialpassword}")
                                    break
                                elif choice == 'n':
                                        print(
                                            "Enter your password for the account")
                                        credentialpassword = input()
                                        print(
                                            f"This is your password- {credentialpassword}")
                                        break
                                else:
                                        print(" Please choose 'y' or 'n' ")
                                # create and save new credenials.
                            save_account(create_credential(
                                a_name, u_name, credentialpassword))

                            print('\n')
                            print(
                                f"*** New credentials saved for {u_name} ***")
                            print('\n')

                        elif short_code == 'dc':
                            if display_cred():
                                print('\n')

                            # loops through credential object & gets each user
                                for credential in display_cred():
                                    print(f"***Here is a list of {u_name}'s credentials: {credential.account_name}-{credential.account_uName}-{credential.account_password}***")
                                    print('\n')
                            else:
                                print("***No user credentials saved***")
                                print('\n')

                        elif short_code == 'del':
                            print(
                                "Enter your account username so that account can be deleted")

                            search_username = input()
                            if search(search_username):
                                search_credential = search(
                                    search_username)
                                delete(search_credential)
                                print(f"{search_username} is deleted")

                            else:
                                print("***That username doesn't exist***")

                        elif short_code == "lv":
                                print("***Until next time***")
                                break

                        else:
                            print("***Back to the shortcodes. Choose one.***")
                            print('\n')

                else:
                    print(
                        "***Username or Email isn't valid. Try again or Sign Up as a New User***")
                    print('\n')

        elif shortcode == "ex":
                print("Until next time")
                print('\n')
                break

        else:
            print("***Back to the shortcodes. Choose one.***")


if __name__ == '__main__':
    main()
