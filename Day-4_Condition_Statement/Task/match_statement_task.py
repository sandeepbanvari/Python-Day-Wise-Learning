# Practice Task: Food delivery app

food = input("Enter food item: ").capitalize()
match food:
    case "Pizza":
        print("Price: ₹299")
    case "Burger":
        print("Price: ₹149")
    case "Biryani":
        print("Price: ₹249")
    case "Dosa":
        print("Price: ₹99")
    case _:
        print("Not Available")