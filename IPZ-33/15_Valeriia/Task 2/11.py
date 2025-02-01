def find_capital(coords): #Find the optimal capital location that minimizes the sum of Manhattan distances to all given cities.
    x_coords = sorted([x for x, y in coords])  # Sort all x-coordinates
    y_coords = sorted([y for x, y in coords])  # Sort all y-coordinates

    # Find median of x and y separately
    median_x = x_coords[len(x_coords) // 2]  
    median_y = y_coords[len(y_coords) // 2]  

    return median_x, median_y

# Read input from user
n = int(input("Ввеіть кіллкість міст: "))
cities = []

print("Введіть координати міст (x y): ")
for _ in range(n):
    x, y = map(int, input().split())
    cities.append((x, y))

# Compute and print the capital's coordinates
capital = find_capital(cities)
print("Оптимальні координати столиці: ", capital)
