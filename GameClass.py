import pygame
from TicTacBoard import TicTacBoard
import sys
from enum import Enum


class GameState(Enum):
    IN_PROGRESS = 1
    WAITING_FOR_RESTART = 2


class GameClass:
    def __init__(self) -> None:
        # initialize the game
        pygame.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tic Tac Toe')
        self.bg_color = (0, 0, 0)  # black background
        self.line_color = (255, 255, 255)
        self.screen.fill(self.bg_color)
        self.state = GameState.IN_PROGRESS

        self.cell_width = self.width / 3
        self.cell_height = self.height / 3

        self.board = TicTacBoard()
        self.current_player = 'X'

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    if self.state == GameState.IN_PROGRESS:
                        row, col = self.get_grid_position(pos)
                        self.handle_move(row, col)

                    elif self.state == GameState.WAITING_FOR_RESTART:
                        self.restart_game()

            self.draw_board()
            pygame.display.flip()

    def handle_move(self, row, col):
        if self.board.is_valid_move(row, col):
            self.board.make_move(row, col, self.current_player)
            if self.board.check_winner(row, col) or self.board.is_full():
                self.state = GameState.WAITING_FOR_RESTART
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def start_game(self):
        self.state = GameState.IN_PROGRESS

    def update_game(self):
        # Update the game, handle player inputs, etc.
        pass

    def restart_game(self):
        self.screen.fill(self.bg_color)
        self.board = TicTacBoard()
        self.current_player = 'X'
        self.state = GameState.IN_PROGRESS
        print("Game restarted.")

    def get_grid_position(self, pos):
        """ Get grid position based on mouse click. """
        x, y = pos

        # Calculate row and column based on cell boundaries
        row = None
        col = None

        # Determine row
        for i in range(3):
            if y < self.cell_height * (i + 1):
                row = i
                break

        # Determine column
        for j in range(3):
            if x < self.cell_width * (j + 1):
                col = j
                break

        return row, col

    def draw_board(self):
        for i in range(1, 3):
            # Draw vertical lines
            pygame.draw.line(self.screen, self.line_color,
                             (self.cell_width * i, 0),
                             (self.cell_width * i, self.height), 5)
            # Draw horizontal lines
            pygame.draw.line(self.screen, self.line_color,
                             (0, self.cell_height * i),
                             (self.width, self.cell_height * i), 5)

        # Draw Xs and Os
        for row in range(3):
            for col in range(3):
                center_x = (col * self.cell_width) + (self.cell_width / 2)
                center_y = (row * self.cell_height) + (self.cell_height / 2)
                if self.board.grid[row][col] == 'X':
                    pygame.draw.line(self.screen, self.line_color,
                                     (center_x - 40, center_y - 40),
                                     (center_x + 40, center_y + 40), 5)
                    pygame.draw.line(self.screen, self.line_color,
                                     (center_x + 40, center_y - 40),
                                     (center_x - 40, center_y + 40), 5)
                elif self.board.grid[row][col] == 'O':
                    pygame.draw.circle(self.screen, self.line_color,
                                       (int(center_x), int(center_y)), 40, 5)

        if self.state == GameState.WAITING_FOR_RESTART:
            font = pygame.font.Font(None, 74)
            text = font.render(
                'Game Over. Click to restart.', True, (255, 0, 0))
            text_rect = text.get_rect(center=(self.width/2, self.height/2))
            self.screen.blit(text, text_rect)


g = GameClass()
g.run_game()
