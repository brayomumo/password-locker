import random
class Credentials:


    credentials_list = []


    def __init__(self, account_name, account_uName, account_password):
        self.account_name = account_name
        self.account_password = account_password
        self.account_uName = account_uName

    def save_credential(self):
        '''
        function to save credentials
        '''

        Credentials.credentials_list.append(self)

    
    def delete_credential(self):
        '''
        deletes saved credentials
        '''
        Credentials.credentials_list.remove(self)

    
    
    
