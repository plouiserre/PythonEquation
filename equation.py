from part import Part
#TODO unit test for this class
class Equation : 
    def __init__(self, text) : 
        self.text = text
        self.parts = []


    def get_parts(self) : 
        parts = self.text.split("=")
        for part in parts :
            find_part = Part(part)
            self.parts.append(find_part)