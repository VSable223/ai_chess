import tkinter as tk

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chess Game")
        self.board = self.create_board()
        self.is_white_turn = True
        self.selected_square = None

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.new_game_button = tk.Button(self.root, text="New Game", command=self.new_game, height=2, width=10)
        self.new_game_button.pack(pady=10)

        self.setup_initial_position()
        self.render_board()

    def create_board(self):
        return [[None for _ in range(8)] for _ in range(8)]

    def setup_initial_position(self):
        white_pieces = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        black_pieces = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']

        for col in range(8):
            self.board[0][col] = ('black', black_pieces[col])
            self.board[1][col] = ('black', '♟')
            self.board[6][col] = ('white', '♟')
            self.board[7][col] = ('white', white_pieces[col])

    def render_board(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        for row in range(8):
            for col in range(8):
                color = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"
                square = tk.Button(
                    self.board_frame,
                    text=self.board[row][col][1] if self.board[row][col] else '',
                    font=("Arial", 24),
                    width=4,
                    height=2,
                    bg=color,
                    fg="white" if self.board[row][col] and self.board[row][col][0] == "white" else "black",
                    command=lambda r=row, c=col: self.handle_square_click(r, c)
                )
                square.grid(row=row, column=col)

    def handle_square_click(self, row, col):
        if self.selected_square:
            from_row, from_col = self.selected_square
            piece = self.board[from_row][from_col]

            if piece and (self.board[row][col] is None or self.board[row][col][0] != piece[0]):
                self.board[row][col] = piece
                self.board[from_row][from_col] = None
                self.is_white_turn = not self.is_white_turn

            self.selected_square = None
            self.render_board()
        else:
            if self.board[row][col]:
                self.selected_square = (row, col)

    def new_game(self):
        self.board = self.create_board()
        self.setup_initial_position()
        self.render_board()


if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()
