def display_summary(results):
    print("\n====== Carbon Footprint Summary ======")

    for k, v in results.items():
        print(f"{k}: {v:.2f} kg CO2")

    print("=======================================\n")