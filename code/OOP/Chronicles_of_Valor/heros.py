from character import Character


class Hero(Character):
    def __init__(self, name, health, attack_power, special_power):
        super().__init__(name, health, attack_power)
        self._special_power = special_power

    def use_special(self, other):
        other._health -= self._special_power
        return f"{self._name} uses special power on {other._name} for {self._special_power} damage!"
