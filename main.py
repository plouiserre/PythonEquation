from analyze import Analyze


print("Which equation do you want resolve?")
equation = input()
input = Analyze(equation)
isValidate = input.is_validate()
if isValidate :
    print("Equation is validate")
else :
    print("Equation is not validate")