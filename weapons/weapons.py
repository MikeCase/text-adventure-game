from enum import Enum, auto
from typing import Protocol

class WeaponType(Enum):
    IMPACT = auto()
    ELECTRICAL = auto()
    RANGED = auto()


class Weapon(Protocol):
    def deal_damage(self) -> int:
        ...

    def take_damage(self, other) -> None:
        ...
