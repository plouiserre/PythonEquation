class SignNumber : 
    def __init__(self, text, priority, position, order) : 
        self.text = text
        self.priority = priority
        self.position = position
        self.order = order
        self.sign = ''


    def determine_priority(self) : 
        if '*' in self.text or '/' in self.text :
            self.priority = 2
        elif '+' in self.text or '-' in self.text :
            self.priority = 1

    
    def determine_sign(self) :
        if '*' in self.text :
            self.sign = '*'
        elif '/' in self.text : 
            self.sign = '/'
        elif '+' in self.text : 
            self.sign = '+'
        else :
            self.sign = '-'