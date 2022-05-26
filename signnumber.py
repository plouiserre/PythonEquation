class SignNumber : 
    def __init__(self, text, priority, position, order) : 
        self.text = text
        self.priority = priority
        self.position = position
        self.order = order
        self.sign = []


    def determine_priority(self) : 
        if '*' in self.text or '/' in self.text :
            self.priority = 2
        elif '+' in self.text or '-' in self.text :
            self.priority = 1

    
    def determine_sign(self) :
        is_simple = self.__determine_simple_or_complexe_signs()
        if is_simple : 
            self.__determine_sign_simple(self.text)
        else : 
            self.__determine_sign_complexe()


    def __determine_simple_or_complexe_signs(self): 
        is_simple_sign = True
        if '*'in self.text  and '-' in self.text :
            is_simple_sign = False
        elif '/'in self.text  and '-' in self.text :
            is_simple_sign = False
        elif '+'in self.text  and '-' in self.text :
            is_simple_sign = False
        elif self.text.count('-') > 1 :
            is_simple_sign = False
        return is_simple_sign


    def __determine_sign_complexe(self) :
        for element in self.text :
            if element == '-' or element == '+' or element == '*' or element == '/' : 
                self.sign.append(element)
            else :
                continue


    def __determine_sign_simple(self, text) : 
        if '*' in text :
            self.sign.append('*')
        elif '/' in text : 
            self.sign.append('/')
        elif '+' in text : 
            self.sign.append('+')
        else :
            self.sign.append('-')