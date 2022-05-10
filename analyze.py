class Analyze : 
    def __init__(self, equation) :
        self.Equation = equation


    def IsValidate(self) :
        isOk = True
        isEqualSignOk = False
        for index, element in enumerate(self.Equation) : 
            isAlpha = element.isalpha()
            if isAlpha  and element != 'x' :
                isOk = False
            elif index > 0 and ((element == '/' and self.Equation[index - 1] == '*') or (element == '*' and self.Equation[index - 1] == '/')):
                isOk = False
            elif self.EqualSignIsValidate(element,index) :
                isEqualSignOk = True

        if isOk and isEqualSignOk == False :
            isOk = False 
        elif isOk and self.UnknowInLeftPart() == False :
            isOk = False

        return isOk


    def EqualSignIsValidate(self, element, index) : 
        isEqualSignOk = False 
        if element == '=' and index > 0 and index < len(self.Equation) - 1 :
            lastElement = self.Equation[index - 1]
            if lastElement != '+' and lastElement != '-' and lastElement != '*' and lastElement != '/' :
                isEqualSignOk = True
        return isEqualSignOk
        

    def UnknowInLeftPart(self) : 
        parts = self.Equation.split("=")
        IsUnknowInLeftPart = False

        for element in parts[0] :
            if element == 'x' : 
                IsUnknowInLeftPart = True

        return IsUnknowInLeftPart