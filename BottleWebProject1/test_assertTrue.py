import unittest
import myform_mail

list_mail_cor = ["m.m@mail.ru", "m1@gmail.com","m232@list.ru"]

class Test_assertTrue(unittest.TestCase):
    def test_A(self):
        for i in list_mail_cor:
            self.assertTrue(myform_mail.test_regular(i))

if __name__ == '__main__':
    unittest.main()
