def generate_recommendations(results):
    print("===== Recommendations =====")

    if results["Electricity"] > 200:
        print("- Reduce electricity usage.")

    if results["Fuel"] > 100:
        print("- Use public transport.")

    if results["Waste"] > 30:
        print("- Recycle more waste.")

    if results["Diet"] > 400:
        print("- Reduce meat consumption.")

    print("===========================\n")