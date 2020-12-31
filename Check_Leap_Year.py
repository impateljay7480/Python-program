y = int(input("Enter a Year to check a leap year or not:"))

if (y % 4) == 0:
    if (y % 100) == 0:
        if (y % 400) == 0:
            print(f"{y} is a leap Year.")
        else:
            print(f"{y} is not a leap Year.")
    else:
        print(f"{y} is a leap year.")
else:
    print(f"{y} is not a leap Year.")
