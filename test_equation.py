import unittest
from analyze import Analyze
from equation import Equation
from rewrite import Rewrite

#TODO à la fin faire des unit test pour vérifier les appels et pour tout tester
class EquationTest(unittest.TestCase) :

    def test_is_validate_equation(self) : 
        eq = self.__get_eq("x-977=78")

        eq.resolve()

        self.assertTrue(eq.is_validate)

    
    def test_is_no_validate_equation(self) : 
        eq = self.__get_eq("x/*977=78")

        eq.resolve()

        self.assertFalse(eq.is_validate)


    def test_eq_rewrite_small_eq(self) : 
        eq = self.__get_eq("x+5=7")

        eq.resolve()

        self.assertEqual(1, len(eq.steps))
        self.assertEqual("x=7-5", eq.steps[0])


    def test_eq_rewrite_medium_eq(self) : 
        eq = self.__get_eq("3x+3=15")

        eq.resolve()

        self.assertEqual(2, len(eq.steps))
        self.assertEqual("3x=15-3", eq.steps[0])
        self.assertEqual("x=12.0/3", eq.steps[1])


    def test_eq_rewrite_complex_eq(self) :
        eq = self.__get_eq("5x+5-10*5/10=30")

        eq.resolve()

        self.assertEqual(5, len(eq.steps))
        self.assertEqual("5x+5-10*5=30*10", eq.steps[0])
        self.assertEqual("5x+5-10=300.0/5", eq.steps[1])
        self.assertEqual("5x+5=60.0+10", eq.steps[2])
        self.assertEqual("5x=70.0-5", eq.steps[3])
        self.assertEqual("x=65.0/5", eq.steps[4])


    def test_eq_rewrite_complex_relative_eq(self) :
        eq = self.__get_eq("5x+-5-10*5/-10=30")

        eq.resolve()

        self.assertEqual(5, len(eq.steps))
        self.assertEqual("5x+-5-10*5=30*-10", eq.steps[0])
        self.assertEqual("5x+-5-10=-300.0/5", eq.steps[1])
        self.assertEqual("5x+-5=-60.0+10", eq.steps[2])
        self.assertEqual("5x=-50.0+5", eq.steps[3])
        self.assertEqual("x=-45.0/5", eq.steps[4])
    

    def test_solve_add_equation(self) : 
        eq = self.__get_eq("x+5=7")
        
        eq.resolve()

        self.assertEqual(2, eq.unknown_value)


    def test_solve_substract_equation(self) : 
        eq = self.__get_eq("x-5=7")
        
        eq.resolve()

        self.assertEqual(12, eq.unknown_value)
        

    def test_solve_multiply_equation_simple(self) : 
        eq = self.__get_eq("42x=84")
        
        eq.resolve()

        self.assertEqual(2, eq.unknown_value)


    def test_solve_multiply_equation_medium(self) : 
        eq = self.__get_eq("x*5=7")
        
        eq.resolve()

        self.assertEqual(1.4, eq.unknown_value)


    def test_solve_divide_equation(self) : 
        eq = self.__get_eq("x/5=7")
        
        eq.resolve()

        self.assertEqual(35, eq.unknown_value)


    def test_solve_unknown_medium_equation(self) : 
        eq = self.__get_eq("3x+3=15")
        
        eq.resolve()

        self.assertEqual(4, eq.unknown_value)


    def test_solve_unknown_complex_equation(self) : 
        eq = self.__get_eq("5x+5-10*5/10=30")
        
        eq.resolve()

        self.assertEqual(13, eq.unknown_value)


    def test_solve_unknown_complex_relative_equation(self) : 
        eq = self.__get_eq("5x+-5-10*5/-10=30")
        
        eq.resolve()

        self.assertEqual(-9, eq.unknown_value)

    
    def __get_eq(self, text) :
        analyze = Analyze(text)
        rewrite = Rewrite()
        eq = Equation(text, analyze, rewrite)
        return eq