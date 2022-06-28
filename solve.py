class Solve :
    #TODO simplifier constructeur en supprimant le analyze des paramètres
    def __init__(self, rewrite, analyze, rewrite_eq) : 
        self.rewrite = rewrite
        self.analyze = analyze
        self.rewrite_eq = rewrite_eq

    def solve(self) : 
        result = 0
        if self.rewrite.equation_can_be_solved : 
            self.analyze.determine_all_elements(self.rewrite_eq[len(self.rewrite_eq)-1])
            first_number = int(self.analyze.numbers[0])
            second_number = int(self.analyze.numbers[1])

            if self.rewrite.new_sign == '-' :
                result = first_number - second_number
            elif self.rewrite.new_sign == '+' :
                result = first_number + second_number
            elif self.rewrite.new_sign == '/' :
                result = first_number / second_number
            elif self.rewrite.new_sign == '/-' :
                result = first_number / - second_number
            elif self.rewrite.new_sign == '*' :
                result = first_number * second_number
            elif self.rewrite.new_sign == '*-' :
                result = first_number * - second_number
        return result
        