import re 
import copy

from part import Part

class Analyze : 

    def __init__(self, text) : 
        self.text = text
        self.parts = []
        self.numbers = []
        self.all_signs = []
        self.signs = []
        
        
    def get_parts(self) : 
        parts = self.text.split("=")
        for part in parts :
            find_part = Part(part)
            self.parts.append(find_part)


    def get_index_signs(self, sign, times) :
        index = 0
        index_end = 0 
        occurency = 1
        while index < len(self.text) :
            len_sign = len(sign)
            index_end = index + len_sign 
            caracter = self.text[index : index_end]
            if caracter == sign and times == occurency : 
                break
            elif caracter == sign and times != occurency : 
                occurency += 1
            index += 1
        return index
        
    
    def determine_all_elements(self, text) : 
        self.text = text
        self.is_next_sign_detected = False
        self.number = ''
        self.numbers_building = []
        self.is_before_equal = True
        self.is_number_finished = False
        self.numbers.clear()
        self.all_signs.clear()
        self.signs.clear()
        for i in range (0,len(text)) : 
            element = text[i]
            if element == '=' :
                self.is_before_equal = False
            if self.is_numeral(element) :
                self.__manage_numbers(i, element)
            elif element == 'x' or self.is_next_sign_detected:
                self.is_next_sign_detected = False
                continue
            elif self.is_numeral(element) == False and element != '='  :                  
                self.__manage_signs(element, i)
        for i in  range (0, len(self.numbers_building)) :
            self.numbers.append(self.numbers_building[i])


    def __manage_numbers(self, i, element) : 
                is_number_finished = False
                self.number = self.number + element
                if i + 1 >= len(self.text) :
                    is_number_finished = True
                if i + 1 < len(self.text) and self.is_numeral(self.text[i+1]) == False:
                    is_number_finished = True
                if is_number_finished :
                    self.numbers_building.append(self.number)
                    self.number = ''


    def __manage_signs(self,element, i) : 
        if i + 1 < len(self.text) and self.is_numeral(self.text[i+1]) == False: 
            complex_sign = element + self.text[i+1]
            self.all_signs.append(complex_sign)
            if self.is_before_equal :
                self.signs.append(complex_sign)
            self.is_next_sign_detected = True
        else :
            self.all_signs.append(element)
            if self.is_before_equal :
                self.signs.append(element)  


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