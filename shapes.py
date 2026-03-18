import tkinter as tk
import turtle

class Shape:
    
    @staticmethod
    def _is_valid_color(color):
        try:
            tk.Widget.winfo_rgb(tk._default_root, color)
            return True
        except (ValueError, tk.TclError):
            return False


class Circle(Shape):
    def __init__(self, radius, extent=360, step=None, color=None, is_filled=False, is_centered=False):
        self.radius = radius
        self.extent = extent
        self.step = step
        self.color = color
        self.is_filled = is_filled
        self.is_centered = is_centered

    def _apply_color(self, t):
        if self.color and Shape._is_valid_color(self.color):
            t.color(self.color)

    def _restore_color(self, t, original_color):
        if self.color and Shape._is_valid_color(self.color):
            t.color(original_color)

    def _draw_circle(self, t):
        if self.is_filled:
            t.begin_fill()

        t.circle(self.radius, self.extent, self.step)

        if self.is_filled:
            t.end_fill()

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

        self._apply_color(t)

        if self.is_centered:
            self._offset(t)
            self._draw_circle(t)
            self._offset(t, reverse=True)
        else:
            self._draw_circle(t)

        self._restore_color(t, original_color)


class Square(Shape):
    def __init__(self, side_length, color=None, is_filled=False, is_centered=False):
        self.side_length = side_length
        self.color = color
        self.is_filled = is_filled
        self.is_centered = is_centered

    def _apply_color(self, t):
        if self.color and Shape._is_valid_color(self.color):
            t.color(self.color)

    def _restore_color(self, t, original_color):
        if self.color and Shape._is_valid_color(self.color):
            t.color(original_color)

    def _draw_square(self, t):
        if self.is_filled:
            t.begin_fill()

        t.move(self.side_length)
        for _ in range(3):
            t.rotate(-90)
            t.move(self.side_length)
        t.rotate(-90)

        if self.is_filled:
            t.end_fill()

    def _draw_square_centered(self, t):
        if self.is_filled:
            t.begin_fill()

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

        if self.is_filled:
            t.end_fill()

    def draw(self, manager, turtle_name):
        t = manager.get_turtle(turtle_name)

        original_color = t.color()

        self._apply_color(t)

        if self.is_centered:
            self._draw_square_centered(t)
        else:
            self._draw_square(t)

        self._restore_color(t, original_color)