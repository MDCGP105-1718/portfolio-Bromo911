bottle_number = 0


for n in range(99,0,-1):
    if bottle_number == 2:
        print(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer.")
        bottle_number = n - 1
        print(f"Take one down, pass it around, {bottle_number} bottle of beer on the wall…")
    if bottle_number == 1:
        print ("1 bottle of beer on the wall, 1 bottle of beer! So take it down, pass it around, no more bottles of beer on the wall!")
        bottle_number = n - 1
        break
    bottle_number = n
    print(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer.")
    bottle_number = n - 1
    print(f"Take one down, pass it around, {bottle_number} bottles of beer on the wall…")
