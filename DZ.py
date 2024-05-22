class Hero():
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack_other(self, other):
        other.health -= self.attack_power
        print(f"{self.name} ударил {other.name}  с {self.attack_power} уроном.")
        print(f"{other.name} получил увечье, осталось здоровья {other.health}, у {other.name} упадок сил.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack_other(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} победил {self.computer.name}")
                break
            self.computer.attack_other(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} победил {self.player.name}")
                break


player = Hero("Тесей")
computer = Hero("Минотавр")
game = Game(player, computer)
game.start()


