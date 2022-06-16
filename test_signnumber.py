from re import S
import unittest

from signnumber import SignNumber

class SignNumberTest(unittest.TestCase) :

    def test_determine_priority_addition(self) : 
        sign_number = SignNumber("98+65",0,0,0)
        
        sign_number.determine_priority()

        self.assertEqual(1, sign_number.priority)


    def test_determine_priority_substraction(self) : 
        sign_number = SignNumber("98-65",0,0,0)
        
        sign_number.determine_priority()

        self.assertEqual(1, sign_number.priority)


    def test_determine_priority_multiplication(self) : 
        sign_number = SignNumber("98*65",0,0,0)
        
        sign_number.determine_priority()

        self.assertEqual(2, sign_number.priority)


    def test_determine_priority_division(self) : 
        sign_number = SignNumber("98/65",0,0,0)
        
        sign_number.determine_priority()

        self.assertEqual(2, sign_number.priority)
    

    def test_determine_sign_simple(self) :
        sign_number_first = SignNumber("32+21",0,0,0)
        sign_number_second = SignNumber("32-21",0,0,0)
        sign_number_third = SignNumber("32*21",0,0,0)
        sign_number_fourth = SignNumber("32/21",0,0,0) 

        sign_number_first.determine_sign()
        sign_number_second.determine_sign()
        sign_number_third.determine_sign()
        sign_number_fourth.determine_sign()

        self.assertEqual(1, len(sign_number_first.sign))
        self.assertEqual(1, len(sign_number_second.sign))
        self.assertEqual(1, len(sign_number_third.sign))
        self.assertEqual(1, len(sign_number_fourth.sign))

        self.assertEqual("+", sign_number_first.sign[0])
        self.assertEqual("-", sign_number_second.sign[0])
        self.assertEqual("*", sign_number_third.sign[0])
        self.assertEqual("/", sign_number_fourth.sign[0])
        

    def test_determine_sign_complexe(self) :
        sign_number_first = SignNumber("32+-21",0,0,0)
        sign_number_second = SignNumber("32--21",0,0,0)
        sign_number_third = SignNumber("32*-21",0,0,0)
        sign_number_fourth = SignNumber("32/-21",0,0,0) 

        sign_number_first.determine_sign()
        sign_number_second.determine_sign()
        sign_number_third.determine_sign()
        sign_number_fourth.determine_sign()

        self.assertEqual("+", sign_number_first.sign[0])
        self.assertEqual("-", sign_number_first.sign[1])
        self.assertEqual("-", sign_number_second.sign[0])
        self.assertEqual("-", sign_number_second.sign[1])
        self.assertEqual("*", sign_number_third.sign[0])
        self.assertEqual("-", sign_number_third.sign[1])
        self.assertEqual("/", sign_number_fourth.sign[0])
        self.assertEqual("-", sign_number_fourth.sign[1])


    def test_determine_sign_unknown(self) :
        sign_number = SignNumber("42x",0,0,0)
        
        sign_number.determine_sign()
        
        self.assertEqual("*", sign_number.sign[0])