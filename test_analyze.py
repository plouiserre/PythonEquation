import unittest

from analyze import Analyze

class AnalyseTest(unittest.TestCase) :

    def test_validate_equation_is_ok(self) :
        equation = "23x+6 = 66"
        analyze = Analyze(equation)

        isOk = analyze.is_validate()

        self.assertTrue(isOk)
    
    
    def test_validate_no_letter(self) : 
        equation = "98x+43a = 87"
        analyze = Analyze(equation)
        
        isOk = analyze.is_validate()
        
        self.assertFalse(isOk)

    def test_validate_division_multiplication_separated(self) :
        equation = "09x/*2=67" 
        analyze = Analyze(equation)

        isOk = analyze.is_validate()

        self.assertFalse(isOk)


    def test_validate_equal_equation(self) : 
        equation_no_equal = "87x*867"
        analyze_no_equal = Analyze(equation_no_equal)
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

        isOk = analyze_no_equal.is_validate()
        isOkFirst = analyzeFirst.is_validate()
        isOkSecond = analyzeSecond.is_validate()
        isOkThird = analyzeThird.is_validate()
        isOkFourth = analyzeFourth.is_validate()
        isOkFifth = analyzeFifth.is_validate()
        isOkSixth = analyzeSixth.is_validate()

        self.assertFalse(isOk)
        self.assertFalse(isOkFirst)
        self.assertFalse(isOkSecond)
        self.assertFalse(isOkThird)
        self.assertFalse(isOkFourth)
        self.assertFalse(isOkFifth)
        self.assertFalse(isOkSixth)


    def test_validate_unknown_equation(self) :
        equation = "32=87x*867"
        analyze = Analyze(equation)

        isOk = analyze.is_validate()

        self.assertFalse(isOk)


    def test_validate_relatif_understood(self) :
        first_equation = "-98x/87=765"
        analyze_first = Analyze(first_equation)
        second_equation = "+98x/87=765"
        analyze_second = Analyze(second_equation)
        third_equation = "*98x/87=765"
        analyze_third = Analyze(third_equation)
        fourth_equation ="/98x/87=765"
        analyze_fourth = Analyze(fourth_equation)

        is_ok_first = analyze_first.is_validate()
        is_ok_second = analyze_second.is_validate()
        is_ok_third = analyze_third.is_validate()
        is_ok_fourth = analyze_fourth.is_validate()

        self.assertTrue(is_ok_first)
        self.assertTrue(is_ok_second)
        self.assertFalse(is_ok_third)
        self.assertFalse(is_ok_fourth)


    def test_validate_multiplication_division(self) :
        equation = "09x/*2=67" 
        analyze = Analyze(equation)
        first_equation = "98x+/87=765"
        analyze_first = Analyze(first_equation)
        second_equation = "+98x-*87=765"
        analyze_second = Analyze(second_equation)

        is_ok = analyze.is_validate()
        is_ok_first = analyze_first.is_validate()
        is_ok_second = analyze_second.is_validate()
        
        self.assertFalse(is_ok)
        self.assertFalse(is_ok_first)
        self.assertFalse(is_ok_second)


    def test_identification_signs_numbers(self) : 
        equation = "98x+75/53*34-96=89"
        analyze = Analyze(equation)

        is_validate = analyze.is_validate()
        analyze.identification()
        signs_numbers = analyze.equation.parts[0].signs_numbers

        self.assertTrue(is_validate)
        self.assertEqual(4, len(signs_numbers))
        self.assertEqual('98x+75', signs_numbers[0].text)
        self.assertEqual('75/53', signs_numbers[1].text)
        self.assertEqual('53*34', signs_numbers[2].text)
        self.assertEqual('34-96', signs_numbers[3].text)



    def test_identifications_relatifs_numbers(self) : 
        equation = "98x+75/-53*-34-96=89"
        analyze = Analyze(equation)

        is_validate = analyze.is_validate()
        analyze.identification()
        signs_numbers = analyze.equation.parts[0].signs_numbers

        self.assertTrue(is_validate)
        self.assertEqual(4, len(signs_numbers))
        self.assertEqual('98x+75', signs_numbers[0].text)
        self.assertEqual('75/-53', signs_numbers[1].text)
        self.assertEqual('53*-34', signs_numbers[2].text)
        self.assertEqual('34-96', signs_numbers[3].text)

    
    def test_identifications_multi_occurences(self) : 
        equation = "98x+75/-53*-34-98=89"
        analyze = Analyze(equation)

        is_validate = analyze.is_validate()
        analyze.identification()
        signs_numbers = analyze.equation.parts[0].signs_numbers

        self.assertTrue(is_validate)
        self.assertEqual(4, len(signs_numbers))
        self.assertEqual('98x+75', signs_numbers[0].text)
        self.assertEqual('75/-53', signs_numbers[1].text)
        self.assertEqual('53*-34', signs_numbers[2].text)
        #TODO modifier l'algo pour que ca soit -34-98
        self.assertEqual('34-98', signs_numbers[3].text)


    def test_position_sign_numbers(self) : 
        equation = "87x+65/-69*89=666"
        analyze = Analyze(equation)

        is_validate = analyze.is_validate()
        analyze.identification()
        signs_numbers = analyze.equation.parts[0].signs_numbers
        first_sign_number = signs_numbers[0]
        second_sign_number = signs_numbers[1]
        third_sign_number = signs_numbers[2]

        self.assertTrue(is_validate)
        self.assertEqual(3, len(signs_numbers))
        self.assertEqual("87x+65", first_sign_number.text)
        self.assertEqual(0, first_sign_number.position)
        self.assertEqual("65/-69", second_sign_number.text)
        self.assertEqual(1, second_sign_number.position)
        self.assertEqual("69*89", third_sign_number.text)
        self.assertEqual(2, third_sign_number.position)
    