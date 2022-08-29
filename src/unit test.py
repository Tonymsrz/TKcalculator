import unittest

from calculator import click_button
from calculator import CAL
from calculator import btnclear
from calculator import btnback


class MyTestCase(unittest.TestCase):
    def test_functions(self):
        print("1 for 'sqrt'\n2 for 'MR'\n3 for '='\n4 for 'M+'\n5 for 'M-'")
        a = input("number：")
        a = int(a)
        if a == 1:  # sqrt功能
            result = CAL('sqrt')[0]
            self.assertEqual(result, 3.0)
        elif a == 2:  # MR功能
            self.assertEqual(CAL('MR')[0], 32)
        elif a == 3:  # =功能
            result = CAL('=')[0]
            self.assertEqual(result, 3)
        elif a == 4:  # M+功能
            result = CAL('M+')
            self.assertEqual(result, 14.0)
        elif a == 5:   # M-功能
            result = CAL('M-')
            self.assertEqual(result, 4.0)




    # def test_mr(self):
    #    self.assertEqual(CAL('MR'), 32)



if __name__ == '__main__':
    unittest.main()
