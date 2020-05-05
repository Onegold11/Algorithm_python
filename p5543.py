burger = []
drink = []

for i in range(5):
    if i < 3:
        burger.append(int(input()))
    else:
        drink.append(int(input()))

# cheap_burger = min(burger)
# cheap_drink = min(drink)

cheap_burger = burger[0]
cheap_drink = drink[0]

for i in range(len(burger)):
    if burger[i] < cheap_burger:
        cheap_burger = burger[i]
for i in range(len(drink)):
    if drink[i] < cheap_drink:
        cheap_drink = drink[i]

print(cheap_burger + cheap_drink - 50)