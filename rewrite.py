from solve import Solve

class Rewrite :

    def __init__(self) :
        self.step = ''
        self.equation_can_be_solved = False
        self.new_sign = ''
        self.signs_simplified = ''
        self.signs = []
    
    def rewrite(self, analyze) : 
        self.analyze = analyze
        self.signs = self.analyze.signs
        all_signs = ''.join(self.signs)
        elements_to_delete = self.__get_elements_to_delete(all_signs)
        self.__get_this_step(elements_to_delete)
        self.__is_eq_can_be_solved()
       
        return self.step


    def __get_elements_to_delete(self, all_signs) :
        elements_to_delete = ''
        if len(all_signs) > 0 :
            index_sign = self.analyze.get_index_signs(all_signs[0])
            index_equal = self.analyze.get_index_signs('=')
            elements_to_delete = self.analyze.text[index_sign : index_equal]
        else : 
            index_unknown = self.analyze.get_index_signs('x') 
            elements_to_delete = self.analyze.text[0 : index_unknown]
        return elements_to_delete


    def __get_this_step(self, elements_to_delete) : 
        self.analyze.text = self.analyze.text.replace(elements_to_delete,'')
        self.__construct_new_sign()
        self.step = self.analyze.text + self.new_sign + self.analyze.numbers[0] 
        

    def __construct_new_sign(self) :
        self.__simplified_signs()
        if len(self.signs_simplified) > 1 : 
            self.new_sign = self.__get_new_signs_for_complexs()
        elif self.signs_simplified != '' :
            self.new_sign = self.__get_new_sign(self.signs_simplified)
        else :
            for sign in self.signs :
                self.new_sign += self.__get_new_sign(sign)


    def __simplified_signs(self) :
        self.__add_multiply_if_otmitted()
        signs_to_simplified = ''.join(self.signs)
        if signs_to_simplified == '--' or signs_to_simplified =='++':
            self.signs_simplified = '+'
        elif signs_to_simplified == '+-' or signs_to_simplified == '-+' or signs_to_simplified == '-' :
            self.signs_simplified = '-'
        elif self.new_sign == '*+' :
            self.signs_simplified = '*'
        elif self.new_sign == '/+' :
            self.signs_simplified = '/'
        else :
            self.signs_simplified = signs_to_simplified


    def __add_multiply_if_otmitted(self) : 
        if len(self.signs) == 0 : 
            self.signs.append('*')


    def __get_new_signs_for_complexs (self) :
        new_sign = ''
        if self.signs == '*-' :
            new_sign = "/-"
        elif self.signs == '/-' :
            new_sign = "*-"
        else :
            new_sign = ''
        return new_sign


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
        first_part = self.step.split("=")[0]
        if  first_part == "x" : 
            self.equation_can_be_solved = True


    def simplify(self, text_to_simplify) :
        parts = text_to_simplify.split("=")
        first_part = parts[0]
        second_part = parts[1]
        self.analyze.determine_all_elements(second_part)

        first_number = int(self.analyze.numbers[0])
        second_number = int(self.analyze.numbers[1])
        sign = self.analyze.signs[0]

        solve = Solve()
        new_second_part = solve.do_the_math(first_number, second_number, sign)

        text = first_part+"="+str(new_second_part)

        return text