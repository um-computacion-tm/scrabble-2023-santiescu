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



