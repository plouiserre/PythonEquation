import unittest
from analyze import Analyze
from rewrite import Rewrite
from solve import Solve

class SolveTest(unittest.TestCase) :
    def test_no_solve_if_False(self) : 
        text = "x+8 = 10"
        solve = self.__get_solve(text, ["x=10-8"], "-", False)

        result = solve.solve()

        self.assertEqual(0, result)

    def test_solve_add_equation(self) : 
        text = "x+8 = 10"
        solve = self.__get_solve(text, ["x=10-8"], "-", True)

        result = solve.solve()

        self.assertEqual(2, result)


    def test_solve_substract_equation(self) : 
        text = "x-8=10"
        solve = self.__get_solve(text, ["x=10+8"], "+", True)

        result = solve.solve()

        self.assertEqual(18, result)


    def test_solve_multiply_simple_equation(self) : 
        text="42x=84"
        solve = self.__get_solve(text, ["x=84/42"], "/", True)

        result = solve.solve()

        self.assertEqual(2, result)
        

    def test_solve_multiply_medium_equation(self) : 
        text = "x*8 = 80"
        solve = self.__get_solve(text, ["x=80/8"], "/", True)

        result = solve.solve()

        self.assertEqual(10, result)


    def test_solve_divide_equation(self) : 
        text = "x/8=10"
        solve = self.__get_solve(text, ["x=10*8"], "*", True)

        result = solve.solve()

        self.assertEqual(80, result)


    def test_do_the_math_addition(self) :
        solve = self.__get_solve("", "]", "", True)

        result = solve.do_the_math(3,5,'+')

        self.assertEqual(8, result)


    def test_do_the_math_soustraction(self) :
        solve = self.__get_solve("", "]", "", True)

        result = solve.do_the_math(3,5,'-')

        self.assertEqual(-2, result)


    def test_do_the_math_multiplication(self) :
        solve = self.__get_solve("", "]", "", True)

        result = solve.do_the_math(3,5,'*')

        self.assertEqual(15, result)


    def test_do_the_math_division(self) :
        solve = self.__get_solve("", "]", "", True)

        result = solve.do_the_math(5,2,'/')

        self.assertEqual(2.5, result)

    
    def test_do_the_math_multiplication_negatif(self) :
        solve = self.__get_solve("", "]", "", True)

        result = solve.do_the_math(3,-5,'*')

        self.assertEqual(-15, result)


    def test_do_the_math_division_negatif(self) :
        solve = self.__get_solve("", "]", "", True)

        result = solve.do_the_math(5,-2,'*')

        self.assertEqual(-10, result)

    
    def __get_solve(self, text, rewrite_eq, new_sign, is_eq_can_be_solved) :
        analyze = Analyze(text)
        rewrite = Rewrite()
        rewrite.equation_can_be_solved = is_eq_can_be_solved
        rewrite.new_sign = new_sign
        solve = Solve(rewrite, analyze, rewrite_eq)
        return solve

