import unittest
from analyze import Analyze

from solve import Solve

class SolveTest(unittest.TestCase) :

    '''def test_solve_add_equation(self) : 
        equation_text = "x+8 = 10"
        analyze = Analyze(equation_text)
        solve = Solve(analyze)

        solve.resolve()

        self.assertEqual(2, solve.unknow)


    def test_solve_substract_equation(self) : 
        equation_text = "x-8=10"
        analyze = Analyze(equation_text)
        solve = Solve(analyze)

        solve.resolve()

        self.assertEqual(18, solve.unknow)


    def test_solve_multiply_simple_equation(self) : 
        equation_text="42x=84"
        analyze = Analyze(equation_text)
        solve = Solve(analyze)

        solve.resolve()

        self.assertEqual(2, solve.unknow)
        

    def test_solve_multiply_medium_equation(self) : 
        equation_text = "x*8 = 80"
        analyze = Analyze(equation_text)
        solve = Solve(analyze)

        solve.resolve()

        self.assertEqual(10, solve.unknow)


    def test_solve_divide_equation(self) : 
        equation_text = "x/8=10"
        analyze = Analyze(equation_text)
        solve = Solve(analyze)

        solve.resolve()

        self.assertEqual(80, solve.unknow)

    
    def test_solve_add_equation_relatif(self) : 
        equation_text = "x+-8 = 10"
        analyze = Analyze(equation_text)
        solve = Solve(analyze)

        solve.resolve()

        self.assertEqual(18, solve.unknow)


    def test_solve_substract_equation_relatif(self) : 
        equation_text = "x--8=10"
        analyze = Analyze(equation_text)
        solve = Solve(analyze)

        solve.resolve()

        self.assertEqual(2, solve.unknow)


    def test_solve_multiply_equation_relatif(self) : 
        equation_text = "x*-8 = 80"
        analyze = Analyze(equation_text)
        solve = Solve(analyze)

        solve.resolve()

        self.assertEqual(-10, solve.unknow)


    def test_solve_divide_equation_relatif(self) : 
        equation_text = "x/-8=10"
        analyze = Analyze(equation_text)
        solve = Solve(analyze)

        solve.resolve()

        self.assertEqual(-80, solve.unknow)'''

