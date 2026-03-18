import turtle

def is_valid_color(color):
    try:
        turtle.color(color)
        return True
    except turtle.TurtleGraphicsError:
        return False
    
class Circle:
    def __init__(self, radius, extent=360, step=None, color=None, is_filled=False):
        self.radius = radius
        self.extent = extent
        self.step = step
        self.color = color
        self.is_filled = is_filled
    
    def draw(self, manager, turtle_name, group_name="default"):
        
        t = manager.get_turtles(group_name, turtle_name)
            
        turtle_color = t.color
            
        if self.color and is_valid_color(self.color):
            t.t.color(self.color)
            
        if self.is_filled:
            t.t.begin_fill()
            
        t.t.circle(self.radius, self.extent, self.step)
        
        if self.is_filled:
            t.t.end_fill()
            
        if self.color and is_valid_color(self.color):
            t.t.color(turtle_color)
            
class Square:
    def __init__(self, side_length, color=None, is_filled=False):
        self.side_length = side_length
        self.color = color
        self.is_filled = is_filled
        
    def draw(self, manager, turtle_name, group_name):
        
        t = manager.get_turtles(group_name, turtle_name)
        
        turtle_color = t.color
        
        if self.color and is_valid_color(self.color):
            t.t.color(self.color)
            
        if self.is_filled:
            t.t.begin_fill()
        
        t.t.penup()
        t.t.right(90)
        t.t.forward(self.side_length/2)
        t.t.left(90)
        t.t.pendown()
        t.t.forward(self.side_length/2)
        for _ in range(3):
            t.t.left(90)
            t.t.forward(self.side_length)
        t.t.left(90)
        t.t.forward(self.side_length/2)
        t.t.penup()
        t.t.left(90)
        t.t.forward(self.side_length/2)
        t.t.right(90)
        t.t.pendown()
        
        if self.is_filled:
            t.t.end_fill()
            
        if self.color and is_valid_color(self.color):
            t.t.color(turtle_color)