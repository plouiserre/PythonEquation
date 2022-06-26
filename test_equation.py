import unittest
from analyze import Analyze
from equation import Equation

class EquationTest(unittest.TestCase) :

    def test_is_validate_equation(self) : 
        eq = self.__get_eq("x-977=78")

        eq.process_resolve()

        self.assertTrue(eq.is_validate)

    def test_is_no_validate_equation(self) : 
        eq = self.__get_eq("x/*977=78")

        eq.process_resolve()

        self.assertFalse(eq.is_validate)


    #TODO redites avec la partie analyze donc il faut déplacer dans analyze ou supprimer
    '''def test_get_numbers_small_equation(self) :
        equation = Equation("x-977=78")

        equation.process_resolve()

        self.assertEqual("977", equation.numbers[0])
        self.assertEqual("78", equation.numbers[1])'''

    
    '''def test_get_numbers_medium_equation(self) :
        equation = Equation("3x+3=15")

        equation.process_resolve()

        self.assertEqual("3", equation.numbers[0])
        self.assertEqual("3", equation.numbers[1])
        self.assertEqual("15", equation.numbers[2])'''


    def test_rewrite_add_equation(self) : 
        eq = self.__get_eq("x+5=7")

        eq.process_resolve()

        self.assertEqual("x=7-5", eq.rewrite_eq[0])
        self.assertTrue(eq.equation_can_be_solved)


    def test_rewrite_substract_equation(self) : 
        eq = self.__get_eq("x-5=7")
        
        eq.process_resolve()

        self.assertEqual("x=7+5", eq.rewrite_eq[0])
        self.assertTrue(eq.equation_can_be_solved)


    def test_rewrite_multiply_equation(self) : 
        eq = self.__get_eq("x*5=7")
        
        eq.process_resolve()

        self.assertEqual("x=7/5", eq.rewrite_eq[0])
        self.assertTrue(eq.equation_can_be_solved)


    def test_rewrite_multiply_express_equation(self) : 
        eq = self.__get_eq("42x=84")
        
        eq.process_resolve()

        self.assertEqual("x=84/42", eq.rewrite_eq[0])
        self.assertTrue(eq.equation_can_be_solved)


    def test_rewrite_divide_equation(self) : 
        eq = self.__get_eq("x/5=7")
        
        eq.process_resolve()

        self.assertEqual("x=7*5", eq.rewrite_eq[0])
        self.assertTrue(eq.equation_can_be_solved)


    def test_rewrite_unknown_numbers_all_rewrite_equation(self) : 
        eq = self.__get_eq("3x+3=15")
        
        eq.process_resolve()

        self.assertEqual("3x=15-3", eq.rewrite_eq[0])
        self.assertEqual("x=12/3", eq.rewrite_eq[1])
        self.assertTrue(eq.equation_can_be_solved)


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
        eq = Equation(text, analyze)
        return eq