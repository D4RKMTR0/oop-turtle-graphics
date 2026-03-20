import tkinter as tk
import turtle
import math

class Shape:
    @staticmethod
    def _is_valid_color(color):
        try:
            tk.Widget.winfo_rgb(tk._default_root, color)
            return True
        except (ValueError, tk.TclError):
            return False

    def _begin_fill(self, t):
        if self.is_filled:
            t.begin_fill()

    def _end_fill(self, t):
        if self.is_filled:
            t.end_fill()

    def _apply_color(self, t):
        if self.color and Shape._is_valid_color(self.color):
            t.color(self.color)

        if self.fill_color and Shape._is_valid_color(self.fill_color):
            t.fill_color(self.fill_color)

    def _restore_color(self, t, original_color, original_fill_color):
        if self.color and Shape._is_valid_color(self.color):
            t.color(original_color)

        if self.fill_color and Shape._is_valid_color(self.fill_color):
            t.fill_color(original_fill_color)

    @staticmethod
    def from_dict(data):
        shape_map = {
            "Circle": Circle,
            "Square": Square,
            "Rectangle": Rectangle,
            "EquilateralTriangle": EquilateralTriangle,
            "Triangle": Triangle,
            "Polygon": Polygon,
            "Star": Star,
            "Ellipse": Ellipse,
            "Spiral": Spiral,
        }

        shape_type = data.get("type")
        cls = shape_map.get(shape_type)

        if cls is None:
            raise ValueError(f"Unknown shape type: '{shape_type}'")

        params = {k: v for k, v in data.items() if k != "type"}
        return cls(**params)


class Circle(Shape):
    def __init__(self, radius, extent=360, step=None, color=None, fill_color=None, is_filled=False, is_centered=False):
        if radius <= 0:
            raise ValueError(f"Radius must be a positive number, got {radius}.")

        if not 0 < extent <= 360:
            raise ValueError(f"Extent must be between 0 and 360, got {extent}.")

        if step is not None and step <= 0:
            raise ValueError(f"Step must be a positive number, got {step}.")

        self.radius = radius
        self.extent = extent
        self.step = step
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

    def to_dict(self):
        return {
            "type": "Circle",
            "radius": self.radius,
            "extent": self.extent,
            "step": self.step,
            "color": self.color,
            "fill_color": self.fill_color,
            "is_filled": self.is_filled,
            "is_centered": self.is_centered,
        }

    def _draw_circle(self, t):
        self._begin_fill(t)
        t.circle(self.radius, self.extent, self.step)
        self._end_fill(t)

    def _offset(self, t, reverse=False):
        angle = -90 if reverse else 90

        t.pen_up()
        t.rotate(angle)
        t.move(self.radius)
        t.rotate(-angle)
        t.pen_down()

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()

        self._apply_color(t)

        if self.is_centered:
            self._offset(t)
            self._draw_circle(t)
            self._offset(t, reverse=True)
        else:
            self._draw_circle(t)

        self._restore_color(t, original_color, original_fill_color)


class Square(Shape):
    def __init__(self, side_length, color=None, fill_color=None, is_filled=False, is_centered=False):
        if side_length <= 0:
            raise ValueError(f"Side length must be a positive number, got '{side_length}'")

        self.side_length = side_length
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

    def to_dict(self):
        return {
            "type": "Square",
            "side_length": self.side_length,
            "color": self.color,
            "fill_color": self.fill_color,
            "is_filled": self.is_filled,
            "is_centered": self.is_centered,
        }

    def _draw_square(self, t):
        self._begin_fill(t)

        t.move(self.side_length)
        for _ in range(3):
            t.rotate(-90)
            t.move(self.side_length)
        t.rotate(-90)

        self._end_fill(t)

    def _draw_square_centered(self, t):
        self._begin_fill(t)

        t.pen_up()
        t.rotate(90)
        t.move(self.side_length / 2)
        t.rotate(-90)
        t.pen_down()
        t.move(self.side_length / 2)

        for _ in range(3):
            t.rotate(-90)
            t.move(self.side_length)

        t.rotate(-90)
        t.move(self.side_length / 2)
        t.pen_up()
        t.rotate(-90)
        t.move(self.side_length / 2)
        t.rotate(90)
        t.pen_down()

        self._end_fill(t)

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()

        self._apply_color(t)

        if self.is_centered:
            self._draw_square_centered(t)
        else:
            self._draw_square(t)

        self._restore_color(t, original_color, original_fill_color)


