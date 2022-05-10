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

    
    def test_multiplication_division_separated(self) :
        equation = "09x*/2=67" 
        analyze = Analyze(equation)

        isOk = analyze.IsValidate()

        self.assertFalse(isOk)


    def test_division_multiplication_separated(self) :
        equation = "09x/*2=67" 
        analyze = Analyze(equation)

        isOk = analyze.IsValidate()

        self.assertFalse(isOk)



    def test_equal_is_missing(self) :
        equation = "87x*867"
        analyze = Analyze(equation)

        isOk = analyze.IsValidate()

        self.assertFalse(isOk)



    def test_equal_is_wrong_place(self) : 
        equationFirst = "=92x+87"
        analyzeFirst = Analyze(equationFirst)
        equationSecond = "92x+87="
        analyzeSecond = Analyze(equationSecond)
        equationThird = "92x+87+=3"
        analyzeThird = Analyze(equationThird)
        equationFourth = "92x+87-=3"
        analyzeFourth = Analyze(equationFourth)
        equationFifth = "92x+87*=3"
        analyzeFifth = Analyze(equationFifth)
        equationSixth = "92x+87/=3"
        analyzeSixth = Analyze(equationSixth)

        isOkFirst = analyzeFirst.IsValidate()
        isOkSecond = analyzeSecond.IsValidate()
        isOkThird = analyzeThird.IsValidate()
        isOkFourth = analyzeFourth.IsValidate()
        isOkFifth = analyzeFifth.IsValidate()
        isOkSixth = analyzeSixth.IsValidate()

        self.assertFalse(isOkFirst)
        self.assertFalse(isOkSecond)
        self.assertFalse(isOkThird)
        self.assertFalse(isOkFourth)
        self.assertFalse(isOkFifth)
        self.assertFalse(isOkSixth)


    def test_unknown_in_left_part(self) :
        equation = "32=87x*867"
        analyze = Analyze(equation)

        isOk = analyze.IsValidate()

        self.assertFalse(isOk)