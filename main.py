MENU = {
    "espresso" : {
        "ingredients" : {
            "coffee" : 18,
            "water": 50,
        },
        "cost" : 15,
    },
    "latte" : {
        "ingredients" : {
            "milk" : 150,
            "coffee" : 24,
            "water" : 200,
        },
        "cost" : 25,
    },
    "cappuccino" : {
        "ingredients" : {
            "milk" : 100,
            "coffee" : 24,
            "water" : 250,
        },
        "cost" : 40,
    },
}

profit = 0

resources = {
    "water": 400,
    "milk": 300,
    "coffee": 150,
}

def resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from inserted coins."""
    print("please insert coins.")
    total = int(input("how many five rupees : ")) * 5
    total += int(input("how many ten rupees : ")) * 10
    total += int(input("how many twenty rupees : ")) * 20
    total += int(input("how many fifty rupees : ")) * 50
    total += int(input("how many hundred rupees : ")) * 100
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = int(money_received - drink_cost)
        print(f"Here is your change ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink {drink_name} ☕️. Enjoy!")

is_on = True
while is_on:
    choice = input("What would you like ? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Milk :{resources['milk']}ml")
        print(f"Water :{resources['water']}ml")
        print(f"Coffee :{resources['coffee']}g")
        print(f"Profit : ${profit}")
    else:
        drink = MENU[choice]
        if resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])


