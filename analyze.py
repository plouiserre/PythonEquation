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
            elif self.MultiplicationDivisionSignsArentValidates(element, index):
                isOk = False
            elif self.EqualSignIsValidate(element,index) :
                isEqualSignOk = True

        if isOk and isEqualSignOk == False :
            isOk = False 
        elif isOk and self.UnknowInLeftPart() == False :
            isOk = False

        return isOk
        

    def MultiplicationDivisionSignsArentValidates(self, element, index) :
        isSignsAreKo = False
        lastElement = self.Equation[index - 1]
        if index > 0 :
            if (element == '/' and lastElement == '*') or (element == '*' and lastElement == '/') : 
                isSignsAreKo = True
            elif (element == '/' or element=='*') and (lastElement == '-' or lastElement == '+') :
                isSignsAreKo = True
        elif index == 0 and (element == '/' or element == '*') : 
                isSignsAreKo = True
        
        return isSignsAreKo


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