class Rectangle(Shape):
    def __init__(self, width, height, color=None, fill_color=None, is_filled=False, is_centered=False):
        if width <= 0 or height <= 0:
            raise ValueError(f"Width and Height must be a positive number, got width: {width} and height: {height}")

        self.width = width
        self.height = height
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

    def to_dict(self):
        return {
            "type": "Rectangle",
            "width": self.width,
            "height": self.height,
            "color": self.color,
            "fill_color": self.fill_color,
            "is_filled": self.is_filled,
            "is_centered": self.is_centered,
        }

    def _draw_rectangle(self, t):
        self._begin_fill(t)

        sides = (self.width, self.height) * 2
        for side in sides:
            t.move(side)
            t.rotate(-90)

        self._end_fill(t)

    def _draw_rectangle_centered(self, t):
        self._begin_fill(t)

        t.pen_up()
        t.rotate(90)
        t.move(self.height / 2)
        t.rotate(-90)
        t.move(self.width / 2)
        t.rotate(180)
        t.pen_down()

        sides = (self.width, self.height) * 2
        for side in sides:
            t.move(side)
            t.rotate(-90)

        t.pen_up()
        t.rotate(180)
        t.move(self.width / 2)
        t.rotate(90)
        t.move(self.height / 2)
        t.rotate(-90)
        t.pen_down()

        self._end_fill(t)

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()

        self._apply_color(t)

        if self.is_centered:
            self._draw_rectangle_centered(t)
        else:
            self._draw_rectangle(t)

        self._restore_color(t, original_color, original_fill_color)


class EquilateralTriangle(Shape):
    def __init__(self, side_length, color=None, fill_color=None, is_filled=False, is_centered=False):
        if side_length <= 0:
            raise ValueError(f"Side length must be a positive number, got {side_length}.")

        self.side_length = side_length
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

    def to_dict(self):
        return {
            "type": "EquilateralTriangle",
            "side_length": self.side_length,
            "color": self.color,
            "fill_color": self.fill_color,
            "is_filled": self.is_filled,
            "is_centered": self.is_centered,
        }

    def _draw_triangle(self, t):
        self._begin_fill(t)

        for _ in range(3):
            t.move(self.side_length)
            t.rotate(-120)

        self._end_fill(t)

    def _offset(self, t, reverse=False):
        offset = self.side_length / (2 * math.sqrt(3))
        angle = -90 if reverse else 90

        t.pen_up()
        t.rotate(angle)
        t.move(offset)
        t.rotate(-angle)
        t.pen_down()

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()

        self._apply_color(t)

        if self.is_centered:
            self._offset(t)
            self._draw_triangle(t)
            self._offset(t, reverse=True)
        else:
            self._draw_triangle(t)

        self._restore_color(t, original_color, original_fill_color)


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c, color=None, fill_color=None, is_filled=False, is_centered=False):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(f"All sides must be positive numbers, got side_a: {side_a}, side_b: {side_b}, side_c: {side_c}.")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

        if not (self.side_a + self.side_b > self.side_c and
                self.side_b + self.side_c > self.side_a and
                self.side_a + self.side_c > self.side_b):
            raise ValueError("Invalid triangle: sides do not form a valid triangle.")

    def to_dict(self):
        return {
            "type": "Triangle",
            "side_a": self.side_a,
            "side_b": self.side_b,
            "side_c": self.side_c,
            "color": self.color,
            "fill_color": self.fill_color,
            "is_filled": self.is_filled,
            "is_centered": self.is_centered,
        }

    def _compute_angles(self):
        angle_a = math.acos(max(-1, min(1, (self.side_b**2 + self.side_c**2 - self.side_a**2) / (2 * self.side_b * self.side_c))))
        angle_b = math.acos(max(-1, min(1, (self.side_a**2 + self.side_c**2 - self.side_b**2) / (2 * self.side_a * self.side_c))))
        angle_c = math.acos(max(-1, min(1, (self.side_a**2 + self.side_b**2 - self.side_c**2) / (2 * self.side_a * self.side_b))))

        return math.degrees(angle_a), math.degrees(angle_b), math.degrees(angle_c)

    def _draw_triangle(self, t):
        angle_a, angle_b, angle_c = self._compute_angles()

        self._begin_fill(t)

        t.move(self.side_a)
        t.rotate(-(180 - angle_c))
        t.move(self.side_b)
        t.rotate(-(180 - angle_a))
        t.move(self.side_c)
        t.rotate(-(180 - angle_b))

        self._end_fill(t)

    def _offset(self, t, origin=None, reverse=False):
        angle_a, angle_b, angle_c = self._compute_angles()

        if not reverse:
            origin = t.pos

            vert1 = origin

            vert2 = (
                vert1[0] + self.side_a * math.cos(math.radians(t.angle)),
                vert1[1] + self.side_a * math.sin(math.radians(t.angle))
            )

            vert3 = (
                vert2[0] + self.side_b * math.cos(math.radians(t.angle - (180 - angle_c))),
                vert2[1] + self.side_b * math.sin(math.radians(t.angle - (180 - angle_c)))
            )

            centroid_x = (vert1[0] + vert2[0] + vert3[0]) / 3
            centroid_y = (vert1[1] + vert2[1] + vert3[1]) / 3

            t.pen_up()
            t.move_to(centroid_x, centroid_y)
            t.pen_down()

            return origin

        else:
            t.pen_up()
            t.move_to(origin[0], origin[1])
            t.pen_down()

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()

        self._apply_color(t)

        if self.is_centered:
            origin = self._offset(t)
            self._draw_triangle(t)
            self._offset(t, origin=origin, reverse=True)
        else:
            self._draw_triangle(t)

        self._restore_color(t, original_color, original_fill_color)


