import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Drawing App")
        self.root.geometry("800x600")

        self.brush_color = "black"
        self.brush_size = 3

        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Use light green background and dark text for all buttons
        button_bg = "#90ee90"  # light green
        button_fg = "black"    # dark text for better contrast

        self.colors = ["black", "red", "green", "blue", "orange", "purple", "brown", "yellow"]
        for color in self.colors:
            btn = tk.Button(
                self.top_frame,
                text=color.capitalize(),
                bg=button_bg,
                fg=button_fg,
                activebackground=button_bg,
                activeforeground=button_fg,
                width=10,
                command=lambda c=color: self.set_color(c)
            )
            btn.pack(side=tk.LEFT, padx=2, pady=2)

        clear_btn = tk.Button(
            self.top_frame,
            text="Clear",
            bg=button_bg,
            fg=button_fg,
            activebackground=button_bg,
            activeforeground=button_fg,
            width=10,
            command=self.clear_canvas
        )
        clear_btn.pack(side=tk.RIGHT, padx=10)

        self.canvas = tk.Canvas(self.root, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.last_x = None
        self.last_y = None

    def set_color(self, new_color):
        self.brush_color = new_color

    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(self.last_x, self.last_y, x, y,
                                fill=self.brush_color,
                                width=self.brush_size,
                                capstyle=tk.ROUND,
                                smooth=True)
        self.last_x = x
        self.last_y = y

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
