class TicTacBoard:
    def __init__(self):
        self.grid = [[None for _ in range(3)] for _ in range(3)]

    def print_board(self):
        """For testing and debugging purposes"""
        for row in self.grid:
            print(row)

    def make_move(self, row, col, player_symbol):
        if self.is_valid_move(row, col):
            self.grid[row][col] = player_symbol
            self.print_board()
            if self.check_winner(row, col):
                print("Game over!")

    def check_winner(self, row, col):
        player = self.grid[row][col]
        if player is None:
            return False

        # Check the row and column
        if all([cell == player for cell in self.grid[row]]) or all([self.grid[r][col] == player for r in range(3)]):
            return True

        # Check diagonals
        if row == col and all([self.grid[i][i] == player for i in range(3)]):
            return True
        if row + col == 2 and all([self.grid[i][2-i] == player for i in range(3)]):
            return True

        return False

    def is_valid_move(self, row, col) -> bool:
        if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
            return self.grid[row][col] == None
        else:
            return False

    def is_full(self):
        return all([self.grid[row][col] != None for row in range(3) for col in range(3)])

    def get_grid(self):
        return self.grid
