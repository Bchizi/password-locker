import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp (self):

        self.new_account = User ("leon","bichanga","bchizi","lehann")

    def test_init(self):

        self.assertEqual(self.new_account.firstname,"leon")
        self.assertEqual(self.new_account.lastname,"bichanga")
        self.assertEqual(self.new_account.username,"bchizi")
        self.assertEqual(self.new_account.password,"lehann")

    def test_save_user(self):
        self.new_account.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()