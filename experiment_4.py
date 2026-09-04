# Experiment No. 4
# Title: Calculate the nth Fibonacci Number Efficiently

def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


def main():
    n = int(input("Enter the value of n: "))

    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        result = fibonacci_iterative(n)
        print(f"The {n}th Fibonacci number is: {result}")


if __name__ == "__main__":
    main()