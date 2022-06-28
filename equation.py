from solve import Solve
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
            solve = Solve(self.rewrite, self.analyze, self.rewrite_eq)
            self.unknown_value = solve.solve()