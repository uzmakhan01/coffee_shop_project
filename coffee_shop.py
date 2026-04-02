# classes (OOP)

class Coffee:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.coffees = []

    def add_coffee(self, coffee):
        self.coffees.append(coffee)

    def calc_total(self):
        total = 0
        for coffee in self.coffees:
            total += coffee.price
        return total
    

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

    def view_orders(self):
        for order in self.orders:
            print(f"Order for {order.customer_name}:")
            for coffee in order.coffees:
                print(f"  {coffee.size} {coffee.name} - ${coffee.price}")
            print(f"Total: ${order.calc_total()}\n")


# Coffee menu
menu = [
    Coffee("Latte", "Small", 1.5),
    Coffee("Latte", "Medium", 2.5),
    Coffee("Latte", "Large", 3.5),
    Coffee("Espresso", "Small", 2.0),
    Coffee("Espresso", "Medium", 3.0),
    Coffee("Espresso", "Large", 4.0),
    Coffee("Cappuccino", "Small", 2.5),
    Coffee("Cappuccino", "Medium", 3.5),
    Coffee("Cappuccino", "Large", 4.5),
]


# 1. Get customer name
customer_name = input("Enter your name: ")
customer1 = Customer(customer_name)


# 2. Create an order
order1 = Order(customer_name)


# 3. Show menu
print("\nMenu:")
for i, coffee in enumerate(menu, 1):
    print(f"{i}. {coffee.size} {coffee.name} - ${coffee.price}")


# 4. Take coffee orders
while True:
    choice = input("Enter the number of coffee to add (or type 'done' to finish): ")

    if choice.lower() == "done":
        break

    if choice.isdigit():
        coffee_number = int(choice)
        if 1 <= coffee_number <= len(menu):
            selected_coffee = menu[coffee_number - 1]
            order1.add_coffee(selected_coffee)
            print("Added", selected_coffee.size, selected_coffee.name)
        else:
            print("Invalid number, choose from the menu.")
    else:
        print("Invalid input, please enter a number or 'done'.")

# 5. Place order for customer
customer1.place_order(order1)

# 6. Display the order
customer1.view_orders()