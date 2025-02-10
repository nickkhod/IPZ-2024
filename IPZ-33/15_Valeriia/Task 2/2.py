def pascal_triangle(n):  # function declaration
    triangle = []  # variable to store the triangle
    
    for i in range(n):  # loop to construct rows
        row = [1] * (i + 1)  # creating each row
        
        for j in range(1, i):  # filling in the internal elements
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        triangle.append(row)  # adding the row to the triangle
    return triangle

n = int(input("Кількість рядків для т.Паскаля: "))  # request to enter the number of rows
triangle = pascal_triangle(n)  # function call to build the triangle

for row in triangle:  # loop to print each row
    print(row)
