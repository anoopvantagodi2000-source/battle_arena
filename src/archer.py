from character import Character

class Archer(Character):
    def __init__(self,name,health,attack_power,defence):
        super().__init__(name,health,attack_power + 2,defence)