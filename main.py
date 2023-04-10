def solve_sudoku(puzzle):
    """Solves a given Sudoku puzzle using backtracking algorithm

    Args:
        puzzle (list): 9x9 list representing a Sudoku puzzle, where 0 means 'empty'
    """

    def is_valid(row, col, num):
        """Checks whether or not a number is valid in a coordinate

        Args:
            row (int): row for number
            col (int): column for number
            num (int): number to check
        """

        # Check row
        if num in puzzle[row]:
            return False

        for i in range(9):
            if puzzle[i][col] == num:
                return False


        # Check square
        starting_row = row // 3
        starting_col = col // 3

        for row in range(starting_row * 3, starting_row * 3 + 3):
            for col in range(starting_col * 3, starting_col * 3 + 3):
                if puzzle[row][col] == num:
                    return False

        return True

    def print_puzzle():
        """Prints the puzzle to console
        """
        for line in puzzle:
            print(line)

        print('--------------------------')

    def find_empty():
        """Find the next empty coordinate

        Returns:
            tuple: Tuple of location (row, col). None if no coordinate is empty.
        """
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    return row, col
        return None


    def backtrack():
        """The actual solving algorithm through recursion

        Returns:
            bool: Whether or not puzzle could be solved
        """

        empty = find_empty()
        if empty:
            row, col = empty
        else:
            return True

        for i in range(1, 10):
            if is_valid(row, col, i):
                puzzle[row][col] = i

                if backtrack():
                    return True

            puzzle[row][col] = 0

        return False


    return backtrack()


if __name__ == '__main__':
    puzzle = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]

    if solve_sudoku(puzzle):
        for line in puzzle:
            print(line)
    else:
        print("Puzzle could not be solved")

