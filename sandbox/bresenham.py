import tkinter as tk

def bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x2:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            points.append((x, y)) # In Assembly this will be save on memory
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    points.append((x2, y2))  # Make sure the endpoint is included
    return points

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bresenham Line Algorithm")
        self.geometry("250x300")  # Altura extra para botones o etiquetas

        self.canvas = tk.Canvas(self, width=250, height=250, bg='white')
        self.canvas.pack(pady=20)

        self.points = []

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def on_canvas_click(self, event):
        if len(self.points) == 2:
            self.canvas.delete("all")
            self.points = []
        
        self.canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill='red')
        self.points.append((event.x, event.y))
        
        if len(self.points) == 2:
            line_points = bresenham(*self.points[0], *self.points[1])
            for point in line_points:
                self.draw_point(point)

    def draw_point(self, point):
        x, y = point
        self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill='black')

if __name__ == "__main__":
    app = Application()
    app.mainloop()
