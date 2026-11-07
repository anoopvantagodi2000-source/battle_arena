from character import Character

class Mage(Character):
    def __init__(self,name,health,attack_power,defence):
        super().__init__(name,health,attack_power*1.5,defence)