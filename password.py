
class User:

    #store the user 
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def show_user(cls):
        '''
        function returns list of users
        '''

        return cls.user_list

    @classmethod
    def comfirm_user(cls, username, password):
        '''
        confirms wheteher the user is in the list
        '''
        current_user = ''
        for user in User.user_list:
            if(User..username == username and user.password == password):
                current_user == User.username
            return current_user