class Weapon:
    def __init__(self, name, damage):
        self._name = name
        self._damage = damage

    def enhance_attack(self, character):
        character._attack_power += self._damage

    def __str__(self):
        return f"{self._name} - Damage: {self._damage}"
