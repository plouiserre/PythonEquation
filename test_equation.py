import unittest
from equation import Equation

class EquationTest(unittest.TestCase) :

    def test_find_parts(self) :
        equation = Equation("87x+765-7653=987")
        
        equation.get_parts()

        self.assertEqual(2, len(equation.parts))
        self.assertEqual("87x+765-7653", equation.parts[0].text)
        self.assertEqual("987", equation.parts[1].text)