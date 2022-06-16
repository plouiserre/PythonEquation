import unittest
from equation import Equation

class EquationTest(unittest.TestCase) :

    def test_find_parts(self) :
        equation = Equation("87x+765-7653=987")
        
        equation.get_parts()

        self.assertEqual(2, len(equation.parts))
        self.assertEqual("87x+765-7653", equation.parts[0].text)
        self.assertEqual("987", equation.parts[1].text)


    def test_set_numbers(self) :
        equation = Equation("x-977=78")

        equation.set_numbers(["977", "78"])

        self.assertEqual("977", equation.numbers[0])
        self.assertEqual("78", equation.numbers[1])


    def test_rewrite_add_equation(self) : 
        eq = Equation("x+5=7")

        eq.set_numbers(["5"])
        eq.rewrite("+")

        self.assertEqual("x=7-5", eq.text)
        self.assertTrue(eq.equation_can_be_solved)


    def test_rewrite_substract_equation(self) : 
        eq = Equation("x-5=7")

        eq.set_numbers(["5"])
        eq.rewrite("-")

        self.assertEqual("x=7+5", eq.text)
        self.assertTrue(eq.equation_can_be_solved)


    def test_rewrite_multiply_equation(self) : 
        eq = Equation("x*5=7")

        eq.set_numbers(["5"])
        eq.rewrite("*")

        self.assertEqual("x=7/5", eq.text)
        self.assertTrue(eq.equation_can_be_solved)


    def test_rewrite_multiply_express_equation(self) : 
        eq = Equation("42x=84")

        eq.set_numbers(["42"])
        eq.rewrite("")

        self.assertEqual("x=84/42", eq.text)
        self.assertTrue(eq.equation_can_be_solved)


    def test_rewrite_divide_equation(self) : 
        eq = Equation("x/5=7")

        eq.set_numbers(["5"])
        eq.rewrite("/")

        self.assertEqual("x=7*5", eq.text)
        self.assertTrue(eq.equation_can_be_solved)


    def test_solve_add_equation(self) : 
        eq = Equation("x+5=7")

        eq.set_numbers(["5","7"])
        eq.rewrite("+")
        eq.solve()

        self.assertEqual(2, eq.unknown_value)


    def test_solve_substract_equation(self) : 
        eq = Equation("x-5=7")

        eq.set_numbers(["5","7"])
        eq.rewrite("-")
        eq.solve()

        self.assertEqual(12, eq.unknown_value)
        

    def test_solve_multiply_equation_simple(self) : 
        eq = Equation("42x=84")

        eq.set_numbers(["42","84"])
        eq.rewrite("")
        eq.solve()

        self.assertEqual(2, eq.unknown_value)


    def test_solve_multiply_equation_medium(self) : 
        eq = Equation("x*5=7")

        eq.set_numbers(["5","7"])
        eq.rewrite("*")
        eq.solve()

        self.assertEqual(1.4, eq.unknown_value)


    def test_solve_divide_equation(self) : 
        eq = Equation("x/5=7")

        eq.set_numbers(["5","7"])
        eq.rewrite("/")
        eq.solve()

        self.assertEqual(35, eq.unknown_value)