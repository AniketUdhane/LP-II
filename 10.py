class nQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for x in range(n)] for y in range(n)]
        self.solutions = []
   
    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False
            for j in range(self.n):
                if (self.board[i][j] == 1 and
                   (abs(i - row) == abs(j - col))):
                    return False
        return True
   
    def solve(self, row):
        if row == self.n:
            solution = []
            for i in range(self.n):
                row_solution = ''
                for j in range(self.n):
                    if self.board[i][j] == 1:
                        row_solution += 'Q'
                    else:
                        row_solution += '.'
                solution.append(row_solution)
            self.solutions.append(solution)
            return True
       
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve(row + 1):
                    self.board[row][col] = 0
                else:
                    self.board[row][col] = 0
       
        return False
   
    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(row)
            print()
   
n = int(input("Enter the size of the chessboard: "))
queens = nQueens(n)
queens.solve(0)
queens.print_solutions()

'''

Objective:
 Understand and implement Constraint Satisfaction Problem using Branch and Bound for nqueens problem
 Understand and implement Constraint Satisfaction Problem using Backtracking for n-queens
problem

Outcome:
 Ability to choose an appropriate problem solving method and knowledge representation
technique

Software Required:
 Python

Theory:

 N Queen Problem using Backtracking:
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two
queens attack each other. For example, the following is a solution for the 4 Queen problem.

The expected output is a binary matrix that has 1s for the blocks where queens are placed. For
example, the following is the output matrix for the above 4 queen solution.

 Backtracking Algorithm:
The idea is to place queens one by one in different columns, starting from the leftmost
column. When we place a queen in a column, we check for clashes with already placed
queens. In the current column, if we find a row for which there is no clash, we mark this
row and column as part of the solution. If we do not find such a row due to clashes, then
we backtrack and return false.
1. Start in the leftmost column
2. If all queens are placed
 return true
3. Try all rows in the current column.
 Do following for every tried row.
a) If the queen can be placed safely in this row then mark this [row, column] as
part of the solution and recursively check if placing queen here leads to a
solution.
b) If placing the queen in [row, column] leads to a solution then return true.
c) If placing queen doesn't lead to a solution then unmark this [row, column]
(Backtrack) and go to step (a) to try other rows.
4. If all rows have been tried and nothing worked, return false to trigger
backtracking.

Conclusion: Thus we have Implement a solution for a Constraint Satisfaction Problem using Branch
and Bound and Backtracking for n-queens problem.

'''
