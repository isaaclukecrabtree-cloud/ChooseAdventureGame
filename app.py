import tkinter as tk
from tkinter import ttk
from player import Player

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Adventure")
        self.geometry("500x300")

        # Declare stuff we want to reference later (like scene text so we can pass in event text)
        self.scene_text = None
        self.left_button = None
        self.right_button = None
        self.name_label = None
        self.level_label = None

        self.configure_layout()
        self.setup_frames()

    def load_event(self, event):
        self.scene_text.delete("1.0", tk.END)
        self.scene_text.insert(tk.END, event.get("scene_text", ""))

        self.left_button.config(text=event.get("option1", "Option 1"))
        self.right_button.config(text=event.get("option2", "Option 2"))

    def update_player_info(self, player):
        self.name_label.config(text=f"Name: {player.name}")
        self.level_label.config(text=f"Health: {player.health}/{player.max_health}")

    def load_demo_event(self):
        self.scene_text.delete("1.0", tk.END)
        self.scene_text.insert(tk.END, "Demo Scene")

        self.left_button.config(text="Option 1")
        self.right_button.config(text="Option 2")

        self.name_label.config(text="Name: Ninja")
        self.level_label.config(text="Level: 1")

    def configure_layout(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

    def setup_frames(self):
        left_frame = ttk.Frame(self)
        right_frame = ttk.Frame(self)

        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=3)
        left_frame.rowconfigure(1, weight=0)
        left_frame.rowconfigure(2, weight=0)

        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)

        left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.setup_left_frame(left_frame)
        self.setup_right_frame(right_frame)

    def setup_left_frame(self, frame):
        self.scene_text = tk.Text(frame, wrap=tk.WORD, width=40)
        self.left_button = ttk.Button(frame, text="Option 1", command=self.load_demo_event)
        self.right_button = ttk.Button(frame, text="Option 2")

        self.scene_text.grid(row=0, column=0, sticky="nsew")
        self.left_button.grid(row=1, column=0, sticky="ew", pady=5)
        self.right_button.grid(row=2, column=0, sticky="ew")

    def setup_right_frame(self, frame):
        self.name_label = ttk.Label(frame, text="Name: ")
        self.level_label = ttk.Label(frame, text="Level: ")

        self.name_label.pack(anchor="n", pady=(0, 10))
        self.level_label.pack(anchor="n")