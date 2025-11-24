# input_module.py

from validation import validate_number, validate_diet

def ask_number(prompt):
    while True:
        value = input(prompt)
        valid = validate_number(value)
        if valid is not None:
            return valid
        print("Invalid input! Enter a positive number.")

def get_user_input():
    print("\n--- Enter Your Household Data ---")

    electricity = ask_number("Electricity (kWh/month): ")
    fuel = ask_number("Fuel (litres or km/month): ")
    waste = ask_number("Waste (kg/month): ")

    diet = ""
    while not validate_diet(diet):
        diet = input("Diet (veg / non-veg): ")
    diet = diet.lower()

    return electricity, fuel, waste, diet