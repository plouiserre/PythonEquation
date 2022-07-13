#TODO simply self.rewrite_eq because we do not need it
class Solve :
    def __init__(self, *args) :
        if len(args) > 0 : 
            self.rewrite = args[0]
            self.analyze = args[1]
            self.rewrite_eq = args[2]


    def solve(self) : 
        result = 0
        if self.rewrite.equation_can_be_solved : 
            self.analyze.determine_all_elements(self.rewrite_eq[len(self.rewrite_eq)-1])
            first_number_str =  ''
            if len(self.analyze.all_signs) == 2 :
               first_number_str = self.analyze.numbers[0]
            else : 
                first_number_str = '-'+self.analyze.numbers[0]  
            first_number = float(first_number_str) 
            second_number = float(self.analyze.numbers[1])


            result = self.do_the_math(first_number, second_number, self.rewrite.new_sign)
        
        return result


    def do_the_math(self, first_number, second_number, sign) :
        if sign == '-' :
            result = first_number - second_number
        elif sign == '+' :
            result = first_number + second_number
        elif sign == '/' :
            result = first_number / second_number
        elif sign == '/-' :
            result = first_number / - second_number
        elif sign == '*' :
            result = first_number * second_number
        elif sign == '*-' :
            result = first_number * - second_number
        return result
        