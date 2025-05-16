import unittest
from controller import UserLoginController

class TestLoginLogic(unittest.TestCase):
    def setUp(self):
        self.controller = UserLoginController()

    def test_admin_login(self):
        # Use a real known user in your DB
        result = self.controller.checkCredentials("admin1", "12345")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["role_id"], 1)

    def test_cleaner_login(self):
        # Use a real known user in your DB
        result = self.controller.checkCredentials("cleaner1", "12345")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["role_id"], 2)

    def test_HO_login(self):
        # Use a real known user in your DB
        result = self.controller.checkCredentials("homeowner1", "12345")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["role_id"], 3)
    
    def test_PM_login(self):
        # Use a real known user in your DB
        result = self.controller.checkCredentials("platform1", "12345")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["role_id"], 4)

    def test_invalid_login(self):
        result = self.controller.checkCredentials("admin1", "123")
        self.assertEqual(result["status"], "fail")

    

    def test_nonexistent(self):
        result = self.controller.checkCredentials("ghost1", "ghost")
        self.assertEqual(result["status"], "fail")

    def test_suspended_user(self):
        result = self.controller.checkCredentials("xxerii", "12345")
        self.assertEqual(result["status"], "suspended")

if __name__ == '__main__':
    unittest.main()