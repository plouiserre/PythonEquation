from analyze import Analyze


print("Which equation do you want resolve?")
equation = input()
input = Analyze(equation)
isValidate = input.IsValidate()
if isValidate :
    print("Equation is validate")
else :
    print("Equation is not validate")