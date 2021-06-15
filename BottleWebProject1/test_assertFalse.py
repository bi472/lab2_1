import unittest
import myform_mail

list_mail_uncor = ["", "1", "m1@", "@mail","word"]

class Test_assertFalse(unittest.TestCase):
    def test_A(self):
        for i in list_mail_uncor:
            self.assertFalse(myform_mail.test_regular(i))

if __name__ == '__main__':
    unittest.main()
