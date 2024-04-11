import math

class Character:
    def __init__(self, name, height, strength_items, agility_items, proficiency_items, resistance_items, life_items):
        self.name = name
        self.height = height
        self.strength_items = strength_items
        self.agility_items = agility_items
        self.proficiency_items = proficiency_items
        self.resistance_items = resistance_items
        self.life_items = life_items

        #Raise an error if sum of items not equal to 150
        total_items = strength_items + agility_items + proficiency_items + resistance_items + life_items
        if total_items != 150:
            raise ValueError("Items sum of items must 150.")

        # Raise an error if the name is not valid
        valid_names = ["Warrior", "Archer", "Defender", "Infiltrator"]
        if name not in valid_names:
            raise ValueError("Invalid character name")

    def performance(self):
        strength_coeff = 100 * math.tanh(0.01 * self.strength_items)
        agility_coeff = math.tanh(0.01 * self.agility_items)
        proficiency_coeff = 0.6 * math.tanh(0.01 * self.proficiency_items)
        resistance_coeff = math.tanh(0.01 * self.resistance_items)
        life_coeff = 100 * math.tanh(0.01 * self.life_items)

        attack_modifier = 0.5 - (3*self.height - 5)**4 + (3*self.height - 5)**2 + self.height/2
        defense_modifier = 2 + (3*self.height - 5)**4 - (3*self.height - 5)**2 - self.height/2

        if self.name == "Warrior":
            attack = (agility_coeff + proficiency_coeff) * strength_coeff * attack_modifier
            defense = (resistance_coeff + proficiency_coeff) * life_coeff * defense_modifier
            return 0.6 * attack + 0.4 * defense
        elif self.name == "Archer":
            attack = (agility_coeff + proficiency_coeff) * strength_coeff * attack_modifier
            defense = (resistance_coeff + proficiency_coeff) * life_coeff * defense_modifier
            return 0.9 * attack + 0.1 * defense
        elif self.name == "Defender":
            attack = (agility_coeff + proficiency_coeff) * strength_coeff * attack_modifier
            defense = (resistance_coeff + proficiency_coeff) * life_coeff * defense_modifier
            return 0.1 * attack + 0.9 * defense
        elif self.name == "Infiltrator":
            attack = (agility_coeff + proficiency_coeff) * strength_coeff * attack_modifier
            defense = (resistance_coeff + proficiency_coeff) * life_coeff * defense_modifier
            return 0.8 * attack + 0.3 * defense

        def get_gen(self):
            return 1