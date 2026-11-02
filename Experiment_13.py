import threading


def count_numbers():
    for number in range(1, 6):
        print(f"Count: {number}")


def calculate_squares():
    for number in range(1, 6):
        print(f"Square of {number}: {number ** 2}")


def calculate_cubes():
    for number in range(1, 6):
        print(f"Cube of {number}: {number ** 3}")


def main():
    tasks = [count_numbers, calculate_squares, calculate_cubes]
    threads = [threading.Thread(target=task) for task in tasks]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("All tasks completed.")


if __name__ == "__main__":
    main()