class Polygon(Shape):
    def __init__(self, sides, side_length, color=None, fill_color=None, is_filled=False, is_centered=False):
        if sides < 3:
            raise ValueError("Polygon must have at least 3 sides.")

        if side_length <= 0:
            raise ValueError(f"Side length must be a positive number, got {side_length}.")

        self.sides = sides
        self.side_length = side_length
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

    def to_dict(self):
        return {
            "type": "Polygon",
            "sides": self.sides,
            "side_length": self.side_length,
            "color": self.color,
            "fill_color": self.fill_color,
            "is_filled": self.is_filled,
            "is_centered": self.is_centered,
        }

    def _draw_polygon(self, t):
        exterior_angle = 360 / self.sides

        self._begin_fill(t)

        for _ in range(self.sides):
            t.move(self.side_length)
            t.rotate(-exterior_angle)

        self._end_fill(t)

    def _offset(self, t, reverse=False):
        circumradius = self.side_length / (2 * math.sin(math.pi / self.sides))
        angle = -90 if reverse else 90

        t.pen_up()
        t.rotate(angle)
        t.move(circumradius)
        t.rotate(-angle)
        t.pen_down()

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()

        self._apply_color(t)

        if self.is_centered:
            self._offset(t)
            self._draw_polygon(t)
            self._offset(t, reverse=True)
        else:
            self._draw_polygon(t)

        self._restore_color(t, original_color, original_fill_color)


