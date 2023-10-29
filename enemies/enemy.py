from typing import Protocol
from enum import Enum, auto

class EnemyType(Enum):
    FLYING: int = auto()
    GROUND: int = auto()
    UNDERGROUND: int = auto()


class Enemy(Protocol):
    health: int
    damage: int
    enemy_type: Enum

    def attack(self, player):
        ...

    def take_damage(self, dmg: int):
        ...
