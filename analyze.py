import re 

from equation import Equation
from signnumber import SignNumber

class Analyze : 
    def __init__(self, equation) :
        self.equation = Equation(equation)
        self.parts = []


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


    #TODO changer le nom de cette méthode
    def identification(self) :
        numbers = self.__get_numbers()

        self.__concatene_numbers_signs(numbers)


    def __get_numbers(self) : 
        numbers = []
        number = ''
        for element in self.equation.text :
            if self.__is_numeral(element):
                number += element   
            elif number == '=':  
                numbers.append(number)  
                number = ''
                break
            elif number != '': 
                numbers.append(number)  
                number = ''

        return numbers

    
    def __is_numeral(self, element) :
        if element != '+' and element != '-' and element != '*' and element != '/' and element != '=' and element != 'x':
            return True 
        else :
            return False


    def __concatene_numbers_signs(self, numbers) :
        equation = self.equation.text
        if len(numbers) > 1 :
            self.__get_signs_numbers_large_equation(numbers, equation)
        else : 
            self.__get_signs_numbers_small_equation(numbers, equation)
        self.__determine_order_sign_number(self.equation.parts[0].signs_numbers)


    def __get_signs_numbers_large_equation(self, numbers, equation) : 
        save_indexs = {}
        for index, _ in enumerate(numbers) : 
                if index < len(numbers) - 1 : 
                    first_number = numbers[index]
                    last_number= numbers[index+1]
                    first_index = self.__get_index(first_number, equation, save_indexs, False)
                    save_indexs[first_number] = first_index
                    last_index = self.__get_index(last_number, equation, save_indexs, True)
                    save_indexs[last_number] = last_index
                    text_sign_number = equation[first_index : last_index]
                    sign_number = SignNumber(text_sign_number, 0, index, 0)
                    sign_number.determine_priority()
                    self.equation.parts[0].signs_numbers.append(sign_number)


    def __get_signs_numbers_small_equation(self, numbers, equation) :
        text_sign_number = self.equation.parts[0].text
        sign_number = SignNumber(text_sign_number, 0, 0, 0)
        self.equation.parts[0].signs_numbers.append(sign_number)
                


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



