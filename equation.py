from solve import Solve
from part import Part


class Equation : 
    def __init__(self, text, analyze, rewrite) : 
        self.text = text
        self.sign = ''
        self.parts = []
        self.steps = []
        self.unknown_value = 0
        self.analyze = analyze
        self.is_validate = False
        self.rewrite = rewrite
    

    def resolve(self) : 
        self.text = self.text.replace(" ","")
        self.is_validate = self.analyze.is_validate()
        if self.is_validate :
            index = 0
            while self.rewrite.equation_can_be_solved == False:
                self.__transform()
                index += 1
            solve = Solve(self.rewrite, self.analyze, self.steps)
            self.unknown_value = solve.solve()


    def __transform(self) : 
        self.analyze.determine_all_elements(self.text)
        last_step = self.rewrite.rewrite(self.analyze)
        self.steps.append(last_step)
        if self.rewrite.equation_can_be_solved == False : 
            self.text = self.rewrite.simplify(last_step)