def save_report(results):
    with open("carbon_report.txt", "w") as f:
        for k, v in results.items():
            f.write(f"{k}: {v:.2f} kg CO2\n")

    print("Report saved as carbon_report.txt\n")