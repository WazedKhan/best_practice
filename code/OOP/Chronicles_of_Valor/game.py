class Game:
    def __init__(self, hero, villain):
        self._hero = hero
        self._villain = villain

    def start_battle(self):
        print(
            f"The battle begins between {self._hero._name} and {self._villain._name}!\n"
        )
        while self._hero.is_alive() and self._villain.is_alive():
            self._hero.attack(self._villain)
            if not self._villain.is_alive():
                print(f"{self._villain._name} is defeated! {self._hero._name} wins!")
                break
            self._villain.attack(self._hero)
            if not self._hero.is_alive():
                print(f"{self._hero._name} is defeated! {self._villain._name} wins!")
                break
            print(self._hero)
            print(self._villain)
            print("=================================================================")
            print("\n")
