class Rewrite :

    def __init__(self, analyze) :
        self.analyze = analyze
        self.rewrite_eq = ''
        self.equation_can_be_solved = False
        self.new_sign = ''
    
    #TODO retravailler cette méthode
    #TODO enlever aussi les signs en param
    def rewrite(self) : 
        number = self.analyze.numbers[0]
        signs_finded = self.analyze.detects_signs()
        all_signs = ''.join(signs_finded)
        #on détecte l'index du premier sign
        element_to_delete = ''
        if len(all_signs) > 0 :
            index_sign = self.analyze.get_index_signs(all_signs[0])
            index_equal = self.analyze.get_index_signs('=')
            element_to_delete = self.analyze.text[index_sign : index_equal]
        else : 
            index_unknown = self.analyze.get_index_signs('x') 
            element_to_delete = self.analyze.text[0 : index_unknown]

        #on détecte l'index du = 
        #du premier index - 1 à egal ca correspond à element_to_delete
        #element_to_delete = all_signs + number
        self.analyze.text = self.analyze.text.replace(element_to_delete,'')
        self.new_sign = self.__construct_new_sign(signs_finded)
        self.rewrite_eq = self.analyze.text + self.new_sign + number 
        self.__is_eq_can_be_solved()
        return self.rewrite_eq


    def __construct_new_sign(self, signs) :
        new_sign = ''
        signs = self.__add_multiply_if_otmitted(signs)
        signs_simplified = self.__get_signs_simplified(signs)
        if len(signs_simplified) > 1 : 
            new_sign = self.__get_new_signs_for_complexs(signs)
        elif signs_simplified != '' :
            new_sign = self.__get_new_sign(signs_simplified)
        else :
            for sign in signs :
                new_sign += self.__get_new_sign(sign)
        return new_sign


    def __add_multiply_if_otmitted(self, signs) : 
        if signs == '' : 
            signs = '*'
        return signs


    def __get_signs_simplified(self, signs) :
        signs_to_simplified = ''.join(signs)
        if signs_to_simplified == '--' or signs_to_simplified =='++':
            signs_simplified = '+'
        elif signs_to_simplified == '+-' or signs_to_simplified == '-+' or signs_to_simplified == '-' :
            signs_simplified = '-'
        elif self.new_sign == '*+' :
            signs_simplified = '*'
        elif self.new_sign == '/+' :
            signs_simplified = '/'
        else :
            signs_simplified = signs_to_simplified
        return signs_simplified


    def __get_new_signs_for_complexs (self, signs) :
        signs_to_simplified = ''.join(signs)
        if signs_to_simplified == '*-' :
            signs_simplified = "/-"
        elif signs_to_simplified == '/-' :
            signs_simplified = "*-"
        else :
            signs_simplified = ''
        return signs_simplified


    def __get_new_sign(self, sign) :
        new_sign = ''
        if sign == '+' :
            new_sign += '-'
        elif sign == '-' : 
            new_sign += '+'
        elif sign == '*' : 
            new_sign += '/'
        elif sign == '/' : 
            new_sign += '*'
        return new_sign


    def __is_eq_can_be_solved(self) :
        #TODO retravailler pour voir si on peut utiliser la bonne méthode
        first_part = self.rewrite_eq.split("=")[0]
        if  first_part == "x" : 
            self.equation_can_be_solved = True