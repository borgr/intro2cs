#############################################################
# FILE : geo_tweet_tools.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex7 200132014
# DESCRIPTION: geographic tweet tools
# 
#############################################################
from geo import us_states, Position, geo_distance
from tweet import Tweet
import sys
    
def find_centroid(polygon):
    """Find the centroid of a polygon.

    http://en.wikipedia.org/wiki/Centroid #Centroid_of_polygon

    polygon -- A list of positions, in which the first and last are the same

    Returns: 3 numbers; centroid latitude, centroid longitude, and polygon area

    Hint: If a polygon has 0 area, return its first position as its centroid

    >>> p1, p2, p3 = Position(1, 2), Position(3, 4), Position(5, 0)
    >>> triangle = [p1, p2, p3, p1]  # First vertex is also the last vertex
    >>> find_centroid(triangle)
    (Position(3.0, 2.0), 6.0)
    >>> find_centroid([p1, p3, p2, p1])
    (Position(3.0, 2.0), 6.0)
    >>> find_centroid([p1, p2, p1])
    (Position(1.0, 2.0), 0)
    """
    calculation = [polygon[index].latitude()*polygon[index+1].longitude()-
                    polygon[index+1].latitude()*polygon[index].longitude()
                   for index in range(len(polygon)-1)]
    area = 0.5*sum(calculation)

    # if there is no area
    if(area == 0):
        return polygon[0], int(area)  # area as a float is not expected
    cx = sum([(polygon[index].latitude()+polygon[index+1].latitude())
              *calculation[index] for index in range(len(calculation))])/6/area
    cy = sum([(polygon[index].longitude()+polygon[index+1].longitude())
              *calculation[index] for index in range(len(calculation))])/6/area
    return Position(cx,cy), abs(area)


def find_center(polygons):
    """Compute the geographic center of a state, averaged over its polygons.

    The center is the average position of centroids of the polygons in polygons,
    weighted by the area of those polygons.

    Arguments:
    polygons -- a list of polygons

    >>> ca = find_center(us_states['CA'])  # California
    >>> round(ca.latitude(), 5)
    37.25389
    >>> round(ca.longitude(), 5)
    -119.61439

    >>> hi = find_center(us_states['HI'])  # Hawaii
    >>> round(hi.latitude(), 5)
    20.1489
    >>> round(hi.longitude(), 5)
    -156.21763
    """
    centroids = [find_centroid(polygon) for polygon in polygons]
    place_polygon = 0
    place_area = 1
    cx = (sum(centroids[index][place_polygon].latitude()*
              centroids[index][place_area]
              for index in range(len(centroids)))
          /sum([centroids[index][place_area]
                for index in range(len(centroids))]))
    cy = (sum(centroids[index][place_polygon].longitude()*
              centroids[index][place_area]
              for index in range(len(centroids)))
          /sum([centroids[index][place_area]
                for index in range(len(centroids))]))
    return Position(cx,cy)

def find_closest_state(state_centers):
    """Returns a function that takes a tweet and returns the name of the state 
    closest to the given tweet's location.

    Use the geo_distance function (already provided) to calculate distance
    in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    state_centers -- a dictionary from state names to positions.

    >>> state_centers = {n: find_center(s) for n, s in us_states.items()}
    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> nj = Tweet("Welcome to New Jersey", None, 41.1, -74)
    >>> find_state = find_closest_state(state_centers)
    >>> find_state(sf)
    'CA'
    >>> find_state(nj)
    'NJ'
    """
    #copy the dictionary to avoid changing later from the outside
    state_centers = state_centers.copy()

    #define the needed function
    def find_state(tweet):
        """ Tells in which state was the tweet
        """
        if not state_centers:
            return
        #Checks for smallest distance, going through dict. only once.
        distance = float("inf")
        for state in state_centers:
            check_distance = geo_distance(tweet.get_location(),
                                          state_centers[state])
            if check_distance < distance:
                distance = check_distance
                postal = state
        return postal
    return find_state


def intersects(position, side):
    """ This function gets a position and a side
        and tells if they intersect.
        Args:
        position - a position object
        side - a tuple containing two position objects

        Returns:
        True if they intersect
        False otherwise

        for info about how it works:
        http://rosettacode.org/wiki/Ray-casting_algorithm
    """
    if side[0].longitude() < side[1].longitude():
        a = side[0]
        b = side[1]
    else:
        a = side[1]
        b = side[0]
    py = position.longitude()  # p stands for position
    px = position.latitude()
    ay = a.longitude()
    ax = a.latitude()
    by = b.longitude()
    bx = b.latitude()
    if py == ay or py == by:
        py += sys.float_info.epsilon
    if py < ay or py > by:
        return False
    elif px > max(ax, bx):
         return False
    else:
        if px < min(ax, bx):
            return True
        else:
            if ax != bx :
                check_ab = (by - ay)/(bx - ax)
            else:
                check_ab = float("inf")
            if ax != px:
                check_pa = (py-ay) / (px-ax)
            else:
                check_pa = float("inf")
            if check_pa >= check_ab:
                return True
            else:
                return False

            
def find_containing_state(states):
    """Returns a function that takes a tweet and returns the name of the state 
    containing the given tweet's location.

    Use the geo_distance function (already provided) to calculate distance
    in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    us_states -- a dictionary from state names to positions.

    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> ny = Tweet("Welcome to New York", None, 41.1, -74)
    >>> find_state = find_containing_state(us_states)
    >>> find_state(sf)
    'CA'
    >>> find_state(ny)
    'NY'
    """
    states = states.copy()
    def find_state(tweet):
        count = 0
        x = 1
        for name, state in states.items():
            for polygon in state:
                sides = [(polygon[index],polygon[index+1])
                         for index in range(len(polygon)-1)]
                for side in sides:
                    if intersects(tweet.get_location(), side):
                        count += 1
                if count%2 != 0:
                    return name
        return
    return find_state

    
def group_tweets_by_state(tweets,find_state):
    """Return a dictionary that aggregates tweets by their nearest state center.

    The keys of the returned dictionary are state names, and the values are
    lists of tweets that appear closer to that state center than any other.

    tweets -- a sequence of tweet abstract data types

    >>> state_centers = {n: find_center(s) for n, s in us_states.items()}
    >>> find_state = find_closest_state(state_centers);
    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> ny = Tweet("Welcome to New York", None, 41, -74)
    >>> ca_tweets = group_tweets_by_state([sf, ny],find_state)['CA']
    >>> ca_tweets
    [Tweet('Welcome to San Francisco',None,38,-122)]
    """
    grouped = {}
    for tweet in tweets:
        state = find_state(tweet)
        if state in grouped:
            grouped[state].append(tweet)
        else:
            grouped[state] = [tweet]
    return grouped
    
    




