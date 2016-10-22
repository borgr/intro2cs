"""The graphics module implements a simple GUI library."""

from PIL import Image,ImageDraw,ImageFont

import sys
import math

from data import DATA_PATH

# Should do for now
fontdict = {(36,'normal'):ImageFont.load(DATA_PATH+"pilfonts/helvR24.pil"),
            (12,'bold'  ):ImageFont.load(DATA_PATH+"pilfonts/helvB14.pil")}

class MapImage(Image.Image):
    """A Canvas object supports drawing and animation primitives.

    draw_* methods return the id number of a shape object in the underlying Tk
    object.  This id can be passed to move_* and edit_* methods.

    Canvas is a singleton; only one Canvas instance can be created.

    """
    def __init__(self, width=1024, height=768, title='', color='White', tk=None):
        self._img = Image.new('RGB',(width,height))
        self.draw = ImageDraw.Draw(self._img)

        # Attributes
        self.color = color
        self.width = width
        self.height = height

        # Canvas object
        self._draw_background()

    def get_copy(self):
        return self._img.copy()

    def clear(self, shape='all'):
        self._draw_background()

    def draw_polygon(self, points, color='Black', fill_color=None, filled=1, smooth=0, width=1):
        """Draw a polygon and return its tkinter id.

        points -- a list of (x, y) pairs encoding pixel positions
        """
        if fill_color == None:
            fill_color = color
        if filled == 0:
            fill_color = ""
        return self.draw.polygon(xy=points,fill=fill_color,outline='Black')

    def draw_circle(self, center, radius, color='Black', fill_color=None, filled=1, width=1):
        """Draw a cirlce and return its tkinter id.

        center -- an (x, y) pair encoding a pixel position
        """
        if fill_color == None:
            fill_color = color
        if filled == 0:
            fill_color = ""
        x0, y0 = [c - radius for c in center]
        x1, y1 = [c + radius for c in center]
        return self.draw.ellipse([x0, y0, x1, y1], fill=fill_color, outline=color)

    def draw_text(self, text, pos, color='Black', font='Arial',
                  size=12, style='normal', anchor=None):
        """Draw text and return its tkinter id."""
        x, y = pos
        font = fontdict[size,style] #Should do for now
        w,h = self.draw.textsize(text, font)
        return self.draw.text((x-w//2,y-h//2), text, color, font)

    def wait_for_click(self, seconds=0):
        pass

    def _draw_background(self):
        w, h = self.width - 1, self.height - 1
        corners = [(0,0), (0, h), (w, h), (w, 0)]
        self.draw_polygon(corners, self.color, fill_color=self.color, filled=True, smooth=False)

def translate_point(point, angle, distance):
    """Translate a point a distance in a direction (angle)."""
    x, y = point
    return (x + math.cos(angle) * distance, y + math.sin(angle) * distance)

def shift_point(point, offset):
    """Shift a point by an offset."""
    x, y = point
    dx, dy = offset
    return (x + dx, y + dy)

def rectangle_points(pos, width, height):
    """Return the points of a rectangle starting at pos."""
    x1, y1 = pos
    x2, y2 = width + x1, height + y1
    return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

def format_color(r, g, b):
    """Format a color as a string.

    r, g, b -- integers from 0 to 255
    """
    return '#{0:02x}{1:02x}{2:02x}'.format(int(r * 255), int(g * 255), int(b * 255))
