import unittest

from analyze import Analyze

class AnalyseTest(unittest.TestCase) :

    def test_find_parts(self) :
        analyze = Analyze("87x+765-7653=987")
        
        analyze.get_parts()

        self.assertEqual(2, len(analyze.parts))
        self.assertEqual("87x+765-7653", analyze.parts[0].text)
        self.assertEqual("987", analyze.parts[1].text)


    def test_get_index_signs(self) : 
        analyze_first = Analyze("87x+86=80")
        analyze_second = Analyze("46-7x=6545")
        analyze_third = Analyze("85x*87=654")
        analyze_fourth = Analyze("459x/7=65")

        result_index_first = analyze_first.get_index_signs("+")
        result_index_second = analyze_second.get_index_signs("-")
        result_index_third = analyze_third.get_index_signs("*")
        result_index_fourth = analyze_fourth.get_index_signs("/")

        self.assertEqual(3, result_index_first)
        self.assertEqual(2, result_index_second)
        self.assertEqual(3, result_index_third)
        self.assertEqual(4, result_index_fourth)


    def test_get_index_signs_complex(self) : 
        analyze_first = Analyze("87x+-86=80")
        analyze_second = Analyze("46--7x=6545")
        analyze_third = Analyze("85x*-87=654")
        analyze_fourth = Analyze("459x/-7=65")

        result_index_first = analyze_first.get_index_signs("+-")
        result_index_second = analyze_second.get_index_signs("--")
        result_index_third = analyze_third.get_index_signs("*-")
        result_index_fourth = analyze_fourth.get_index_signs("/-")

        self.assertEqual(3, result_index_first)
        self.assertEqual(2, result_index_second)
        self.assertEqual(3, result_index_third)
        self.assertEqual(4, result_index_fourth)


    def test_detects_signs(self) : 
        analyze = Analyze("98x+98*67/45-9=87")

        analyze.determine_all_elements("98x+98*67/45-9=87")

        self.assertEqual(4, len(analyze.signs))
        self.assertEqual('+', analyze.signs[0])
        self.assertEqual('*', analyze.signs[1])
        self.assertEqual('/', analyze.signs[2])
        self.assertEqual('-', analyze.signs[3])


    def test_detects_signs_complex(self) : 
        analyze_first = Analyze("87x+-86=80")
        analyze_second = Analyze("46--7x=6545")
        analyze_third = Analyze("85x*-87=654")
        analyze_fourth = Analyze("459x/-7=65")

        analyze_first.determine_all_elements("87x+-86=80")
        analyze_second.determine_all_elements("46--7x=6545")
        analyze_third.determine_all_elements("85x*-87=654")
        analyze_fourth.determine_all_elements("459x/-7=65")

        self.assertEqual(1, len(analyze_first.signs))
        self.assertEqual('+-', analyze_first.signs[0])
        self.assertEqual(1, len(analyze_second.signs))
        self.assertEqual('--', analyze_second.signs[0])
        self.assertEqual(1, len(analyze_third.signs))
        self.assertEqual('*-', analyze_third.signs[0])
        self.assertEqual(1, len(analyze_fourth.signs))
        self.assertEqual('/-', analyze_fourth.signs[0])
        

    def test_is_numeral(self) : 
        analyze = Analyze("9x-87x=7")

        is_numeral_first = analyze.is_numeral('9')
        is_numeral_second = analyze.is_numeral('x')
        is_numeral_third = analyze.is_numeral('-')
        is_numeral_fourth = analyze.is_numeral('/')
        is_numeral_fifth = analyze.is_numeral('=')
        is_numeral_sixth = analyze.is_numeral('*')
        is_numeral_seventh = analyze.is_numeral('+')


        self.assertTrue(is_numeral_first)
        self.assertFalse(is_numeral_second)
        self.assertFalse(is_numeral_third)
        self.assertFalse(is_numeral_fourth)
        self.assertFalse(is_numeral_fifth)
        self.assertFalse(is_numeral_sixth)
        self.assertFalse(is_numeral_seventh)


    def test_determine_elements_text(self) :
        analyze = Analyze("9x-87x=7")

        analyze.determine_all_elements("3x+3=15")

        self.assertEqual(analyze.text,"3x+3=15" )


    def test_determine_elements_small_eq(self) :
        analyze = Analyze("x+5=7")

        analyze.determine_all_elements("x+5=7")

        self.assertEqual(2, len(analyze.numbers))
        self.assertEqual(analyze.numbers[0],"5" )
        self.assertEqual(analyze.numbers[1],"7" )
        self.assertEqual(1, len(analyze.signs))
        self.assertEqual("+", analyze.signs[0])


    def test_determine_elements_medium_eq(self) :
        analyze = Analyze("3x+3=15")

        analyze.determine_all_elements("3x+3=15")

        self.assertEqual(3, len(analyze.numbers))
        self.assertEqual(analyze.numbers[0],"3" )
        self.assertEqual(analyze.numbers[1],"3" )
        self.assertEqual(analyze.numbers[2],"15" )
        self.assertEqual(1, len(analyze.signs))
        self.assertEqual("+", analyze.signs[0])


    def test_validate_equation_is_ok(self) :
        analyze = Analyze("23x+6 = 66")

        isOk = analyze.is_validate()

        self.assertTrue(isOk)
    
    
    def test_validate_no_letter(self) : 
        analyze = Analyze("98x+43a = 87")
        
        isOk = analyze.is_validate()
        
        self.assertFalse(isOk)


    def test_validate_division_multiplication_separated(self) :
        analyze = Analyze("09x/*2=67" )

        isOk = analyze.is_validate()

        self.assertFalse(isOk)


    def test_validate_equal_equation(self) : 
        analyze_no_equal = Analyze("87x*867")
        analyzeFirst = Analyze("=92x+87")
        analyzeSecond = Analyze("92x+87=")
        analyzeThird = Analyze("92x+87+=3")
        analyzeFourth = Analyze("92x+87-=3")
        analyzeFifth = Analyze("92x+87*=3")
        analyzeSixth = Analyze("92x+87/=3")

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
        analyze = Analyze("32=87x*867")

        isOk = analyze.is_validate()

        self.assertFalse(isOk)


    def test_validate_relatif_understood(self) :
        analyze_first = Analyze("-98x/87=765")
        analyze_second = Analyze("+98x/87=765")
        analyze_third = Analyze("*98x/87=765")
        analyze_fourth = Analyze("/98x/87=765")

        is_ok_first = analyze_first.is_validate()
        is_ok_second = analyze_second.is_validate()
        is_ok_third = analyze_third.is_validate()
        is_ok_fourth = analyze_fourth.is_validate()

        self.assertTrue(is_ok_first)
        self.assertTrue(is_ok_second)
        self.assertFalse(is_ok_third)
        self.assertFalse(is_ok_fourth)


    def test_validate_multiplication_division(self) :
        analyze = Analyze("09x/*2=67" )
        analyze_first = Analyze("98x+/87=765")
        analyze_second = Analyze("+98x-*87=765")

        is_ok = analyze.is_validate()
        is_ok_first = analyze_first.is_validate()
        is_ok_second = analyze_second.is_validate()
        
        self.assertFalse(is_ok)
        self.assertFalse(is_ok_first)
        self.assertFalse(is_ok_second)   



    def test_validate_relative_eq(self) : 
        first_analyze = Analyze("x+-2=2")
        second_analyze = Analyze("x--2=4")
        third_analyze = Analyze("x*-5=10")
        fourth_analyze = Analyze("x/-5=10")

        is_ok_first = first_analyze.is_validate()
        is_ok_second = second_analyze.is_validate()
        is_ok_third = third_analyze.is_validate()
        is_ok_fourth = fourth_analyze.is_validate()

        self.assertTrue(is_ok_first)
        self.assertTrue(is_ok_second)
        self.assertTrue(is_ok_third)
        self.assertTrue(is_ok_fourth)