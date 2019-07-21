import unittest
from password import User
from  credentials import Credentials 

class TestUser(unittest.TestCase):
    '''
    Test class which defines test cases for the user class functions
    '''
    def setUp(self):
        '''
        setup method to run before each case
        '''
        self.new_user = User("brian", "mumo")
        self.new_credential = Credentials("twitter", "brayomull7", "mumo")

    def test_init(self):
        '''
        test to check if the object is initialized correctly
        '''
        self.assertEqual(self.new_user.username,"brian")
        self.assertEqual(self.new_user.password, "mumo")
        self.assertEqual(self.new_credential.account_name,"twitter")
        self.assertEqual(self.new_credential.account_uName, "brayomull7")
        self.assertEqual(self.new_credential.account_password, "mumo")

    def test_save_user(self):
        '''
        test if the user is being saved 
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        test does a clean up after every test
        '''
        User.user_list = []


    def test_show_users(self):
        '''
        test show user function
        '''
        self.assertEqual(User.show_user(),User.user_list)


    def save_credential(self):
        ''' 
        test saving credentials
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()
