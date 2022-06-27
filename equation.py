import numbers
from part import Part


#TODO voir si on explose Equation
class Equation : 
    def __init__(self, text, analyze, rewrite) : 
        self.text = text
        self.sign = ''
        self.parts = []
        self.rewrite_eq = []
        self.unknown_value = 0
        self.analyze = analyze
        self.is_validate = False
        self.rewrite = rewrite
    

    #TODO améliorer
    def process_resolve(self) : 
        self.text = self.text.replace(" ","")
        self.is_validate = self.analyze.is_validate()
        if self.is_validate :
            while self.rewrite.equation_can_be_solved == False:
                self.analyze.determine_all_elements(self.text)
                last_rewrite = self.rewrite.rewrite()
                self.rewrite_eq.append(last_rewrite)
                if self.rewrite.equation_can_be_solved == False : 
                    self.__simplify(len( self.rewrite_eq) - 1)
            self.__solve()


    

    
    


    


    


    #TODO nettoyer
    def __simplify(self, len_index) :
        text = self.rewrite_eq[len_index]
        parts = text.split("=")
        first_part = parts[0]
        second_part = parts[1]
        first_number_str = ''
        second_number_str = ''
        is_first_number_finished = False
        sign = ''
        for i in range (0,len(second_part)) : 
            element = second_part[i]
            if self.analyze.is_numeral(element) and is_first_number_finished == False :
                first_number_str = first_number_str + element
            elif self.analyze.is_numeral(element) and is_first_number_finished : 
                second_number_str = second_number_str + element
            else : 
                sign = sign + element
                is_first_number_finished = True

        first_number = int(first_number_str)
        second_number = int(second_number_str)

        new_second_part = 0

        if sign == '-' :
            new_second_part = first_number - second_number
        elif sign == '+' :
            new_second_part = first_number + second_number
        elif sign == '/' :
            new_second_part = first_number / second_number
        elif sign == '/-' :
            new_second_part = first_number / - second_number
        elif sign == '*' :
            new_second_part = first_number * second_number
        elif sign == '*-' :
            new_second_part = first_number * - second_number

        self.text = first_part+"="+str(new_second_part)


    #TODO retravailler
    def __solve(self) : 
        if self.rewrite.equation_can_be_solved : 
            self.analyze.determine_all_elements(self.rewrite_eq[len(self.rewrite_eq)-1])
            first_number = int(self.analyze.numbers[0])
            second_number = int(self.analyze.numbers[1])

            if self.rewrite.new_sign == '-' :
                self.unknown_value = first_number - second_number
            elif self.rewrite.new_sign == '+' :
                self.unknown_value = first_number + second_number
            elif self.rewrite.new_sign == '/' :
                self.unknown_value = first_number / second_number
            elif self.rewrite.new_sign == '/-' :
                self.unknown_value = first_number / - second_number
            elif self.rewrite.new_sign == '*' :
                self.unknown_value = first_number * second_number
            elif self.rewrite.new_sign == '*-' :
                self.unknown_value = first_number * - second_number


    