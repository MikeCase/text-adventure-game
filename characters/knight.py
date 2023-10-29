from weapons.weapons import Weapon
from weapons.gun import Gun
from weapons.sword import Sword
from typing import List

class Knight:
    
    def __init__(self, age: int, name: str) -> None:
        self.weapons: List[Weapon] = [Sword(), Gun()]
        self.age: int = age
        self.name: str = name
        self.health: int = 100
        self.chosen_weapon: int = 0

    def take_damage(self, dmg: int) -> None:
        self.health -= dmg
        print(self.health)

    def use_weapon(self, enemy) -> int:
        print(f"{self.name} attacks {enemy} dealing {self.weapons[self.chosen_weapon].damage} damage")
        return enemy.take_damage(self.weapons[self.chosen_weapon].deal_damage())

    def list_weapons(self) -> None:
        for idx, weapon in enumerate(self.weapons):
            print(f"{idx} - {weapon}")
    
    def choose_weapon(self, weapon_id: int) -> None:
        self.chosen_weapon = weapon_id
    
    def is_alive(self) -> bool:
        if self.health >= 0:
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"{self.name}"