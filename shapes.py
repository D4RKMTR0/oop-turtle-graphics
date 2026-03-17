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
    
    def draw(self, turtle_dict, turtle_name):
        try:
            t = turtle_dict[turtle_name]
        except Exception as e:
            print(f"[Error]: {e}")
            
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