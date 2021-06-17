import unittest
import test

list_mail_f = ["m@mailru", "cal.ru", "mor@"]
list_mail_t = ["1@mail.ru", "123p@mail.ru", "test@gmail.com"]

list_phone_f = ["4353453454354", "35234234234", "+7 234 555 11 11"]
list_phone_t = ["+8 (999) 999-23-23", "+9 (999) 999-99-99", "+7 (777) 777-77-77"]

class Test_test(unittest.TestCase):
    def test_A_mail(self):
        for str in list_mail_f:
            self.assertFalse(test.check_mail(str))
    def test_B_mail(self):
        for str in list_mail_t:
            self.assertTrue(test.check_mail(str))
    def test_A_phone(self):
        for str in list_phone_f:
            self.assertFalse(test.check_phone(str))
    def test_B_phone(self):
        for str in list_phone_t:
            self.assertTrue(test.check_phone(str))

if __name__ == '__main__':
    unittest.main()
