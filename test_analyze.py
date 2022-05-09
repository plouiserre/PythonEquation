import unittest

from analyze import Analyze

class AnalyseTestTest(unittest.TestCase) :

    def test_equation_is_ok(self) :
        equation = "23x+6 = 66"
        analyze = Analyze(equation)

        isOk = analyze.IsValidate()

        self.assertTrue(isOk)
    
    
    def test_no_letter_equation(self) : 
        equation = "98x+43a = 87"
        analyze = Analyze(equation)
        
        isOk = analyze.IsValidate()
        
        self.assertFalse(isOk)
    
    '''def test_multiplication_division_separated(self) :
        equation = "09" '''