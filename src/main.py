
from  warrior import Warrior
from mage import  Mage
from archer import Archer



def main():
    ## create character
    thor = Warrior("Thor",120,25,10)
    merlin = Mage("Merlin",80,35,5)
    robin = Archer("Robin",100,20,8)

    ## Battle time
    thor.attack(merlin)
    print(thor)
    print(merlin)
    print(f"{merlin.name} is alive : {merlin.is_alive()}")
    print("*" * 50)

    merlin.attack(thor)
    print(merlin)
    print(thor)
    print(f"{thor.name} is alive : {thor.is_alive()}")
    print("*" * 50)


    robin.attack(merlin)
    print(robin)
    print(merlin)
    print(f"{merlin.name} is alive : {merlin.is_alive()}")

    # task 3 : Battle until death
    attacker = thor
    defender = merlin
    while defender.is_alive() and attacker.is_alive():
        attacker.attack(defender)
        if not defender.is_alive():
            print(f"Winner is : {attacker.name}")
            break
        attacker,defender = defender,attacker
    print("\nWinner's Stats:")
    print(attacker)





main()