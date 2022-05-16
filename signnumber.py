class SignNumber : 
    def __init__(self, text, priority, position, order) : 
        self.text = text
        self.priority = priority
        self.position = position
        self.order = order


    def determine_priority(self) : 
        if '*' in self.text or '/' in self.text :
            self.priority = 2
        elif '+' in self.text or '-' in self.text :
            self.priority = 1