import re 
import copy

from part import Part

class Analyze : 

    def __init__(self, text) : 
        self.text = text
        self.parts = []
        self.numbers = []
        self.signs = []
        
    def get_parts(self) : 
        parts = self.text.split("=")
        for part in parts :
            find_part = Part(part)
            self.parts.append(find_part)


    def get_index_signs(self, sign) :
        index = 0
        index_end = 0 
        while index < len(self.text) :
            len_sign = len(sign)
            index_end = index + len_sign 
            caracter = self.text[index : index_end]
            if caracter == sign : 
                break
            index += 1
        return index
        
    
    #TODO simplifier cette méthode
    def determine_all_elements(self, text) : 
        self.text = text
        is_next_sign_detected = False
        number = ''
        numbers = []
        index = 0
        self.numbers.clear()
        self.signs.clear()
        for i in range (0,len(text)) : 
            element = text[i]
            if self.is_numeral(element) :
                if len(numbers) == index :
                    number = element
                    numbers.append(number)
                else :  
                    number = number + element
                    numbers[index] = number
            elif element == 'x' or is_next_sign_detected:
                is_next_sign_detected = False
                continue
            elif self.is_numeral(element) == False :  
                if element != '=' : 
                    if i + 1 < len(text) and self.is_numeral(text[i+1]) == False: 
                        complex_sign = element + text[i+1]
                        self.signs.append(complex_sign)
                        is_next_sign_detected = True
                    else :
                        self.signs.append(element)
                if number != '':
                    index += 1
        for i in  range (0, len(numbers)) :
            self.numbers.append(numbers[i])


    def is_numeral(self, element) :
        if element != '+' and element != '-' and element != '*' and element != '/' and element != '=' and element != 'x' and element != ' ':
            return True 
        else :
            return False


    def is_validate(self) :
        is_ok = True
        is_equal_sign_ok = False
        equation_text= self.text
        for index, element in enumerate(equation_text) : 
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
        last_element = self.text[index - 1]
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
        equation_text= self.text
        if element == '=' and index > 0 and index < len(equation_text) - 1 :
            last_element = equation_text[index - 1]
            if last_element != '+' and last_element != '-' and last_element != '*' and last_element != '/' :
                is_equal_sign_ok = True
        return is_equal_sign_ok
        

    def __validate_unknown(self) : 
        if len(self.parts) == 0 :
            self.get_parts()
        
        is_unknow_in_left_part = False

        for element in self.parts[0].text :
            if element == 'x' : 
                is_unknow_in_left_part = True

        return is_unknow_in_left_part