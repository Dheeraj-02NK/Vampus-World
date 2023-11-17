import tkinter as tk
from tkinter import PhotoImage, messagebox


class VampusWorld:
    def __init__(self, size, vampus_positions, gold_positions):
        self.size = size
        self.agent_pos = (0, 0)
        self.vampus_positions = vampus_positions
        self.gold_positions = gold_positions
        self.obstacles = []  # No obstacles for simplicity
        self.agent_history = [self.agent_pos]
        self.feedback = ""
        self.game_over = False

    def move_agent(self, direction):
        if self.game_over:
            return

        x, y = self.agent_pos
        if direction == "UP" and y > 0:
            self.agent_pos = (x, y - 1)
        elif direction == "DOWN" and y < self.size - 1:
            self.agent_pos = (x, y + 1)
        elif direction == "LEFT" and x > 0:
            self.agent_pos = (x - 1, y)
        elif direction == "RIGHT" and x < self.size - 1:
            self.agent_pos = (x + 1, y)

        self.agent_history.append(self.agent_pos)
        self.update_feedback()

    def is_valid_move(self, pos):
        x, y = pos
        return 0 <= x < self.size and 0 <= y < self.size and pos not in self.obstacles

    def check_proximity(self):
        x, y = self.agent_pos

        vampus_nearby = False
        for vampus_x, vampus_y in self.vampus_positions:
            if abs(x - vampus_x) <= 1 and abs(y - vampus_y) <= 1:
                vampus_nearby = True

        if vampus_nearby:
            self.feedback = "Smoke! Vampus is nearby."
        else:
            self.feedback = "Cold."

    def update_feedback(self):
        if self.agent_pos in self.vampus_positions:
            self.feedback = "Game Over! Vampus caught you."
            self.game_over = True
        elif self.agent_pos in self.gold_positions:
            self.feedback = "Congratulations! You found the gold."
            self.game_over = True
        else:
            self.check_proximity()


class VampusGUI:
    def __init__(self, master, world):
        self.master = master
        self.world = world
        self.master.title("Vampus World")

        self.canvas_size = 600

        self.canvas = tk.Canvas(master, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack()

        self.images = {
            "agent": PhotoImage(file="agent.png").subsample(6,6),
            "vampus": PhotoImage(file="vampus.png").subsample(6,6),
            "gold": PhotoImage(file="gold.png").subsample(6,6),
        }

        self.create_buttons()
        self.draw_world()

    def create_buttons(self):
        button_frame = tk.Frame(self.master, bg="white")
        button_frame.pack()

        button_up = tk.Button(button_frame, text="↑", font=("Times New Roman", 14),
                              command=lambda: self.move_agent("UP"), width=10, height=2)
        button_down = tk.Button(button_frame, text="↓", font=("Times New Roman", 14),
                                command=lambda: self.move_agent("DOWN"), width=10, height=2)
        button_left = tk.Button(button_frame, text="←", font=("Times New Roman", 14),
                                command=lambda: self.move_agent("LEFT"), width=10, height=2)
        button_right = tk.Button(button_frame, text="→", font=("Times New Roman", 14),
                                 command=lambda: self.move_agent("RIGHT"), width=10, height=2)

        button_up.grid(row=0, column=1)
        button_down.grid(row=2, column=1)
        button_left.grid(row=1, column=0)
        button_right.grid(row=1, column=2)

    def move_agent(self, direction):
        self.world.move_agent(direction)
        self.draw_world()

    def draw_world(self):
        self.canvas.delete("all")

        cell_size = self.canvas_size // self.world.size

        for x in range(self.world.size):
            for y in range(self.world.size):
                self.canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size,
                                             fill="lightgray")

        for vampus_pos in self.world.vampus_positions:
            if vampus_pos == self.world.agent_pos:
                self.draw_item(vampus_pos, "agent")
            elif vampus_pos in self.world.agent_history:
                self.draw_item(vampus_pos, "vampus")

        for gold_pos in self.world.gold_positions:
            if gold_pos == self.world.agent_pos:
                self.draw_item(gold_pos, "agent")
            elif gold_pos in self.world.agent_history:
                self.draw_item(gold_pos, "gold")

        self.draw_item(self.world.agent_pos, "agent")

        self.world.update_feedback()
        feedback_text = self.world.feedback
        self.canvas.create_text(self.canvas_size // 2, self.canvas_size - 20, text=feedback_text,
                                font=("Times New Roman", 16), fill="black")

        if self.world.game_over:
            self.disable_buttons()
            messagebox.showinfo("Game Over", self.world.feedback)

    def draw_item(self, position, item):
        cell_size = self.canvas_size // self.world.size
        x, y = position
        self.canvas.create_image(x * cell_size + cell_size // 2, y * cell_size + cell_size // 2,
                                 image=self.images[item], tag=item)

    def disable_buttons(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state="disabled")


def run_game():
    size = 5
    vampus_positions = [(1, 2), (3, 3), (4, 1)]  # Example of multiple vampus positions
    gold_positions = [(4, 4)]  # Example of multiple gold positions
    world = VampusWorld(size, vampus_positions, gold_positions)

    root = tk.Tk()

    gui = VampusGUI(root, world)

    root.mainloop()


if __name__ == "__main__":
    run_game()
