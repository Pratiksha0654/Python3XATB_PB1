#Place an order for starbucks with arg

def place_order(size, drink, flavor,temp):
    for i in size,  drink, flavor, temp:
        print(i, end="\n")


Order1 = place_order(size="large", drink="latte", flavor="mocha", temp="hot")
Order2 = place_order(size="small", drink="capachino", flavor="vanila", temp="cold")
print(Order1, Order2)

