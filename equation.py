import numbers
from part import Part

#TODO factoriser une partie avec le code de analyze.py
class Equation : 
    def __init__(self, text) : 
        self.text = text
        self.parts = []
        self.unknown_value = 0
        self.equation_can_be_solved = False
        self.new_sign =''


    def get_parts(self) : 
        parts = self.text.split("=")
        for part in parts :
            find_part = Part(part)
            self.parts.append(find_part)


    def rewrite(self, signs) : 
        index = self.__get_start_index(signs)
        rest_equation = self.text[index + 1 : len(self.text)]
        number = ""
        for element in rest_equation : 
            if element != '=' and element != '-': 
                    number += element
            elif  element == '-'  :
                continue
            else:
                break
        all_signs = ''.join(signs)
        element_to_delete = all_signs + number
        self.text = self.text.replace(element_to_delete,'')
        self.new_sign = self.__construct_new_sign(signs)
        self.text= self.__get_new_text(number)
        self.equation_can_be_solved = True

    
    def __construct_new_sign(self, signs) :
        new_sign = ''
        #TODO retravailler cette partie
        signs_simplified = self.__get_signs(signs)
        if len(signs_simplified) > 1 : 
            new_sign = signs_simplified
        elif signs_simplified != '' :
            new_sign = self.__get_new_sign(signs_simplified)
        else :
            for sign in signs :
                new_sign += self.__get_new_sign(sign)
        return new_sign


    def __get_signs(self, signs) :
        all_signs = ''.join(signs)
        if all_signs == '--' or all_signs =='++':
            all_signs = '+'
        elif all_signs == '+-' or all_signs == '-+' or all_signs == '-' :
            all_signs = '-'
        elif all_signs == '*-' :
            all_signs = "/-"
        elif all_signs == '/-' :
            all_signs = "*-"
        else :
            all_signs = ''
        return all_signs


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


    #TODO reprendre cette partie là
    def __get_new_text(self, number) :
        text = ''
        if len(self.new_sign) == 1 :
            text = self.text+self.new_sign+number
        else : 
            sign_simplified = ''
            if self.new_sign == '*+' :
                sign_simplified = '*'
            elif self.new_sign == '/+' :
                sign_simplified = '/'
            else :
                sign_simplified = self.new_sign
            text = self.text+sign_simplified+number
        return text


    def __get_start_index(self, signs) : 
        index = 0
        sign = signs[0]
        if sign in self.text :
            index = self.text.index(sign)
        else : 
            self.text = self.text.replace('--','+')
            index = self.text.index(sign)
        return index


    #TODO à améliorer
    def solve(self) : 
        if self.equation_can_be_solved : 
            resolve_space = self.text.split('=')[1]

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
