from heros import Hero
from villain import Villain
from weapon import Weapon
from game import Game

# Example Usage
hero = Hero(name="Arthur", health=100, attack_power=20, special_power=50)
villain = Villain(name="Mordred", health=100, attack_power=15, evil_power=45)
weapon = Weapon(name="Excalibur", damage=10)
weapon.enhance_attack(hero)

game = Game(hero, villain)
game.start_battle()
