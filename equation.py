import numbers
from part import Part

class Equation : 
    def __init__(self, text) : 
        self.text = text
        self.numbers = []
        self.parts = []
        self.unknown_value = 0
        self.equation_can_be_solved = False
        self.new_sign =''


    def set_numbers(self, numbers) : 
        self.numbers = numbers


    def get_parts(self) : 
        parts = self.text.split("=")
        for part in parts :
            find_part = Part(part)
            self.parts.append(find_part)


    def rewrite(self, signs) : 
        number = self.numbers[0]
        all_signs = ''.join(signs)
        element_to_delete = all_signs + number
        self.text = self.text.replace(element_to_delete,'')
        self.new_sign = self.__construct_new_sign(signs)
        self.text = self.text+self.new_sign+number
        self.equation_can_be_solved = True

    
    def __construct_new_sign(self, signs) :
        new_sign = ''
        signs_simplified = self.__get_signs_simplified(signs)
        if len(signs_simplified) > 1 : 
            new_sign = self.__get_new_signs_for_complexs(signs)
        elif signs_simplified != '' :
            new_sign = self.__get_new_sign(signs_simplified)
        else :
            for sign in signs :
                new_sign += self.__get_new_sign(sign)
        return new_sign


    def __get_signs_simplified(self, signs) :
        signs_to_simplified = ''.join(signs)
        if signs_to_simplified == '--' or signs_to_simplified =='++':
            signs_simplified = '+'
        elif signs_to_simplified == '+-' or signs_to_simplified == '-+' or signs_to_simplified == '-' :
            signs_simplified = '-'
        elif self.new_sign == '*+' :
            signs_simplified = '*'
        elif self.new_sign == '/+' :
            signs_simplified = '/'
        else :
            signs_simplified = signs_to_simplified
        return signs_simplified


    def __get_new_signs_for_complexs (self, signs) :
        signs_to_simplified = ''.join(signs)
        if signs_to_simplified == '*-' :
            signs_simplified = "/-"
        elif signs_to_simplified == '/-' :
            signs_simplified = "*-"
        else :
            signs_simplified = ''
        return signs_simplified


    def __get_new_sign(self, sign) :
        new_sign = ''
        if sign == '+' :
            new_sign += '-'
        elif sign == '-' : 
            new_sign += '+'
        elif sign == '*' : 
            new_sign += '/'
        elif sign == '/' : 
            new_sign += '*'
        return new_sign


    def solve(self) : 
        if self.equation_can_be_solved : 
            first_number = int(self.numbers[1])
            second_number = int(self.numbers[0])

            if self.new_sign == '-' :
                self.unknown_value = first_number - second_number
            elif self.new_sign == '+' :
                self.unknown_value = first_number + second_number
            elif self.new_sign == '/' :
                self.unknown_value = first_number / second_number
            elif self.new_sign == '/-' :
                self.unknown_value = first_number / - second_number
            elif self.new_sign == '*' :
                self.unknown_value = first_number * second_number
            elif self.new_sign == '*-' :
                self.unknown_value = first_number * - second_number
