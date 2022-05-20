class Solve :
    def __init__(self, analyze) : 
        self.unknow = 0
        self.analyze = analyze

    def resolve(self) : 
        eq = self.analyze.equation 
        is_validate = self.analyze.is_validate()
        if is_validate : 
            self.analyze.identification()
            sign_number = eq.parts[0].signs_numbers[0]
            sign_number.determine_sign()
            eq.rewrite(sign_number.sign)
            eq.solve()
            self.unknow = eq.unknown_value
        else :
            print("Error")
        