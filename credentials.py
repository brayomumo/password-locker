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

    def generate_password():
        chars = "abcdefghijklmnopqrstuvwxyz/*-=)%@("
        password =  ""
        for i in range(10):
            password += random.choice(chars) + str(i)
        return password

    @classmethod
    def find_by_accountname(cls, account_name):
        '''
        function to search for credentials using accountname 
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def display_credentials(cls):
        '''
        function which returns the credentials list
        '''
        return cls.credentials_list

        
    
    
    
    
