import unittest
import re

def validate_email(email):
    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|edu|net)"
    if re.match(pattern, email):
        return True
    else:
        return False

class TestEmailValidator(unittest.TestCase):
    def test_email_validator(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("abc123@mydomain.org"))
        self.assertFalse(validate_email("test@.com"))
        self.assertFalse(validate_email("@example.com"))
        self.assertFalse(validate_email("testexample.com"))
        self.assertFalse(validate_email("test@example"))
        self.assertFalse(validate_email("test@.com"))
        

if __name__ == "__main__":
    unittest.main()