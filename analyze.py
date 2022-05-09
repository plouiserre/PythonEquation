class Analyze : 
    def __init__(self, equation) :
        self.Equation = equation


    def IsValidate(self) :
        isOk = True
        for element in self.Equation : 
            isAlpha = element.isalpha()
            if isAlpha  and element != 'x' :
                isOk = False
        return isOk