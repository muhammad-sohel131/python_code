import customtkinter as ctk
import time
from solver import solve, is_valid, solve_csp
from utils import generate_board

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class SudokuGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🤖 AI Sudoku Solver")
        self.geometry("1000x740")
        self.strategy = "Backtracking"
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.start_time = None

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.left_frame = ctk.CTkFrame(self.main_frame)
        self.left_frame.grid(row=0, column=0, padx=10, sticky="n")

        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.grid(row=0, column=1, padx=10, sticky="n")

        self.grid_frame = ctk.CTkFrame(self.left_frame)
        self.grid_frame.pack(pady=10)
        self.create_grid()

        self.button_frame = ctk.CTkFrame(self.left_frame)
        self.button_frame.pack(pady=5)
        self.create_buttons()

        self.message_label = ctk.CTkLabel(self.left_frame, text="🧠 Ready", text_color="blue", font=ctk.CTkFont(size=16))
        self.message_label.pack(pady=6)

        self.timer_label = ctk.CTkLabel(self.left_frame, text="⏱ Timer: 0s", font=ctk.CTkFont(size=14))
        self.timer_label.pack(pady=2)
        self.update_timer()

        self.explanation_box = ctk.CTkTextbox(self.left_frame, width=500, height=160)
        self.explanation_box.pack(pady=5)
        self.explanation_box.insert("1.0", "📘 Explanation log will appear here.\n")
        self.explanation_box.configure(state="disabled")

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                var = ctk.StringVar()
                entry = ctk.CTkEntry(self.grid_frame, width=45, height=45, font=ctk.CTkFont(size=18),
                                     justify="center", textvariable=var)
                entry.grid(row=i, column=j, padx=1, pady=1)
                var.trace_add("write", lambda *args, r=i, c=j: self.validate_cell(r, c))
                self.entries[i][j] = entry

    def create_buttons(self):
        self.difficulty_var = ctk.StringVar(value="Easy")
        ctk.CTkOptionMenu(self.button_frame, variable=self.difficulty_var, values=["Easy", "Medium", "Hard"]).grid(row=0, column=0, padx=5)
        ctk.CTkButton(self.button_frame, text="🎲 Generate", command=self.generate_puzzle, width=100).grid(row=0, column=1, padx=5)
        ctk.CTkButton(self.button_frame, text="🧠 Solve", command=self.solve_sudoku, width=100).grid(row=0, column=2, padx=5)
        ctk.CTkButton(self.button_frame, text="💡 Hint", command=self.give_hint, width=100).grid(row=0, column=3, padx=5)
        ctk.CTkButton(self.button_frame, text="🛠 Strategy", command=self.toggle_strategy, width=120).grid(row=0, column=4, padx=5)
        ctk.CTkButton(self.button_frame, text="📖 Explain Move", command=self.explain_move, width=140).grid(row=0, column=6, padx=5)

   

    def update_timer(self):
        if self.start_time:
            elapsed = int(time.time() - self.start_time)
            self.timer_label.configure(text=f"⏱ Timer: {elapsed}s")
        self.after(1000, self.update_timer)

    def get_board(self):
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                self.board[i][j] = int(val) if val.isdigit() else 0

    def fill_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, ctk.END)
                if self.board[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.board[i][j]))

    def generate_puzzle(self):
        difficulty = self.difficulty_var.get().lower()
        self.board = generate_board(difficulty)
        self.start_time = time.time()
        self.fill_board()
        self.message_label.configure(text=f"🧩 Puzzle generated ({difficulty.title()})")


    def toggle_strategy(self):
        self.strategy = "CSP" if self.strategy == "Backtracking" else "Backtracking"
        self.message_label.configure(text=f"🧠 Strategy set to: {self.strategy}")

    def validate_cell(self, row, col, *_):
        value = self.entries[row][col].get()
        if not value.isdigit():
            self.entries[row][col].configure(fg_color="white")
            return
        value = int(value)
        temp_board = [[int(self.entries[i][j].get() or 0) for j in range(9)] for i in range(9)]
        temp_board[row][col] = 0
        
        if not is_valid(temp_board, row, col, value):
            self.entries[row][col].configure(fg_color="misty rose")
            self.message_label.configure(text=f"⚠️ Invalid: {value} conflicts.")
        else:
            self.entries[row][col].configure(fg_color="light green")
            self.message_label.configure(text=f"✅ {value} is valid.")

            
        if self.is_board_complete() and self.is_board_valid():
            self.message_label.configure(text="🎉 Congratulations! Puzzle completed!")

        if self.is_board_complete() and not self.is_board_valid():
            self.message_label.configure(text="You are not able to solve the puzzle.")


    def is_board_complete(self):
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                if not val.isdigit() or int(val) == 0:
                    return False
        return True

    def is_board_valid(self):
        board = [[int(self.entries[i][j].get() or 0) for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == 0:
                    continue
                board[i][j] = 0
                if not is_valid(board, i, j, value):
                    return False
                board[i][j] = value
        return True


    def solve_sudoku(self):
        self.get_board()
        self.start_time = time.time()
        if self.strategy == "CSP":
            result, steps, duration = solve_csp(self.board)
        else:
            result, steps, duration = solve(self.board)

        if result:
            self.fill_board()
            self.message_label.configure(text=f"✅ Solved in {steps} steps and {duration:.2f}s")   
        else:
            self.message_label.configure(text="❌ No solution found.")

    def give_hint(self):
        self.get_board()
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    possible_values = [num for num in range(1, 10) if is_valid(self.board, i, j, num)]
                    if possible_values:
                        self.entries[i][j].delete(0, ctk.END)
                        self.entries[i][j].insert(0, str(possible_values[0]))
                        self.entries[i][j].configure(fg_color="lightyellow")
                        hint = f"💡 Hint: Try {possible_values[0]} at ({i+1},{j+1})"
                        self.message_label.configure(text=hint)
                        return
        self.message_label.configure(text="✅ Puzzle might already be solved.")

    def explain_move(self):
        self.get_board()
        trace = []

        def trace_solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        for num in range(1, 10):
                            if is_valid(board, i, j, num):
                                trace.append(f"✅ Trying {num} at ({i+1},{j+1}) — valid.")
                                board[i][j] = num
                                if trace_solve(board):
                                    return True
                                board[i][j] = 0
                                trace.append(f"↩️ Backtracking from {num} at ({i+1},{j+1})")
                            else:
                                trace.append(f"❌ {num} at ({i+1},{j+1}) — invalid.")
                        return False
            return True

        trace_solve([row[:] for row in self.board])
        self.explanation_box.configure(state="normal")
        self.explanation_box.delete("1.0", ctk.END)
        self.explanation_box.insert(ctk.END, "\n".join(trace))
        self.explanation_box.configure(state="disabled")
        self.message_label.configure(text="🧠 Explanation ready!")

if __name__ == "__main__":
    app = SudokuGUI()
    app.mainloop()
