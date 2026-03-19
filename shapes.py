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


class Circle(Shape):
    def __init__(self, radius, extent=360, step=None, color=None, fill_color=None, is_filled=False, is_centered=False):
        self.radius = radius
        self.extent = extent
        self.step = step
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

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
        self.side_length = side_length
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

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
        self.width = width
        self.height = height
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

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
        self.side_length = side_length
        self.color = color
        self.fill_color = fill_color
        self.is_filled = is_filled
        self.is_centered = is_centered

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

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()
        original_fill_color = t.fill_color()

        self._apply_color(t)

        if self.is_centered:
            self._offset(t)
            if self.intersected:
                self._draw_star_intersected(t)
            else:
                self._draw_star_outline(t)
            self._offset(t, reverse=True)
        else:
            if self.intersected:
                self._draw_star_intersected(t)
            else:
                self._draw_star_outline(t)

        self._restore_color(t, original_color, original_fill_color)