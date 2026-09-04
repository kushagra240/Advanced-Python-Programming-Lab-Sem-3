"""Experiment No. 6: Solve the 0/1 Knapsack problem using dynamic programming."""

from functools import lru_cache


def _validate_input(values: list[int], weights: list[int], capacity: int) -> None:
    """Validate the data shared by both knapsack implementations."""
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights must be non-negative")


def knapsack_bottom_up(values: list[int], weights: list[int], capacity: int) -> int:
    """Return the maximum value using iterative tabulation.

    Time complexity: O(n * capacity)
    Space complexity: O(n * capacity)
    """
    _validate_input(values, weights, capacity)
    item_count = len(values)
    table = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    for item in range(1, item_count + 1):
        value = values[item - 1]
        weight = weights[item - 1]
        for current_capacity in range(capacity + 1):
            table[item][current_capacity] = table[item - 1][current_capacity]
            if weight <= current_capacity:
                table[item][current_capacity] = max(
                    table[item][current_capacity],
                    table[item - 1][current_capacity - weight] + value,
                )

    return table[item_count][capacity]


def knapsack_top_down(values: list[int], weights: list[int], capacity: int) -> int:
    """Return the maximum value using recursion with memoization.

    Time complexity: O(n * capacity)
    Space complexity: O(n * capacity), including the recursion stack.
    """
    _validate_input(values, weights, capacity)

    @lru_cache(maxsize=None)
    def solve(item_count: int, remaining_capacity: int) -> int:
        if item_count == 0 or remaining_capacity == 0:
            return 0

        item_index = item_count - 1
        if weights[item_index] > remaining_capacity:
            return solve(item_index, remaining_capacity)

        exclude_item = solve(item_index, remaining_capacity)
        include_item = values[item_index] + solve(
            item_index, remaining_capacity - weights[item_index]
        )
        return max(exclude_item, include_item)

    return solve(len(values), capacity)


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    bottom_up_result = knapsack_bottom_up(values, weights, capacity)
    top_down_result = knapsack_top_down(values, weights, capacity)

    print(f"Values: {values}")
    print(f"Weights: {weights}")
    print(f"Capacity: {capacity}")
    print(f"Maximum value (bottom-up): {bottom_up_result}")
    print(f"Maximum value (top-down): {top_down_result}")
