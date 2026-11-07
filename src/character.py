

class Character:
    def __init__(self,name,health,attack_power,defence):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defence = defence
    def attack(self,other_character:Character):
        # damage induced by attacker
        damage = max(self.attack_power - other_character.defence,0)
        other_character.take_damage(damage)
        self.health += damage


    def take_damage(self,amount:int):
        self.health = max(0,self.health - amount)

    def is_alive(self):
        return self.health > 0

    def __str__(self) -> str:
        return (f"name:{self.name}\n health:{self.health} \n attack_power : {self.attack_power}\n"
                f"defense : {self.defence} \n")





