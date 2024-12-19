def invest(amount, rate, years):
    for year in range(years):
        print(f"year {year+1}: ${(amount + amount * rate):.2f}")
        amount = amount + amount * rate

invest(100, 0.05, 4)
