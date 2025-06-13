x=["Apple", "Mango", "Orange"], ["Blueberry", "Melon", "Jackfruit"],["Orange", "Mango", "Banana"]
for y in x:
    for z in y:
        if z == "Apple":
            print(z)


y=[[0, 1, 2], [2, 1, 0],[1, 2, 3]]
for ab in range(3):
    for z in range(3):
        print(f"value at index({ab},{z})is{y[ab][z]}")