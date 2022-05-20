from part import Part

#TODO factoriser une partie avec le code de analyze.py
class Equation : 
    def __init__(self, text) : 
        self.text = text
        self.parts = []
        self.unknown_value = 0
        self.equation_can_be_solved = False


    def get_parts(self) : 
        parts = self.text.split("=")
        for part in parts :
            find_part = Part(part)
            self.parts.append(find_part)


    def rewrite(self, sign) : 
        index = self.text.index(sign)
        rest_equation = self.text[index + 1 : len(self.text)]
        number = ""
        for element in rest_equation : 
            if element != '+' and element != '-' and element != '*' and element != '/' and element != '=' : 
                number += element
            else :
                break
        element_to_delete = sign + number
        self.text = self.text.replace(element_to_delete,'')
        new_sign = ''
        if sign == '+' :
            new_sign = '-'
        elif sign == '-' : 
            new_sign = '+'
        elif sign == '*' : 
            new_sign = '/'
        elif sign == '/' : 
            new_sign = '*'
        self.text = self.text+new_sign+number
        self.equation_can_be_solved = True


    #TODO à améliorer
    def solve(self) : 
        if self.equation_can_be_solved : 
            resolve_space = self.text.split('=')[1]

            sign = ''
            first_number_str = '' 
            second_number_str = ''
            is_first_number_finished = False

            for element in resolve_space : 
                if is_first_number_finished == False and element != '-' and element != '+' and element != '/' and element != '*':
                    first_number_str += element 
                elif element == '-' or element == '+' or element == '/' or element == '*': 
                    sign = element
                    is_first_number_finished = True 
                else : 
                    second_number_str += element

            first_number = int(first_number_str)
            second_number = int(second_number_str)

            if sign == '-' :
                self.unknown_value = first_number - second_number
            elif sign == '+' :
                self.unknown_value = first_number + second_number
            elif sign == '/' :
                self.unknown_value = first_number / second_number
            elif sign == '*' :
                self.unknown_value = first_number * second_number
