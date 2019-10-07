import unittest
from user import User
from user import Credentials


class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_account = User("leon", "bichanga", "bchizi", "lehann")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):

        self.assertEqual(self.new_account.firstname, "leon")
        self.assertEqual(self.new_account.lastname, "bichanga")
        self.assertEqual(self.new_account.username, "bchizi")
        self.assertEqual(self.new_account.password, "lehann")

    def test_save_user(self):
        self.new_account.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        self.new_account.save_user()
        test_user = User("chris", "jaire", "chrisj", "jaish")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


class TestCredentials(unittest.TestCase):

    def setUp(self):
       self.new_account = Credentials ("instagram","bchizi","lehann")
    
    def tearDown(self):
        Credentials.credentials_list=[]

    def test_credential_init(self):
        self.assertEqual(self.new_account.social_account,"instagram")
        self.assertEqual(self.new_account.social_username,"bchizi")
        self.assertEqual(self.new_account.social_password,"lehann")

    

    def test_delete_user(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_account.save_credentials()  
        test_user = User("Test", "user", "0712345678", 
                         "test@user.com")  # new contact
        test_user.save_user()
        self.new_account.delete_user()  # deleting a user object
        self.assertEqual(len(User.user_list), 1)
        


if __name__ == '__main__':
    unittest.main()
