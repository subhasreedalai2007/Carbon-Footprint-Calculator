# Carbon Footprint Calculator - All-in-One
def validate_number(value):
    try:
        value = float(value)
        if value < 0:
            return None
        return value
    except:
        return None

def validate_diet(diet):
    return diet.lower() if diet.lower() in ["veg", "non-veg"] else None

def get_user_input():
    print("\n--- Enter Your Household Data ---")
    
    while True:
        electricity = input("Electricity (kWh/month): ")
        electricity = validate_number(electricity)
        if electricity is not None:
            break
        print("❌ Invalid input! Enter a positive number.")

    while True:
        fuel = input("Fuel (litres or km/month): ")
        fuel = validate_number(fuel)
if fuel is not None:
            break
        print("❌ Invalid input! Enter a positive number.")

    while True:
        waste = input("Waste (kg/month): ")
        waste = validate_number(waste)
        if waste is not None:
            break
        print("❌ Invalid input! Enter a positive number.")

    diet = ""
    while validate_diet(diet) is None:
        diet = input("Diet (veg / non-veg): ")
    diet = diet.lower()

    return electricity, fuel, waste, diet

def calculate_carbon(electricity, fuel, waste, diet):
    results = {}
    results["Electricity"] = electricity * 0.82
    results["Fuel"] = fuel * 2.3
    results["Waste"] = waste * 1.5
    results["Diet"] = 300 if diet == "veg" else 600
    results["Total"] = sum(results.values())
    return results

def display_summary(results):
    print("\n====== Carbon Footprint Summary ======")
    for k, v in results.items():
        print(f"{k}: {v:.2f} kg CO2")
    print("=======================================")

def generate_recommendations(results):
    print("\n===== Recommendations =====")
    if results["Electricity"] > 200:
        print("- Reduce electricity usage.")
    if results["Fuel"] > 100:
        print("- Use public transport or walk more.")
    if results["Waste"] > 30:
        print("- Recycle and reduce household waste.")
    if results["Diet"] > 400:
        print("- Reduce meat consumption.")
    print("===========================\n")

def save_report(results):
    with open("carbon_report.txt", "w") as f:
        f.write("=== Carbon Footprint Report ===\n")
        for k, v in results.items():
            f.write(f"{k}: {v:.2f} kg CO2\n")
    print("✅ Report saved as carbon_report.txt")

def main():
    print("=== Carbon Footprint Calculator ===\n")
    electricity, fuel, waste, diet = get_user_input()
    results = calculate_carbon(electricity, fuel, waste, diet)
    display_summary(results)
    generate_recommendations(results)
    save_report(results)
    print("\n✅ Thank you for using the Carbon Footprint Calculator!\n")

if _name_ == "_main_":
    main()
