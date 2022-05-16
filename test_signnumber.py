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
    