MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    # "water": 0,
    # "milk": 0,
    # "coffee": 0,
}
money = 0
# TODO: 1. create a function to print report
def print_report(res, mon):
    print(f"Water: {res["water"]}ml")
    print(f"Milk: {res["milk"]}ml")
    print(f"Coffee: {res["coffee"]}g")
    print(f"Money: ${mon}")

# TODO: 2. create a function to check resources sufficienty
def check_resources(res, dri):
    for i in MENU[dri]["ingredients"]:
        if res[i] < MENU[dri]["ingredients"][i]:
            print(f"Sorry there is not enough {i}")
            return False
        else:
            return True

# TODO: 3. create a function to process coin
def process_coins():
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("Nickles: "))
    pennies = float(input("Pennies: "))
    mon_ins = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return mon_ins

# TODO: 4. create a function to check transaction successful?
def check_transaction(mon_mac, mon_ins, dri):
    if mon_ins < MENU[dri]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        mon_mac += MENU[dri]["cost"]
        print(f"Here is ${round(mon_ins - MENU[dri]["cost"], 2)} dollars in change.")
        return True, mon_mac
# TODO: 5. create a function to make coffee
def make_coffee(res, dri, mon_mac):
        for i in MENU[dri]["ingredients"]:
            res[i] -= MENU[dri]["ingredients"][i]
        print_report(res, mon_mac)
        print(f"Here is your {dri}. Enjoy!")
        return res

def main(res, mon_mac):
    sel = ""
    while sel != "off":
        sel = input("What would you like?").lower()
        if sel == "report":
            print_report(res, mon_mac)
        elif sel == "espresso" or sel == "latte" or sel == "cappuccino":
            if_resource = check_resources(res, sel)
            if not if_resource:
                continue
            mon_ins = process_coins()
            if_transaction, mon_mac = check_transaction(mon_mac, mon_ins, sel)
            if if_transaction and if_resource:
                res = make_coffee(res, sel, mon_mac)


main(resources, money)




