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
        

    def test_init(self):
        '''
        test to check if the object is initialized correctly
        '''
        self.assertEqual(self.new_user.username,"brian")
        self.assertEqual(self.new_user.password, "mumo")
        
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


    
   



if __name__ == '__main__':
    unittest.main()
