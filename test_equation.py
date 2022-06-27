import unittest
from analyze import Analyze
from equation import Equation
from rewrite import Rewrite

#TODO à la fin faire des unit test pour vérifier les appels et pour tout tester
class EquationTest(unittest.TestCase) :

    def test_is_validate_equation(self) : 
        eq = self.__get_eq("x-977=78")

        eq.process_resolve()

        self.assertTrue(eq.is_validate)

    def test_is_no_validate_equation(self) : 
        eq = self.__get_eq("x/*977=78")

        eq.process_resolve()

        self.assertFalse(eq.is_validate)


    def test_eq_rewrite_small_eq(self) : 
        eq = self.__get_eq("x+5=7")

        eq.process_resolve()

        self.assertEqual(1, len(eq.rewrite_eq))
        self.assertEqual("x=7-5", eq.rewrite_eq[0])


    def test_eq_rewrite_medium_eq(self) : 
        eq = self.__get_eq("3x+3=15")

        eq.process_resolve()

        self.assertEqual(2, len(eq.rewrite_eq))
        self.assertEqual("3x=15-3", eq.rewrite_eq[0])
        self.assertEqual("x=12/3", eq.rewrite_eq[1])
    

    def test_solve_add_equation(self) : 
        eq = self.__get_eq("x+5=7")
        
        eq.process_resolve()

        self.assertEqual(2, eq.unknown_value)


    def test_solve_substract_equation(self) : 
        eq = self.__get_eq("x-5=7")
        
        eq.process_resolve()

        self.assertEqual(12, eq.unknown_value)
        

    def test_solve_multiply_equation_simple(self) : 
        eq = self.__get_eq("42x=84")
        
        eq.process_resolve()

        self.assertEqual(2, eq.unknown_value)


    def test_solve_multiply_equation_medium(self) : 
        eq = self.__get_eq("x*5=7")
        
        eq.process_resolve()

        self.assertEqual(1.4, eq.unknown_value)


    def test_solve_divide_equation(self) : 
        eq = self.__get_eq("x/5=7")
        
        eq.process_resolve()

        self.assertEqual(35, eq.unknown_value)


    def test_solve_unknown_numbers_all_rewrite_equation(self) : 
        eq = self.__get_eq("3x+3=15")
        
        eq.process_resolve()

        self.assertEqual(4, eq.unknown_value)

    
    def __get_eq(self, text) :
        analyze = Analyze(text)
        rewrite = Rewrite(analyze)
        eq = Equation(text, analyze, rewrite)
        return eq