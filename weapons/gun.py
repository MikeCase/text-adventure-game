from enum import Enum
from .weapons import WeaponType

class Gun:
    def __init__(self) -> None:
        self.damage: int = 15
        self.weapon_type: Enum = WeaponType.RANGED
        self.shots: int = 6

    def deal_damage(self) -> int:
        return self.damage
    
    def take_damage(self) -> None:
        self.shots -= 1

    def __repr__(self) -> str:
        return "Gun"