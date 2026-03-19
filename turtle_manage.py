import tkinter as tk
import turtle

class TurtleManager:
    def __init__(self, background_color="white"):
        self.screen = turtle.Screen()
        
        self.background_color = background_color
        self.screen.bgcolor(self.background_color)
        
        self.turtles = {}
        self.commands = []
    
    @property
    def turtle_count(self):
        return len(self.turtles)
    
    def add_turtle(self, name, shape="classic", color="black", size=1, speed=5):
        if name in self.turtles:
            raise ValueError(f"Turtle '{name}' already exists.")
        
        self.turtles[name] = Turtle(self, name, shape, color, size, speed)
        
    def remove_turtle(self, name):
        if name not in self.turtles:
            raise ValueError(f"Turtle '{name}' not found.")
        
        self.turtles[name]._t.hideturtle()
        self.turtles[name]._t.clear()
        
        del self.turtles[name]
        
    def get_turtle(self, name):
        try:
            return self.turtles[name]
        except KeyError:
            print(f"[Error]: '{name}' not found.")
            return None
            
    def print_turtle_list(self):
        for count, name in enumerate(self.turtles, start=1):
            print(f"{count}. {name}")
    
    def record(self, turtle_name, command, *args):
        self.commands.append({
            "turtle": turtle_name,
            "command": command,
            "args": args
        })

class Turtle:
    def __init__(self, manager, name, shape="classic", color="black", size=1, speed=5, fill_color=None):
        self._manager = manager
        
        self._name = name
        self._shape = shape
        self._color = color
        self._size = size
        self._speed = speed
        self._fill_color = fill_color if fill_color else color
        
        self._t = turtle.Turtle()
        
        self._t.shape(self._shape)
        self._t.color(self._color)
        self._t.pensize(self._size)
        self._t.speed(self._speed)
        self._t.fillcolor(self._fill_color)
    
    @property
    def pos(self):
        return self._t.pos()

    @property
    def angle(self):
        return self._t.heading()
    
    @property
    def attributes(self):
        return {
            "name": self._name,
            "shape": self._shape,
            "color": self._color,
            "size": self._size,
            "speed": self._speed,
        }
    
    @staticmethod
    def _is_valid_color(color):
        try:
            tk.Widget.winfo_rgb(tk._default_root, color)
            return True
        except (ValueError, tk.TclError):
            return False    
    
    def move_to(self, x, y):
        self._t.goto(x, y)
        self._manager.record(self._name, "move_to", x, y)
        
    def move(self, distance):
        self._t.forward(distance)
        self._manager.record(self._name, "move", distance)
    
    def rotate(self, angle):
        self._t.right(angle)
        self._manager.record(self._name, "rotate", angle)
        
    def pen_up(self):
        self._t.penup()
        self._manager.record(self._name, "pen_up")
        
    def pen_down(self):
        self._t.pendown()
        self._manager.record(self._name, "pen_down")
        
    def begin_fill(self):
        self._t.begin_fill()
        self._manager.record(self._name, "begin_fill")
        
    def end_fill(self):
        self._t.end_fill()
        self._manager.record(self._name, "end_fill")
        
    def show(self):
        self._t.showturtle()
        self._manager.record(self._name, "show")

    def hide(self):
        self._t.hideturtle()
        self._manager.record(self._name, "hide")

    def clear(self):
        self._t.clear()
        self._manager.record(self._name, "clear")

    def reset(self):
        self._t.reset()
    
    def write(self, text, font=("Arial", 12, "normal"), align="left"):
        self._t.write(text, font=font, align=align)
        self._manager.record(self._name, "write", text, font, align)
    
    def circle(self, radius, extent=360, steps=None):
        self._t.circle(radius, extent, steps)
        self._manager.record(self._name, "circle", radius, extent, steps)
    
    def color(self, color=None):
        
        if color is None:
            return self._color
        
        if not Turtle._is_valid_color(color):
            raise ValueError(f"Invalid color: {color}")
        
        self._color = color
        self._t.color(color)
        
        self._manager.record(self._name, "color", color)

    def speed(self, speed=None):
        
        if speed is None:
            return self._speed
        
        if not 0 <= speed <= 10:
            raise ValueError(f"Speed must be between 0 and 10, got {speed}")
        
        self._speed = speed
        self._t.speed(speed)
        
        self._manager.record(self._name, "speed", speed)

    def size(self, size=None):
        
        if size is None:
            return self._size
        
        if size <= 0:
            raise ValueError(f"Size must be a positive number, got {size}")
        
        self._size = size
        self._t.pensize(size)
        
        self._manager.record(self._name, "size", size)
        
    def fill_color(self, color=None):
    
        if color is None:
            return self._fill_color
        
        if not Turtle._is_valid_color(color):
            raise ValueError(f"Invalid color: {color}")
        
        self._fill_color = color
        self._t.fillcolor(color)
        
        self._manager.record(self._name, "fill_color", color)