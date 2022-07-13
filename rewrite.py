from solve import Solve
#TODO mettre les parts en variables d'objets
#TODO mieux gérer le split
#TODO renommer first_part and second_part en left_part et right_part
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


    #TODO : 
        # 1 - voir si les X sont du même côté : 
            # Si oui on fait comme d'habitude 
            # Si non on passe à l'étape 2
        # 2 - supprimer à droite les X 
    def __get_elements_to_delete(self) :
        if len(self.signs_good_order) > 0 :
            is_unknow_both_side = self.__get_unknown_both_sides()
            if is_unknow_both_side : 
                part_two = self.analyze.text.split("=")[1]
                for unknown in self.analyze.unknowns :
                    if unknown in part_two : 
                        self.elements_to_delete = unknown
                        break
                if part_two.find(unknown) == 0 : 
                    sign_to_delete = part_two[len(unknown)]
                    self.elements_to_delete += sign_to_delete
                else : 
                    #TODO améliorer ca
                    sign_to_delete = self.analyze.right_signs[0][0]
                    self.elements_to_delete = sign_to_delete + self.elements_to_delete
            else : 
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
            self.is_only_unknow = True

    #TODO mettre dnans une variable et ne l'appeler qu'une fois
    def __get_unknown_both_sides(self) : 
        parts = self.analyze.text.split("=")
        if 'x' in parts[0] and 'x' in parts[1] : 
            return True 
        else : 
            return False


    def __get_last_occurence(self) : 
        last_occurence = 0
        index = 0
        while index < len(self.signs_good_order) : 
                if self.sign_to_delete == self.signs_good_order[index] or self.sign_to_delete in self.signs_good_order[index]:
                    last_occurence += 1
                index += 1
        return last_occurence
        

    #TODO :
        # 1 - Est-ce que les X sont du même côté 
            # Si oui on fait comme d'habitude 
            # Si non on passe à l'autre étape
        # 2 - on ajoute les X du même côté
    def __get_this_step(self) : 
        self.analyze.text = self.analyze.text.replace(self.elements_to_delete,self.element_to_replace)
        if 'x' in self.elements_to_delete and self.is_only_unknow == False:
            self.__construct_new_sign(self.analyze.right_signs)
            parts = self.analyze.text.split("=")
            #TODO trouver une autre facon
            second_part_one = self.elements_to_delete.replace('-','').replace('+','')
            part_one = parts[0] + self.new_sign +second_part_one
            part_two = parts[1]
            self.step =  part_one +  '=' + part_two
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


    #TODO refaire cette méthode
    def __simplify_first_part(self, first_part) :
        self.analyze.determine_all_elements(first_part) 
        if len(self.analyze.unknowns) == 1 :
            return first_part
        else : 
            sign = self.analyze.signs[0]
            first_part_working = first_part
            for sign in self.analyze.signs : 
                first_part_working = first_part_working.replace(sign,' ')
            parts = first_part_working.split(' ')
            numbers_unknown = []
            numbers = []
            for part in parts : 
                if 'x' in part :
                    numbers_unknown.append(part)
                else : 
                    numbers.append(part)
            first_number_str = numbers_unknown[0].replace('x','')
            second_number_str = numbers_unknown[1].replace('x','')

            first_number = float(first_number_str)
            second_number = float(second_number_str)

            solve = Solve()
            first_part_number= solve.do_the_math(first_number, second_number, sign)
            
            new_first_part = str(first_part_number)+'x'
            
            if len(numbers) > 0 :
                sign_number = "" 
                index = first_part.find(numbers[0])
                if index == 0 :
                    sign_number = "+"
                else :
                    sign_number = first_part[index-1]
                new_first_part = new_first_part.replace("1.0x","x").replace(".0x","x") + sign_number+ numbers[0]            
            
            return new_first_part



    def __simplify_second_part(self, second_part): 
        self.analyze.determine_all_elements(second_part)
        first_number = 0
        second_number = 0
        sign = ''

        if len(self.analyze.all_signs) == 0 : 
            return second_part
        
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