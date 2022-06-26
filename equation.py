import numbers
from part import Part


#TODO voir si on explose Equation
class Equation : 
    def __init__(self, text, analyze) : 
        self.text = text
        self.sign = ''
        #self.numbers = []
        self.parts = []
        self.rewrite_eq = []
        self.unknown_value = 0
        self.equation_can_be_solved = False
        self.new_sign =''
        self.analyze = analyze
        self.is_validate = False
    

    #TODO améliorer
    def process_resolve(self) : 
        self.text = self.text.replace(" ","")
        self.is_validate = self.analyze.is_validate()
        if self.is_validate :
            while self.equation_can_be_solved == False:
                self.analyze.determine_all_elements(self.text)
                self.__rewrite()
                if self.equation_can_be_solved == False : 
                    self.__simplify(len( self.rewrite_eq) - 1)
            self.__solve()


    #TODO enlever aussi les signs en param
    def __rewrite(self) : 
        number = self.analyze.numbers[0]
        signs_finded = self.analyze.detects_signs()
        all_signs = ''.join(signs_finded)
        #on détecte l'index du premier sign
        element_to_delete = ''
        if len(all_signs) > 0 :
            index_sign = self.analyze.get_index_signs(all_signs[0])
            index_equal = self.analyze.get_index_signs('=')
            element_to_delete = self.text[index_sign : index_equal]
        else : 
            index_unknown = self.analyze.get_index_signs('x') 
            element_to_delete = self.text[0 : index_unknown]

        #on détecte l'index du = 
        #du premier index - 1 à egal ca correspond à element_to_delete
        #element_to_delete = all_signs + number
        self.text = self.text.replace(element_to_delete,'')
        self.new_sign = self.__construct_new_sign(signs_finded)
        #self.text = self.text+self.new_sign+number
        self.rewrite_eq.append(self.text + self.new_sign + number)
        self.__is_eq_can_be_solved(len(self.rewrite_eq) - 1)

    
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


    def __is_eq_can_be_solved(self, len_index) :
        text = self.rewrite_eq[len_index]
        #TODO retravailler pour voir si on peut utiliser la bonne méthode
        first_part = text.split("=")[0]
        if  first_part == "x" : 
            self.equation_can_be_solved = True


    #TODO nettoyer
    def __simplify(self, len_index) :
        text = self.rewrite_eq[len_index]
        parts = text.split("=")
        first_part = parts[0]
        second_part = parts[1]
        first_number_str = ''
        second_number_str = ''
        is_first_number_finished = False
        sign = ''
        for i in range (0,len(second_part)) : 
            element = second_part[i]
            if self.analyze.is_numeral(element) and is_first_number_finished == False :
                first_number_str = first_number_str + element
            elif self.analyze.is_numeral(element) and is_first_number_finished : 
                second_number_str = second_number_str + element
            else : 
                sign = sign + element
                is_first_number_finished = True

        first_number = int(first_number_str)
        second_number = int(second_number_str)

        new_second_part = 0

        if sign == '-' :
            new_second_part = first_number - second_number
        elif sign == '+' :
            new_second_part = first_number + second_number
        elif sign == '/' :
            new_second_part = first_number / second_number
        elif sign == '/-' :
            new_second_part = first_number / - second_number
        elif sign == '*' :
            new_second_part = first_number * second_number
        elif sign == '*-' :
            new_second_part = first_number * - second_number

        self.text = first_part+"="+str(new_second_part)


    #TODO retravailler
    def __solve(self) : 
        if self.equation_can_be_solved : 
            #if len(self.rewrite_eq) > 1 : 
            self.analyze.determine_all_elements(self.rewrite_eq[len(self.rewrite_eq)-1])
            first_number = int(self.analyze.numbers[0])
            second_number = int(self.analyze.numbers[1])

            if self.new_sign == '-' :
                self.unknown_value = first_number - second_number
            elif self.new_sign == '+' :
                self.unknown_value = first_number + second_number
            elif self.new_sign == '/' :
                self.unknown_value = first_number / second_number
            elif self.new_sign == '/-' :
                self.unknown_value = first_number / - second_number
            elif self.new_sign == '*' :
                self.unknown_value = first_number * second_number
            elif self.new_sign == '*-' :
                self.unknown_value = first_number * - second_number


    