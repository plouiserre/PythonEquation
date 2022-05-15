from analyze import Analyze


print("Which equation do you want resolve?")
equation = input()
input = Analyze(equation)
isValidate = input.is_validate()
if isValidate :
    print("Equation is validate\n")
    input.identification()
    for part in input.equation.parts : 
        print("Text of part %s of the equation " % part.text)
        print("Group of part %s of the equation " % part.signs_numbers)
    

else :
    print("Equation is not validate\n")
    print("Program is down.")
