from character import Character


class Villain(Character):
    def __init__(self, name, health, attack_power, evil_power):
        super().__init__(name, health, attack_power)
        self._evil_power = evil_power

    def use_evil_power(self, other):
        other._health -= self._evil_power
        return f"{self._name} uses evil power on {other._name} for {self._evil_power} damage!"
