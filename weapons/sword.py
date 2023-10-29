from enum import Enum
from .weapons import WeaponType

class Sword:
    def __init__(self) -> None:
        self.damage: int = 10
        self.weapon_type: Enum = WeaponType.IMPACT
        self.shots: int = 75

    def deal_damage(self) -> int:
        return self.damage
    
    def take_damage(self) -> None:
        self.shots -= 2

    def __repr__(self) -> str:
        return "Sword"