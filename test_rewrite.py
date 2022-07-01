import unittest
from analyze import Analyze

from rewrite import Rewrite

#TODO il faudra mocker pour les nombres donc la je vais juste faire un analyze des nombres
class RewriteTest(unittest.TestCase) :
    def test_rewrite_add_equation(self) : 
        rewrite = Rewrite()
        
        analyze = self.__get_analyze("x+5=7")
        rewrite.rewrite(analyze)

        self.assertEqual("x=7-5", rewrite.step)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_substract_equation(self) : 
        rewrite = Rewrite()

        analyze = self.__get_analyze("x-5=7")
        rewrite.rewrite(analyze)

        self.assertEqual("x=7+5", rewrite.step)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_multiply_equation(self) : 
        rewrite = Rewrite()

        analyze = self.__get_analyze("x*5=7")
        rewrite.rewrite(analyze)

        self.assertEqual("x=7/5", rewrite.step)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_multiply_express_equation(self) : 
        rewrite = Rewrite()

        analyze = self.__get_analyze("42x=84")
        rewrite.rewrite(analyze)

        self.assertEqual("x=84/42", rewrite.step)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_divide_equation(self) : 
        rewrite = Rewrite()

        analyze = self.__get_analyze("x/5=7")
        rewrite.rewrite(analyze)

        self.assertEqual("x=7*5", rewrite.step)
        self.assertTrue(rewrite.equation_can_be_solved)


    def test_rewrite_unknown_numbers_all_rewrite_equation(self) : 
        rewrite = Rewrite()

        analyze = self.__get_analyze("3x+3=15")
        rewrite.rewrite(analyze)

        self.assertEqual("3x=15-3", rewrite.step)
        self.assertFalse(rewrite.equation_can_be_solved)

        
    def test_simplify_eq(self) :
        rewrite = Rewrite()
        rewrite.analyze = self.__get_analyze("3x=15-3")

        text = rewrite.simplify("3x=15-3")

        self.assertEqual("3x=12.0", text)


    def __get_analyze(self, text) :
        analyze = Analyze(text)
        analyze.determine_all_elements(text)
        return analyze