class Star(Shape):
    def __init__(self, points, size, color=None, fill_color=None, is_filled=False, is_centered=False, intersected=True):
        if points < 3:
            raise ValueError("Star must have at least 3 points.")

        if size <= 0:
            raise ValueError(f"Size must be a positive number, got {size}.")

        self.points = points
        self.size = size
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered
        self.intersected = intersected

    def to_dict(self):
        return {
            "type": "Star",
            "points": self.points,
            "size": self.size,
            "color": self.color,
            "fill_color": self.fill_color,
            "is_filled": self.is_filled,
            "is_centered": self.is_centered,
            "intersected": self.intersected,
        }

    def _draw_star_intersected(self, t):
        turn_angle = 180 - (180 / self.points)

        self._begin_fill(t)

        for _ in range(self.points):
            t.move(self.size)
            t.rotate(-turn_angle)

        self._end_fill(t)

    def _draw_star_outline(self, t):
        outer_angle = 360 / self.points
        inner_angle = outer_angle / 2

        inner_size = self.size * math.sin(math.radians(inner_angle / 2)) / math.sin(math.radians(90 - inner_angle / 2))

        self._begin_fill(t)

        for _ in range(self.points):
            t.move(self.size)
            t.rotate(-(180 - inner_angle))
            t.move(inner_size)
            t.rotate(-(180 - outer_angle))

        self._end_fill(t)

    def _offset(self, t, reverse=False):
        circumradius = self.size / (2 * math.sin(math.pi / self.points))
        angle = -90 if reverse else 90

        t.pen_up()
        t.rotate(angle)
        t.move(circumradius)
        t.rotate(-angle)
        t.pen_down()

    def _draw(self, t):
        if self.intersected:
            self._draw_star_intersected(t)
        else:
            self._draw_star_outline(t)

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()

        self._apply_color(t)

        if self.is_centered:
            self._offset(t)
            self._draw(t)
            self._offset(t, reverse=True)
        else:
            self._draw(t)

        self._restore_color(t, original_color, original_fill_color)


class Ellipse(Shape):
    def __init__(self, radius_x, radius_y, color=None, fill_color=None, is_filled=False, is_centered=False, steps=100):
        if radius_x <= 0:
            raise ValueError(f"radius_x must be a positive number, got {radius_x}.")

        if radius_y <= 0:
            raise ValueError(f"radius_y must be a positive number, got {radius_y}.")

        if steps <= 0:
            raise ValueError(f"Steps must be a positive number, got {steps}.")

        self.radius_x = radius_x
        self.radius_y = radius_y
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered
        self.steps = steps

    def to_dict(self):
        return {
            "type": "Ellipse",
            "radius_x": self.radius_x,
            "radius_y": self.radius_y,
            "color": self.color,
            "fill_color": self.fill_color,
            "is_filled": self.is_filled,
            "is_centered": self.is_centered,
            "steps": self.steps,
        }

    def _get_point(self, origin, angle):
        angle_rad = math.radians(angle)
        x = origin[0] + self.radius_x * math.cos(angle_rad)
        y = origin[1] + self.radius_y * math.sin(angle_rad)
        return x, y

    def _goto_point(self, t, origin, angle):
        x, y = self._get_point(origin, angle)
        t._t.goto(x, y)

    def _draw_ellipse(self, t, origin):
        step_angle = 360 / self.steps

        self._begin_fill(t)

        t._t.penup()
        self._goto_point(t, origin, 0)
        t._t.pendown()

        for i in range(1, self.steps + 1):
            self._goto_point(t, origin, i * step_angle)

        self._end_fill(t)

    def _restore_position(self, t, origin):
        t.pen_up()
        t.move_to(origin[0], origin[1])
        t.pen_down()

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()
        origin = t.pos

        self._apply_color(t)
        self._draw_ellipse(t, origin)

        if self.is_centered:
            self._restore_position(t, origin)

        self._restore_color(t, original_color, original_fill_color)


class Spiral(Shape):
    def __init__(self, steps, growth, angle, color=None, fill_color=None, is_filled=False):
        if steps <= 0:
            raise ValueError(f"Steps must be a positive number, got {steps}.")

        if growth <= 0:
            raise ValueError(f"Growth must be a positive number, got {growth}.")

        if angle == 0:
            raise ValueError("Angle cannot be 0, the spiral would never turn.")

        self.steps = steps
        self.growth = growth
        self.angle = angle
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled

    def to_dict(self):
        return {
            "type": "Spiral",
            "steps": self.steps,
            "growth": self.growth,
            "angle": self.angle,
            "color": self.color,
            "fill_color": self.fill_color,
            "is_filled": self.is_filled,
        }

    def _draw_spiral(self, t):
        self._begin_fill(t)

        for i in range(self.steps):
            t.move(i * self.growth)
            t.rotate(-self.angle)

        self._end_fill(t)

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()

        self._apply_color(t)
        self._draw_spiral(t)
        self._restore_color(t, original_color, original_fill_color)