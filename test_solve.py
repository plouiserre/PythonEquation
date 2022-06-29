import unittest
from analyze import Analyze
from rewrite import Rewrite
from solve import Solve

class SolveTest(unittest.TestCase) :

    def test_solve_add_equation(self) : 
        text = "x+8 = 10"
        solve = self.__get_solve(text, ["x=10-8"], "-")

        result = solve.solve()

        self.assertEqual(2, result)


    def test_solve_substract_equation(self) : 
        text = "x-8=10"
        solve = self.__get_solve(text, ["x=10+8"], "+")

        result = solve.solve()

        self.assertEqual(18, result)


    def test_solve_multiply_simple_equation(self) : 
        text="42x=84"
        solve = self.__get_solve(text, ["x=84/42"], "/")

        result = solve.solve()

        self.assertEqual(2, result)
        

    def test_solve_multiply_medium_equation(self) : 
        text = "x*8 = 80"
        solve = self.__get_solve(text, ["x=80/8"], "/")

        result = solve.solve()

        self.assertEqual(10, result)


    def test_solve_divide_equation(self) : 
        text = "x/8=10"
        solve = self.__get_solve(text, ["x=10*8"], "*")

        result = solve.solve()

        self.assertEqual(80, result)

    
    def __get_solve(self, text, rewrite_eq, new_sign) :
        analyze = Analyze(text)
        rewrite = Rewrite()
        rewrite.equation_can_be_solved = True
        rewrite.new_sign = new_sign
        solve = Solve(rewrite, analyze, rewrite_eq)
        return solve

