import random


class Arena:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    pass


class Team:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    pass


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.staring_health = starting_health
        self.current_health = starting_health

        pass

    def take_damage(self, damage):
        

    def add_ability(self, ability):
        self.abilities.append(ability)
        pass

    def add_armor(self, armor):
        self.armors.append(armor)
        pass

    def attack(self):
        swingValue = 0
        for ability in self.abilities:
            swingValue += random.randint(0, ability.attack_strength)
        return swingValue

    def defend(self, damage_amt):
        defValue = 0
        for armor in self.armors:
            defValue += armor.max_block
        return defValue



class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        blockValue = random.randint(0, self.max_block)
        return blockValue

    pass


class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        swingValue = random.randint(0, self.attack_strength)
        return swingValue


if __name__ == "__main__":
    torrent = Ability("Mending Torrent", 286)
    flame = Ability("Scalding Flame", 78)
    shield = Armor("Gilded Shield", 358)
    myHero = Hero("Exalted of the Trees", 3939)
    print(myHero.name)
    print("Health: " + str(myHero.current_health))
    myHero.add_ability(torrent)
    myHero.add_ability(flame)
    myHero.add_armor(shield)
    print(myHero.armors)
    #hero.take_damage(50)
#    print(hero.current_health)
    print("Attack: " + str(myHero.attack()))
    print("Defend: " + str(myHero.defend(100)))
