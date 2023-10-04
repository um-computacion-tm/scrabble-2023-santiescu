from Game.models import Tile

class Cell:
    
    def __init__(self, multiplier, multiplier_type, letter):
        self.multiplier= multiplier
        self.multiplier_type = multiplier_type
        self.letter = None

    def add_letter(self, letter): 
        self.letter=letter 

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value

    def calculate_word_value(self, word):
            word_value = 0
            word_multiplier = 1
            for l in word :
                word_value += l.calculate_value()  
                if l.multiplier_type == 'word':
                    word_multiplier = l.multiplier
                    l.multiplier_type = None
            word_value *= word_multiplier
            return word_value

