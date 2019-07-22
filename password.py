import random
class User:

    #store the user 
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def save_user(self):
        User.user_list.append(self)

    def generate_password():
       chars = "abcdefghijklmnopqrstuvwxyz/;'[]=)(*$@)"
       password = ""
       for i in range(10):
           password+=random.choice(chars)
       return password          #computated functions give a return value


    @classmethod
    def show_user(cls):
        '''
        function returns list of users
        '''

        return cls.user_list

    @classmethod
    def confirm_user(cls, username, password):
        '''
        confirms wheteher the user is in the list
        '''
        current_user = ''
        for user in User.user_list:
            if user.username == username and user.password == password:
                current_user == user.username
            return current_user