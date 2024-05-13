def main():
    dollars = float("How much was the meal? ")).strip('$').round(3)
    percent = float("What percentage would you like to tip? ")).strip('%').round(3)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")




main()
