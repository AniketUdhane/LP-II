# Implement a solution for a Constraint Satisfaction Problem
# using Branch and Bound 

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def branch_and_bound_knapsack(items, capacity):
    n = len(items)
    best_value = 0
    best_selection = [0] * n

    def knapsack_recursive(curr_value, curr_weight, curr_selection, curr_index):
        nonlocal best_value, best_selection

        if curr_index >= n:
            if curr_value > best_value:
                best_value = curr_value
                best_selection = curr_selection.copy()
            return

        if curr_weight + items[curr_index].weight <= capacity:
            # Include the current item
            curr_selection[curr_index] = 1
            knapsack_recursive(
                curr_value + items[curr_index].value,
                curr_weight + items[curr_index].weight,
                curr_selection,
                curr_index + 1,
            )

        # Exclude the current item
        curr_selection[curr_index] = 0
        knapsack_recursive(curr_value, curr_weight, curr_selection, curr_index + 1)

    knapsack_recursive(0, 0, [0] * n, 0)

    return best_value, best_selection


# Example usage
items = [Item(2, 12), Item(1, 10), Item(3, 20), Item(2, 15)]
capacity = 5

best_value, best_selection = branch_and_bound_knapsack(items, capacity)

print("Best value:", best_value)
print("Best selection:", best_selection)


# Python implementation of the n-queens problem using backtracking:

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def solve(self):
        if not self.solve_util(0):
            print("No solution exists")
        else:
            self.print_board()

    def solve_util(self, col):
        if col >= self.n:
            return True

        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1

                if self.solve_util(col + 1):
                    return True

                self.board[row][col] = 0

        return False

    def is_safe(self, row, col):
        # Check if the current position is attacked by any previous queen

        # Check row
        for c in range(col):
            if self.board[row][c] == 1:
                return False

        # Check upper diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if self.board[r][c] == 1:
                return False
            r -= 1
            c -= 1

        # Check lower diagonal
        r, c = row, col
        while r < self.n and c >= 0:
            if self.board[r][c] == 1:
                return False
            r += 1
            c -= 1

        return True

    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))


# Example usage
n = 8  # Number of queens
queens = NQueens(n)
queens.solve()
