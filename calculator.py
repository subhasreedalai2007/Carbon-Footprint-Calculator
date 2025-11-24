class CarbonCalculator:
    def __init__(self, electricity, fuel, waste, diet):
        self.electricity = electricity
        self.fuel = fuel
        self.waste = waste
        self.diet = diet

    def calc_electricity(self):
        return self.electricity * 0.82

    def calc_fuel(self):
        return self.fuel * 2.3

    def calc_waste(self):
        return self.waste * 1.5

    def calc_diet(self):
        return 300 if self.diet == "veg" else 600

    def calculate_total(self):
        return {
            "Electricity": self.calc_electricity(),
            "Fuel": self.calc_fuel(),
            "Waste": self.calc_waste(),
            "Diet": self.calc_diet(),
            "Total": (
                self.calc_electricity()
                + self.calc_fuel()
                + self.calc_waste()
                + self.calc_diet()
            )
        }