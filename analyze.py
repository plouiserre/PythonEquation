class Analyze : 
    def __init__(self, equation) :
        self.Equation = equation


    def is_validate(self) :
        is_ok = True
        is_equal_sign_ok = False
        for index, element in enumerate(self.Equation) : 
            isAlpha = element.isalpha()
            if isAlpha  and element != 'x' :
                is_ok = False
            elif self.__validate_multiplication_division(element, index):
                is_ok = False
            elif self.__validate_equal(element,index) :
                is_equal_sign_ok = True

        if is_ok and is_equal_sign_ok == False :
            is_ok = False 
        elif is_ok and self.__validate_unknown() == False :
            is_ok = False

        return is_ok
        

    def __validate_multiplication_division(self, element, index) :
        is_signs_are_ko = False
        last_element = self.Equation[index - 1]
        if index > 0 :
            if (element == '/' and last_element == '*') or (element == '*' and last_element == '/') : 
                is_signs_are_ko = True
            elif (element == '/' or element=='*') and (last_element == '-' or last_element == '+') :
                is_signs_are_ko = True
        elif index == 0 and (element == '/' or element == '*') : 
                is_signs_are_ko = True
        
        return is_signs_are_ko


    def __validate_equal(self, element, index) : 
        is_equal_sign_ok = False 
        if element == '=' and index > 0 and index < len(self.Equation) - 1 :
            last_element = self.Equation[index - 1]
            if last_element != '+' and last_element != '-' and last_element != '*' and last_element != '/' :
                is_equal_sign_ok = True
        return is_equal_sign_ok
        

    def __validate_unknown(self) : 
        parts = self.Equation.split("=")
        is_unknow_in_left_part = False

        for element in parts[0] :
            if element == 'x' : 
                is_unknow_in_left_part = True

        return is_unknow_in_left_part