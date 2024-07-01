class Distance(float):
    def __init__(self, value, unit) -> None:
        super().__init__(value)
        self.unit = unit


in_miles = Distance(4.2, "miles")
print(in_miles)
