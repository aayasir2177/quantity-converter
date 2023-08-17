weight = float(input("Enter your weight: "))
unit = input("For Kg to Lbs (Press K) \nFor Lbs to Kg (Press L) \n")

if unit.upper() == "K":
    lbs = str(weight * 2.2)
    print("Your weight in Pounds is " + lbs)
elif unit.upper() == "L":
    kg = str(weight / 2.2)
    print("Your weight in Kilograms is " + kg)
else:
    print("Invalid Input!")
