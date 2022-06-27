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
                    self.text = self.rewrite.simplify(last_rewrite)
            self.__solve()


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


    