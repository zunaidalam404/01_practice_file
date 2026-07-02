Menu = {
    "Salad": 40,
    "Burger": 350,
    "Pizza": 500,
    "Kabab 4 piece": 80,
    "Chicken Tikka": 580,
    "Full Mutton": 1200,
    "Malai Kofta": 430
}

print("WELCOME TO MY RESTAURANT")
print("----HAPPY CUSTOMER IS MY FIRST GOAL----")
print("Menu:", Menu)

# Customer name
name = input("Enter your name: ")

# Order input
Enter_Order = input("Enter your Order (comma separated if multiple): ")

Bill = 0
Order = []

items = Enter_Order.split(",")

for item in items:
    item = item.strip()
    if item in Menu:
        Bill += Menu[item]
        Order.append(item)
    else:
        print(f"Sorry, {item} is not available in my restaurant.")
        # Option to add new item
        choice = input(f"Do you want to add {item} to menu? (yes/no): ")
        if choice.lower() == "yes":
            price = int(input(f"Enter price for {item}: "))
            Menu[item] = price
            print(f"{item} added to menu with price {price}.")

print("\n---- BILL ----")
print(f"Customer Name: {name}")
print(f"Your Order: {', '.join(Order)}")
print(f"Total price: {Bill}")

