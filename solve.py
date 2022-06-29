class Solve :
    #TODO simplifier constructeur en supprimant le analyze des paramètres
    def __init__(self, *args) :
        if len(args) > 0 : 
            self.rewrite = args[0]
            self.analyze = args[1]
            self.rewrite_eq = args[2]

    #TODO ajouter un TU pour checker qu'on fait pas de calcul si le boolean est à false
    def solve(self) : 
        result = 0
        if self.rewrite.equation_can_be_solved : 
            self.analyze.determine_all_elements(self.rewrite_eq[len(self.rewrite_eq)-1])
            first_number = int(self.analyze.numbers[0])
            second_number = int(self.analyze.numbers[1])

            result = self.do_the_math(first_number, second_number, self.rewrite.new_sign)
        
        return result


    #TODO TU 
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
        