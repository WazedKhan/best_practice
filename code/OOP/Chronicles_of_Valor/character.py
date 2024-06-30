class Character:
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        self._name = name
        self._health = health
        self._attack_power = attack_power

    def attack(self, other):
        other._health -= self._attack_power
        return True

    def is_alive(self):
        return self._health > 0

    def __str__(self):
        return f"{self._name} - Health: {self._health}"
