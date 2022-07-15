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
        self.is_only_unknow = False
        self.parts = []
        self.left_part_to_simplify = ''
        self.right_part_to_simplify = ''
        self.numbers_unknown = []
        self.numbers_left_part = []
        self.sign_unknown = ''

    
    def rewrite(self, analyze) : 
        self.analyze = analyze
        self.signs = self.analyze.signs
        self.__get_signs_good_order()
        self.__get_elements_to_delete()
        self.__get_next_step()
        self.__is_eq_can_be_solved()
        return self.step


    def __get_signs_good_order(self) :
        self.signs_good_order.clear()
        for i in range (0,len(self.signs)) : 
            index = len(self.signs) - i - 1
            self.signs_good_order.append(self.signs[index])


    def __get_elements_to_delete(self) :
        if len(self.signs_good_order) > 0 :
            is_unknow_both_side = self.__get_unknown_both_sides()
            if is_unknow_both_side : 
                self.__get_unknows_to_delete()
            else : 
                self.__get_elements_left_side_to_delete()
        else : 
            self.__get_left_side_only_unknow_to_delete()


    def __get_unknown_both_sides(self) : 
        self.parts = self.analyze.text.split("=")
        if 'x' in self.parts[0] and 'x' in self.parts[1] : 
            return True 
        else : 
            return False


    def __get_unknows_to_delete(self) :
        part_right = self.parts[1]
        for unknown in self.analyze.unknowns :
            if unknown in part_right : 
                self.elements_to_delete = unknown
                break
        sign_to_delete = part_right[len(unknown)]
        self.elements_to_delete += sign_to_delete


    def __get_elements_left_side_to_delete(self) :
        self.sign_to_delete = self.signs_good_order[0]
        last_occurence = self.__get_last_occurence()
        index_sign = self.analyze.get_index_signs(self.sign_to_delete, last_occurence)
        index_equal = self.analyze.get_index_signs('=',1)
        self.elements_to_delete = self.analyze.text[index_sign : index_equal]
        self.elements_to_replace = ''


    def __get_last_occurence(self) : 
        last_occurence = 0
        index = 0
        while index < len(self.signs_good_order) : 
                if self.sign_to_delete == self.signs_good_order[index] or self.sign_to_delete in self.signs_good_order[index]:
                    last_occurence += 1
                index += 1
        return last_occurence


    def __get_left_side_only_unknow_to_delete(self) :
        index_unknown = self.analyze.get_index_signs('x',1) 
        self.sign_to_delete = '*'
        self.elements_to_delete = self.analyze.text[0 : index_unknown] + 'x'
        self.element_to_replace = 'x'
        self.is_only_unknow = True
        

    def __get_next_step(self) : 
        self.analyze.text = self.analyze.text.replace(self.elements_to_delete,self.element_to_replace)
        if 'x' in self.elements_to_delete and self.is_only_unknow == False:
            self.__construct_new_sign(self.analyze.right_signs)
            parts = self.analyze.text.split("=")
            right_part_one = self.elements_to_delete.replace('-','').replace('+','')
            part_left = parts[0] + self.new_sign +right_part_one
            part_right= parts[1]
            self.step =  part_left +  '=' + part_right
        else :
            self.__construct_new_sign(self.signs)
            number_index = len(self.analyze.numbers) - 2
            self.step = self.analyze.text + self.new_sign + self.analyze.numbers[number_index] 
        

    def __construct_new_sign(self, signs) :
        self.__simplified_signs(signs)
        if len(self.signs_simplified) > 1 : 
            self.new_sign = self.__get_new_signs_for_complexs()
        elif self.signs_simplified != '' :
            self.new_sign = self.__get_new_sign(self.signs_simplified)
        else :
            for sign in signs :
                self.new_sign += self.__get_new_sign(sign)


    def __simplified_signs(self, signs) :
        self.__add_multiply_if_otmitted()
        signs_to_simplified = ''.join(signs)
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
        left_part = self.step.split("=")[0]
        if  left_part == "x" : 
            self.equation_can_be_solved = True


    def simplify(self, text_to_simplify) :
        parts = text_to_simplify.split("=")
        self.left_part_to_simplify = parts[0]
        self.right_part_to_simplify = parts[1]        
        
        new_left_part = self.__simplify_left_part()
        new_right_part = self.__simplify_right_part()

        text = new_left_part+"="+str(new_right_part)

        return text


    def __simplify_left_part(self) :
        self.analyze.determine_all_elements(self.left_part_to_simplify) 
        if len(self.analyze.unknowns) == 1 :
            return self.left_part_to_simplify
        
        self.__get_numbers_unkown_numbers_and_sign()
        first_number_str = self.numbers_unknown[0].replace('x','')
        second_number_str = self.numbers_unknown[1].replace('x','')

        first_number = float(first_number_str)
        second_number = float(second_number_str)

        solve = Solve()
        
        left_part_number= solve.do_the_math(first_number, second_number, self.sign_unknown)
        
        new_left_part = str(left_part_number)+'x'
        
        new_left_part = self.__simplify_new_left_part(self.numbers_left_part, new_left_part)         
        
        return new_left_part

    
    def __get_numbers_unkown_numbers_and_sign(self) : 
        left_part_working = self.left_part_to_simplify
        for unknown in self.analyze.unknowns : 
            self.numbers_unknown.append(unknown) 
            left_part_working.replace(unknown, ' ')

        if '-' in self.numbers_unknown[1] :
            self.sign_unknown = '+'
        else :
            index_second_unknown = self.analyze.text.find(self.numbers_unknown[1])

            self.sign_unknown = self.analyze.text[index_second_unknown-1]

        for sign in self.analyze.signs : 
                left_part_working = left_part_working.replace(sign,' ')
        
        parts = left_part_working.split(' ')
        for part in parts :
            if ('x' in part) == False :
                self.numbers_left_part.append(part)


    def __simplify_new_left_part(self, numbers, new_left_part) : 
        if len(numbers) > 0 :
            sign_number = "" 
            index = self.left_part_to_simplify.find(numbers[0])
            if index == 0 :
                sign_number = "+"
            else :
                sign_number = self.left_part_to_simplify[index-1]
            new_left_part = new_left_part.replace("1.0x","x").replace(".0x","x") + sign_number+ numbers[0]  
        return new_left_part



    def __simplify_right_part(self): 
        self.analyze.determine_all_elements(self.right_part_to_simplify)
        first_number = 0
        second_number = 0
        sign = ''

        if len(self.analyze.all_signs) == 0 : 
            return self.right_part_to_simplify
        
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
        new_right_part = solve.do_the_math(first_number, second_number, sign)
        return new_right_part