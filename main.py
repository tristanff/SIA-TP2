from src.character import Warrior,Archer,Defender,Infiltrator


my_warrior = Warrior(height=1.75, strength_items=52.5, agility_items=22.5, proficiency_items=31.0, resistance_items=21.0, life_items=23.0)
my_archer = Archer(height=1.62, strength_items=21.0, agility_items=52.0, proficiency_items=31.0, resistance_items=20.5, life_items=25.5)
my_defender = Defender(height=1.93, strength_items=51.0, agility_items=20.0, proficiency_items=21.0, resistance_items=50.0, life_items=8.0)
my_infiltrator = Infiltrator(height=1.65, strength_items=31.5, agility_items=41.0, proficiency_items=41.5, resistance_items=21.0, life_items=15.0)


print("Warrior Performance : ", my_warrior.performance())
print("Archer Performance : ", my_archer.performance())
print("Defender Perfomance : ", my_defender.performance())
print("Infiltrator Perfomance : ", my_infiltrator.performance())



#Basic function to create random personnages with items = 150 - 5 by 5 for each items
def character_Factory():
    personnages = []

    for strength_items in range(0, 151, 5):
        for agility_items in range(0, 151 - strength_items, 5):
            for proficiency_items in range(0, 151 - strength_items - agility_items, 5):
                for resistance_items in range(0, 151 - strength_items - agility_items - proficiency_items, 5):
                    life_items = 150 - (strength_items + agility_items + proficiency_items + resistance_items)
                    if life_items % 5 == 0:
                        height = 1.7  #Default value for testing
                        personnages.append(Warrior(height, strength_items, agility_items, proficiency_items, resistance_items, life_items))
                        personnages.append(Archer(height, strength_items, agility_items, proficiency_items, resistance_items, life_items))
                        personnages.append(Infiltrator(height, strength_items, agility_items, proficiency_items, resistance_items, life_items))
                        personnages.append(Defender(height, strength_items, agility_items, proficiency_items, resistance_items, life_items))

    return personnages

personnages = character_Factory()


best_personnage = max(personnages, key=lambda x: x.performance())
for idx, personnage in enumerate(personnages):
    print(f"Personnage {idx+1} ({type(personnage).__name__}):")
    print(f"  - Strength Items: {personnage.strength_items}")
    print(f"  - Agility Items: {personnage.agility_items}")
    print(f"  - Proficiency Items: {personnage.proficiency_items}")
    print(f"  - Resistance Items: {personnage.resistance_items}")
    print(f"  - Life Items: {personnage.life_items}")
    print(f"  - Performance : {personnage.performance()}")
    print()


best_personnage = max(personnages, key=lambda x: x.performance())

print(f"Best_Personnage {idx + 1} ({type(best_personnage).__name__}):")
print(f"  - Strength Items: {best_personnage.strength_items}")
print(f"  - Agility Items: {best_personnage.agility_items}")
print(f"  - Proficiency Items: {best_personnage.proficiency_items}")
print(f"  - Resistance Items: {best_personnage.resistance_items}")
print(f"  - Life Items: {best_personnage.life_items}")
print(f"  - Performance : {best_personnage.performance()}")



