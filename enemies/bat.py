from .enemy import EnemyType
from enum import Enum

class Bat:
    def __init__(self, damage: int) -> None:
        self.health: int = 100
        self.damage: int = 5
        self.enemy_type: Enum = EnemyType.FLYING

    def attack(self, player) -> int:
        print(f"{self} attacks {player} dealing {self._deal_damage()} damage")
        return player.take_damage(self._deal_damage())
    
    def _deal_damage(self) -> int:
        return self.damage
    
    def take_damage(self, dmg: int) -> None:
        self.health -= dmg
        print(self.health)

    def is_alive(self) -> bool:
        if self.health >= 0:
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return "Bat"