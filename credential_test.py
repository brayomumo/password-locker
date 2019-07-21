import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    '''
    test class to test credentials functions
    '''
    def setUp(self):
        self.new_credential = Credentials("twitter", "brayomull7", "mumo")

    def  test_init(self):
        self.assertEqual(self.new_credential.account_name,"twitter")
        self.assertEqual(self.new_credential.account_uName, "brayomull7")
        self.assertEqual(self.new_credential.account_password, "mumo")

    def test_save_credential(self):
        ''' 
        test saving credentials
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credentials("twitter", "brayomull7", "mumo")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential_by_accountname(self):
        '''
        search for credential using username
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("instagram", "brayomumo", "mumoo")
        test_credential.save_credential()

        credential_exist = Credentials.find_by_accountname("instagram")
        self.assertTrue(credential_exist)

    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)





if __name__ == '__main__':
    unittest.main()
