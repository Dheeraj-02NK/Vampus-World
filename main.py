import tkinter as tk
import random

class VampusWorld:
    def __init__(self, size, vampus_pos, gold_pos):
        self.size = size
        self.agent_pos = (0, 0)
        self.vampus_pos = vampus_pos
        self.gold_pos = gold_pos
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
        vampus_x, vampus_y = self.vampus_pos

        if abs(x - vampus_x) <= 1 and abs(y - vampus_y) <= 1:
            self.feedback = "Smoke! Vampus is nearby."
        else:
            self.feedback = "Cold."

    def update_feedback(self):
        if self.agent_pos == self.vampus_pos:
            self.feedback = "Game Over! Vampus caught you."
            self.game_over = True
        elif self.agent_pos == self.gold_pos:
            self.feedback = "Congratulations! You found the gold."
            self.game_over = True
        else:
            self.check_proximity()

class VampusGUI:
    def __init__(self, master, world):
        self.master = master
        self.world = world
        self.canvas = tk.Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack()
        self.create_buttons()
        self.draw_world()

    def create_buttons(self):
        button_frame = tk.Frame(self.master, bg="white")
        button_frame.pack()

        button_up = tk.Button(button_frame, text="^", command=lambda: self.move_agent("UP"))
        button_down = tk.Button(button_frame, text="v", command=lambda: self.move_agent("DOWN"))
        button_left = tk.Button(button_frame, text="<", command=lambda: self.move_agent("LEFT"))
        button_right = tk.Button(button_frame, text=">", command=lambda: self.move_agent("RIGHT"))

        button_up.grid(row=0, column=1)
        button_down.grid(row=2, column=1)
        button_left.grid(row=1, column=0)
        button_right.grid(row=1, column=2)

    def move_agent(self, direction):
        self.world.move_agent(direction)
        self.draw_world()

    def draw_world(self):
        self.canvas.delete("agent")
        self.canvas.delete("feedback")

        for x in range(self.world.size):
            for y in range(self.world.size):
                self.canvas.create_rectangle(x * 40, y * 40, (x + 1) * 40, (y + 1) * 40, fill="lightgray")

        agent_x, agent_y = self.world.agent_pos
        self.canvas.create_oval(agent_x * 40 + 10, agent_y * 40 + 10,
                                (agent_x + 1) * 40 - 10, (agent_y + 1) * 40 - 10, fill="blue", tag="agent")

        self.world.update_feedback()
        self.canvas.create_text(200, 380, text=self.world.feedback, font=("Arial", 12), fill="black", tag="feedback")

        if self.world.game_over:
            self.disable_buttons()

    def disable_buttons(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state=tk.DISABLED)

def run_game():
    size = 5
    vampus_pos = (3, 2)
    gold_pos = (4, 4)
    world = VampusWorld(size, vampus_pos, gold_pos)

    root = tk.Tk()
    root.title("Vampus World")

    gui = VampusGUI(root, world)

    root.mainloop()

if __name__ == "__main__":
    run_game()
