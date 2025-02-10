import sys  # for terminating the program using sys.exit()
import math  # for computing mathematical functions

def gold_triangles(n):
    return_value = []  # to store found triplets
    for a in range(1, n): 
        for b in range(a, n): 
            c = math.isqrt(a ** 2 + b ** 2)  # to find the square root (to speed up iteration)
            if c < n and a ** 2 + b ** 2 == c ** 2:
                return_value.append((a, b, c))  # store triplets in the list
    return return_value  # return the list of found triplets

def main():
    try:
        n = int(input("Enter an integer n: ").strip())  # prompt the user for an integer input
        print(gold_triangles(n))
    except ValueError:  # when an invalid input is entered
        print("Invalid input. Please enter an integer.")
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())  # calls the main function and terminates the program using sys.exit()
