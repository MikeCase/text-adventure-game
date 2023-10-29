from typing import List, Protocol
from weapons.weapons import Weapon

class Player(Protocol):
    age: int
    health: int
    name: str
    weapons: List[Weapon]

    def take_damage(self, dmg: int) -> None:
        ...

    def use_weapon(self, enemy) -> int:
        ...

    def list_weapons(self) -> None:
        ...
    
    def choose_weapon(self, weapon_id: int) -> None:
        ...

    def is_alive(self) -> bool:
        ...

