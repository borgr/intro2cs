"""Map drawing utilities for U.S. sentiment data."""

from graphics import Canvas
from geo import us_states

# A fixed gradient of sentiment colors from negative (blue) to positive (red)
# Colors chosen via Cynthia Brewer's Color Brewer (colorbrewer2.com)
SENTIMENT_COLORS = ["#313695", "#4575B4", "#74ADD1", "#ABD9E9", "#E0F3F8",
                    "#FFFFFF", "#FEE090", "#FDAE61", "#F46D43", "#D73027",
                    "#A50026"]
GRAY = "#AAAAAA"

def get_sentiment_color(sentiment, sentiment_scale=4):
    """Returns a color corresponding to the sentiment value.

    sentiment -- a number between -1 (negative) and +1 (positive)
    """
    if sentiment is None:
        return GRAY
    scaled = (sentiment_scale * sentiment + 1)/2
    index = int( scaled * len(SENTIMENT_COLORS) ) # Rounds down
    if index < 0:
        index = 0
    if index >= len(SENTIMENT_COLORS):
        index = len(SENTIMENT_COLORS) - 1
    return SENTIMENT_COLORS[index]

def draw_state(shapes, sentiment_value=None, canvas=None):
    """Draw the named state in the given color on the canvas.

    state -- a list of list of polygons (which are lists of positions)
    sentiment_value -- a number between -1 (negative) and 1 (positive)
    canvas -- the graphics.Canvas object
    """
    if not canvas:
        canvas = get_canvas()
    for polygon in shapes:
        vertices = [position.position_to_xy() for position in polygon]
        color = get_sentiment_color(sentiment_value)
        canvas.draw_polygon(vertices, fill_color=color)

def draw_name(name, location, canvas=None):
    """Draw the two-letter postal code at the center of the state.

    location -- a position
    """
    if not canvas:
        canvas = get_canvas()
    center = location.position_to_xy()
    canvas.draw_text(name.upper(), center, anchor='center', style='bold')

def draw_dot(location, sentiment_value=None, radius=3, canvas=None):
    """Draw a small dot at location.

    location -- a position
    sentiment_value -- a number between -1 (negative) and 1 (positive)
    """
    if not canvas:
        canvas = get_canvas()
    center = location.position_to_xy()
    color = get_sentiment_color(sentiment_value)
    canvas.draw_circle(center, radius, fill_color=color)

def memoize(fn):
    """A decorator for caching the results of the decorated function."""
    cache = {}
    def memoized(*args):
        if args in cache:
            return cache[args]
        result = fn(*args)
        cache[args] = result
        return result
    return memoized

@memoize
def get_canvas():
    """Return a Canvas, which is a drawing window."""
    return Canvas(width=960, height=500)

def wait(secs=0, canvas=None):
    """Wait for mouse click."""
    if not canvas:
        canvas = get_canvas()
    canvas.wait_for_click(secs)

def message(s, canvas=None):
    """Display a message."""
    if not canvas:
        canvas = get_canvas()
        canvas.draw_text(s, (canvas.width//2, canvas.height//2), size=36, anchor='center')
    else:
        #canvas.draw_text(s, (canvas.width//2, canvas.height//2), size=36, anchor='center')
        canvas.draw_text(s, (canvas.width*7//11, canvas.height*8//9), size=36, anchor='center')

def clear(canvas=None):
    """Clear canvas."""
    if not canvas:
        canvas = get_canvas()
    canvas.clear()

def get_img_copy(canvas=None):
    """Clear canvas."""
    if canvas:
        return canvas.get_copy()
