## This script demonstrates the use of functions to perform mathematical operations.
def square(a):
    return a * a

def cube(x):
    return x * x * x

# This is the main function that calls the square and cube functions.
def main():
    result1 = square(3)
    result2 = cube(4.0)

    print("Result of square:", result1)
    print("Result of cube:", result2)

if __name__ == "__main__":
    main()
    