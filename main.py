from enemies.bat import Bat
from characters.knight import Knight

class MainGame:

    def __init__(self):
        self.player = Knight(23, "Barth")
        self.enemy = Bat(3)
        
    def run(self) -> None:
        while(self.player.is_alive()):
            # ...
            self.player.list_weapons()
            self.player.choose_weapon(1)
            self.player.use_weapon(self.enemy)
            self.enemy.attack(self.player)

if __name__ == "__main__":
    game = MainGame()
    game.run()
