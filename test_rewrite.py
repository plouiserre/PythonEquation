import unittest
from analyze import Analyze

from rewrite import Rewrite

#TODO il faudra mocker pour les nombres donc la je vais juste faire un analyze des nombres
class RewriteTest(unittest.TestCase) :
    def test_rewrite_add_equation(self) : 
        rewrite = self.__get_rewrite("x+5=7")

        rewrite.rewrite()

        self.assertEqual("x=7-5", rewrite.rewrite_eq)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_substract_equation(self) : 
        rewrite = self.__get_rewrite("x-5=7")
        
        rewrite.rewrite()

        self.assertEqual("x=7+5", rewrite.rewrite_eq)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_multiply_equation(self) : 
        rewrite = self.__get_rewrite("x*5=7")
        
        rewrite.rewrite()

        self.assertEqual("x=7/5", rewrite.rewrite_eq)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_multiply_express_equation(self) : 
        rewrite = self.__get_rewrite("42x=84")
        
        rewrite.rewrite()

        self.assertEqual("x=84/42", rewrite.rewrite_eq)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_divide_equation(self) : 
        rewrite = self.__get_rewrite("x/5=7")
        
        rewrite.rewrite()

        self.assertEqual("x=7*5", rewrite.rewrite_eq)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_unknown_numbers_all_rewrite_equation(self) : 
        rewrite = self.__get_rewrite("3x+3=15")
        
        rewrite.rewrite()

        self.assertEqual("3x=15-3", rewrite.rewrite_eq)
        self.assertFalse(rewrite.equation_can_be_solved)

        
    def test_simplify_eq(self) :
        rewrite = self.__get_rewrite("3x+3=15")

        text = rewrite.simplify("3x=15-3")

        self.assertEqual("3x=12", text)


    def __get_rewrite(self, text) :
        analyze = Analyze(text)
        analyze.determine_all_elements(text)
        rewrite = Rewrite(analyze)
        return rewrite