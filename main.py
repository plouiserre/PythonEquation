from analyze import Analyze
from rewrite import Rewrite
from equation import Equation


print("Which equation do you want resolve?")
text_equation = input()
analyze = Analyze(text_equation)
rewrite = Rewrite()
eq = Equation(text_equation, analyze, rewrite)

isValidate = analyze.is_validate()
if isValidate :
    print("Equation is validate\n")
    eq.resolve()
    print("Solution is %f" %eq.unknown_value)
else :
    print("Equation is not validate\n")
    print("Program is down.")
