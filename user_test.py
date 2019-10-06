import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp (self):

        self.new_account = User ("leon","bichanga","lehann")

    def test_init(self):
        
        self.assertEqual(self.new_account.firstname,"leon")
        self.assertEqual(self.new_account.lastname,"bichanga")
        self.assertEqual(self.new_account.password,"lehann")

if __name__ == '__main__':
    unittest.main()