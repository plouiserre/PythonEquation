from solve import Solve

class Rewrite :

    def __init__(self) :
        self.step = ''
        self.equation_can_be_solved = False
        self.new_sign = ''
        self.signs_simplified = ''
        self.signs = []
        self.signs_good_order = []
        self.sign_to_delete = ''
        self.element_to_delete = ''
        self.element_to_replace = ''

    
    def rewrite(self, analyze) : 
        self.analyze = analyze
        self.signs = self.analyze.signs
        self.__get_signs_good_order()
        self.__get_elements_to_delete()
        self.__get_this_step()
        self.__is_eq_can_be_solved()
        return self.step


    def __get_signs_good_order(self) :
        self.signs_good_order.clear()
        for i in range (0,len(self.signs)) : 
            index = len(self.signs) - i - 1
            self.signs_good_order.append(self.signs[index])


    def __get_elements_to_delete(self) :
        if len(self.signs_good_order) > 0 :
            self.sign_to_delete = self.signs_good_order[0]
            last_occurence = self.__get_last_occurence()
            index_sign = self.analyze.get_index_signs(self.sign_to_delete, last_occurence)
            index_equal = self.analyze.get_index_signs('=',1)
            self.elements_to_delete = self.analyze.text[index_sign : index_equal]
            self.elements_to_replace = ''
        else : 
            index_unknown = self.analyze.get_index_signs('x',1) 
            self.sign_to_delete = '*'
            self.elements_to_delete = self.analyze.text[0 : index_unknown] + 'x'
            self.element_to_replace = 'x'


    def __get_last_occurence(self) : 
        last_occurence = 0
        index = 0
        while index < len(self.signs_good_order) : 
                if self.sign_to_delete == self.signs_good_order[index] or self.sign_to_delete in self.signs_good_order[index]:
                    last_occurence += 1
                index += 1
        return last_occurence
        

    def __get_this_step(self) : 
        self.analyze.text = self.analyze.text.replace(self.elements_to_delete,self.element_to_replace)
        self.__construct_new_sign()
        number_index = len(self.analyze.numbers) - 2
        self.step = self.analyze.text + self.new_sign + self.analyze.numbers[number_index] 
        

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
        elif signs_to_simplified == '*-' or signs_to_simplified == '/-':
            self.signs_simplified = signs_to_simplified
        else :
            self.signs_simplified =  self.sign_to_delete



    def __add_multiply_if_otmitted(self) : 
        if len(self.signs) == 0 : 
            self.signs.append('*')


    def __get_new_signs_for_complexs (self) :
        new_sign = ''
        if self.signs_good_order[0] == '*-' :
            new_sign = "/-"
        elif self.signs_good_order[0] == '/-' :
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

        
        new_first_part = self.__simplify_first_part(first_part)
        new_second_part = self.__simplify_second_part(second_part)

        text = new_first_part+"="+str(new_second_part)

        return text


    def __simplify_first_part(self, first_part) :
        self.analyze.determine_all_elements(first_part) 
        if len(self.analyze.unknowns) == 1 :
            return first_part
        else : 
            sign = self.analyze.signs[0]
            parts = first_part.split(sign)
            first_number_str = parts[0].replace('x','')
            second_number_str = parts[1].replace('x','')

            first_number = float(first_number_str)
            second_number = float(second_number_str)

            solve = Solve()
            first_part_number= solve.do_the_math(first_number, second_number, sign)
            new_first_part = str(first_part_number)+'x'
            return new_first_part



    def __simplify_second_part(self, second_part): 
        self.analyze.determine_all_elements(second_part)
        first_number = 0
        second_number = 0
        sign = ''

        if len(self.analyze.all_signs) == 1 : 
            first_number = float(self.analyze.numbers[0])
            second_number = float(self.analyze.numbers[1])
            sign = self.analyze.all_signs[0]
        else : 
            first_number_str = self.analyze.all_signs[0]+self.analyze.numbers[0]
            first_number = float(first_number_str)
            second_number = float(self.analyze.numbers[1])
            sign = self.analyze.all_signs[1]

        solve = Solve()
        new_second_part = solve.do_the_math(first_number, second_number, sign)
        return new_second_part