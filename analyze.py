import re 
import copy

from equation import Equation
from signnumber import SignNumber

class Analyze : 
    def __init__(self, equation) :
        self.equation = Equation(equation)
        self.parts = []
        self.numbers = []


    def is_validate(self) :
        is_ok = True
        is_equal_sign_ok = False
        equation_text= self.equation.text
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
        last_element = self.equation.text[index - 1]
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
        equation_text= self.equation.text
        if element == '=' and index > 0 and index < len(equation_text) - 1 :
            last_element = equation_text[index - 1]
            if last_element != '+' and last_element != '-' and last_element != '*' and last_element != '/' :
                is_equal_sign_ok = True
        return is_equal_sign_ok
        

    def __validate_unknown(self) : 
        if len(self.parts) == 0 :
            self.equation.get_parts()
        
        is_unknow_in_left_part = False

        for element in self.equation.parts[0].text :
            if element == 'x' : 
                is_unknow_in_left_part = True

        return is_unknow_in_left_part


    def identicate(self) :
        self.__get_numbers()

        self.__concatene_numbers_signs()


    def __get_numbers(self) : 
        number = ''
        for element in self.equation.text :
            if element == '':
                continue
            elif self.__is_numeral(element):
                number += element   
            elif element == '=' and number != '':  
                self.numbers.append(number)  
                number = ''
            elif element != '' and element != '' and element != ' ' and number != '': 
                self.numbers.append(number)  
                number = ''
        if number != '' :
            self.numbers.append(number)
            number = ''
            

    
    def __is_numeral(self, element) :
        if element != '+' and element != '-' and element != '*' and element != '/' and element != '=' and element != 'x' and element != ' ':
            return True 
        else :
            return False


    def __concatene_numbers_signs(self) :
        if len(self.numbers) > 2 :
            self.__get_signs_numbers_large_equation()
        else : 
            self.__get_signs_numbers_small_equation()
        self.__determine_order_sign_number(self.equation.parts[0].signs_numbers)


    def __get_signs_numbers_large_equation(self) : 
        save_indexs = {}
        left_numbers = copy.copy(self.numbers)
        left_numbers.pop()
        self.__get_signs_numbers_unknown(self.equation.text)
        for index, _ in enumerate(left_numbers) : 
                if index < len(left_numbers) - 1 : 
                    first_number = left_numbers[index]
                    last_number= left_numbers[index+1]
                    first_index = self.__get_first_index(first_number, save_indexs)
                    save_indexs[first_number] = first_index
                    last_index = self.__get_index(last_number, self.equation.text, save_indexs, True)
                    save_indexs[last_number] = last_index
                    text_sign_number = self.equation.text[first_index : last_index]
                    sign_number = SignNumber(text_sign_number, 0, index, 0)
                    sign_number.determine_priority()
                    self.equation.parts[0].signs_numbers.append(sign_number)


    def __get_signs_numbers_unknown(self, text) : 
        text_sign_number = ''
        index = 0
        while index < len(text) : 
            character = text[index]
            is_numeral = self.__is_numeral(character)
            text_sign_number = text_sign_number + character
            if is_numeral == False and character == 'x' :
                break
            index = index + 1
        if text_sign_number != '' :
            sign_number = SignNumber(text_sign_number, 0, index, 0)
            self.equation.parts[0].signs_numbers.append(sign_number)



    def __get_first_index(self, first_number, save_indexs) : 
        first_index = self.__get_index(first_number, self.equation.text, save_indexs, False)
        if first_index > 0 :
            sign = self.equation.text[first_index - 1]
            if sign == '-' :
                first_index = first_index - 1
        return first_index
                

    def __get_index(self, number, text, save_indexs, is_last_index) : 
        index = 0
        indexs = re.finditer(number, text)
        for i in indexs : 
            if (number in save_indexs and save_indexs[number] == i.start())  :
                continue 
            else :
                index = i.start()
                break
        if is_last_index : 
            index += len(number) 
        return index


    def __get_signs_numbers_small_equation(self) :
        text_sign_number = self.equation.parts[0].text
        sign_number = SignNumber(text_sign_number, 0, 0, 0)
        self.equation.parts[0].signs_numbers.append(sign_number)


    def __determine_order_sign_number(self, signs_numbers) :
        last_order = 0
        last_order = self.__set_order(last_order, signs_numbers, 2)
        self.__set_order(last_order, signs_numbers, 1)


    def __set_order(self, last_order, signs_numbers, priority) :
        for sign_number in signs_numbers :
            if sign_number.priority == priority : 
                sign_number.order = last_order
                last_order = last_order + 1
            else : 
                continue 
        return last_order



