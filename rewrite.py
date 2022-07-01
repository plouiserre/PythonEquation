from solve import Solve

class Rewrite :

    def __init__(self) :
        self.step = ''
        self.equation_can_be_solved = False
        self.new_sign = ''
        self.signs_simplified = ''
        self.signs = []
        self.sign_to_delete = ''
        self.element_to_delete = ''
        self.element_to_replace =''
    
    def rewrite(self, analyze) : 
        self.analyze = analyze
        self.signs = self.analyze.signs
        all_signs = self.__get_all_signs()
        self.__get_elements_to_delete(all_signs)
        self.__get_this_step()
        self.__is_eq_can_be_solved()
       
        return self.step


    def __get_all_signs(self) :
        all_signs = ''
        for i in range (0,len(self.signs)) : 
            index = len(self.signs) - i - 1
            all_signs += self.signs[index]
        return all_signs


    def __get_elements_to_delete(self, all_signs) :
        if len(all_signs) > 0 :
            self.sign_to_delete = all_signs[0]
            index_sign = self.analyze.get_index_signs(self.sign_to_delete)
            index_equal = self.analyze.get_index_signs('=')
            self.elements_to_delete = self.analyze.text[index_sign : index_equal]
            self.elements_to_replace = ''
        else : 
            index_unknown = self.analyze.get_index_signs('x') 
            self.sign_to_delete = '*'
            self.elements_to_delete = self.analyze.text[0 : index_unknown] + 'x'
            self.element_to_replace = 'x'
        

    def __get_this_step(self) : 
        self.analyze.text = self.analyze.text.replace(self.elements_to_delete,self.element_to_replace)
        self.__construct_new_sign()
        number_index = len(self.analyze.numbers) - 2
        self.step = self.analyze.text + self.new_sign + self.analyze.numbers[number_index] 
        

    #TODO tout revoir sur la construction des signs
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
            self.signs_simplified =  self.sign_to_delete



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

        first_number = float(self.analyze.numbers[0])
        second_number = float(self.analyze.numbers[1])
        sign = self.analyze.signs[0]

        solve = Solve()
        new_second_part = solve.do_the_math(first_number, second_number, sign)

        text = first_part+"="+str(new_second_part)

        return text