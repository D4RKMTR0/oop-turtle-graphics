import turtle

class TurtleManager:
    def __init__(self):
        self.turtles = {
            "default": {}
        }
    
    def get_turtle(self, group_name, turtle_name):
        try:
            return self.turtles[group_name][turtle_name]
        except KeyError:
            print(f"[Error]: '{turtle_name}' not found in group '{group_name}'.")
            return None
            
    def print_turtle_list(self):
        for (group_name, group) in self.turtles.items():
            print(group_name)
            for count, turtle in enumerate(group, start=1):
                print(f"{count}. {turtle}")

    @property
    def turtle_count(self):
        return sum(len(group) for group in self.turtles.values())
    
class Turtle:
    def __init__(self, name, shape="classic", color="black", size=1, speed=5):
        self.name = name
        self.shape = shape
        self.color = color
        self.size = size
        self.speed = speed
        
        self.t = turtle.Turtle()
        
        self.t.shape(self.shape)
        self.t.color(self.color)
        self.t.pensize(self.size)
        self.t.speed(self.speed)