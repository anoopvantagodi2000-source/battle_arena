from character import Character

class Warrior(Character):
    def __init__(self,name,health,attack_power,defence):
        super().__init__(name,health,attack_power + 5,defence)




class Archer(Character):
    def __init__(self,name,health,attack_power,defence):
        super().__init__(name,health,attack_power + 2,defence)