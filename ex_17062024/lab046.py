# *arg examppple2

def shopping_list(*items):
    for home in items:
        print(home, end="\n")

kitchenGrocerry= shopping_list("milk", "bread", "butter")
washingMachine = shopping_list("detergent",  "soap")
food = shopping_list("cake", "icecream", "dates")

