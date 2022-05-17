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
        #TODO ici il faut améliorer le code
        print("Number of sign_numbers in this part %d of the equation " % len(part.signs_numbers))
        for sign_number in part.signs_numbers : 
            print("Sign Number group %s " %sign_number.text)
            print("priority %d "%sign_number.priority)
            print("position %d "%sign_number.position)
            print("order %d "%sign_number.order)
else :
    print("Equation is not validate\n")
    print("Program is down.")
