menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee

map_coffee = map(find_coffee, menu)
print(map_coffee)

for i in map_coffee:
    print(i)

filtered_list = filter(find_coffee, menu)
for i in filtered_list:
    print("\n", i)
