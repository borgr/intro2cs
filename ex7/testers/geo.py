"""Geography and projection utilities."""

from data import load_states
from math import sin, cos, atan2, radians, sqrt

class Position:
    def __init__(self, lat, lon):

        self.__lat = lat
        self.__lon = lon

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__lat == other.__lat and self.__lon == other.__lon
        else:
            return False

    def __str__(self):
        """Return a string representing the position."""
        return '({0}{2}, {1}{3})'.format(abs(self.__lat), abs(self.__lon),
                                        'S' if self.__lat<0 else 'N',
                                        'W' if self.__lon<0 else 'E')

    def __repr__(self):
        """Return a string representing the position."""
        return 'Position({0}, {1})'.format(float(self.__lat), float(self.__lon))

    def __iter__(self):
        """Return an iterator."""
        return iter((self.__lat, self.__lon))

    def latitude(self):
        """Return the latitudinal coordinate of a geographic position."""
        return self.__lat

    def longitude(self):
        """Return the longitudinal coordinate of a geographic position."""
        return self.__lon

    def position_to_xy(self):
        """Convert a geographic position within the US to a planar x-y point."""
        lat = self.latitude()
        lon = self.longitude()
        if lat < 25:
            return _hawaii(self)
        elif lat > 52:
            return _alaska(self)
        else:
            return _lower48(self)

def albers_projection(origin, parallels, translate, scale):
    """Return an Albers projection from geographic positions to x-y positions.

    Derived from Mike Bostock's Albers javascript implementation for D3
    http://mbostock.github.com/d3
    http://mathworld.wolfram.com/AlbersEqual-AreaConicProjection.html

    origin -- a geographic position
    parallels -- bounding latitudes
    translate -- x-y translation to place the projection within a larger map
    scale -- scaling factor
    """
    phi1, phi2 = [radians(p) for p in parallels]
    base_lat = radians(origin.latitude())
    s, c = sin(phi1), cos(phi1)
    base_lon = radians(origin.longitude())
    n = 0.5 * (s + sin(phi2))
    C = c*c + 2*n*s
    p0 = sqrt(C - 2*n*sin(base_lat))/n

    def project(position):
        lat, lon = radians(position.latitude()), radians(position.longitude())
        t = n * (lon - base_lon)
        p = sqrt(C - 2*n*sin(lat))/n
        x = scale * p * sin(t) + translate[0]
        y = scale * (p * cos(t) - p0) + translate[1]
        return (x, y)
    return project

_lower48 = albers_projection(Position(38, -98), [29.5, 45.5], [480,250], 1000)
_alaska = albers_projection(Position(60, -160), [55,65], [150,440], 400)
_hawaii = albers_projection(Position(20, -160), [8,18], [300,450], 1000)

def geo_distance(position1, position2):
    """Return the great circle distance (in miles) between two
    geographic positions.

    Uses the "haversine" formula.
    http://en.wikipedia.org/wiki/Haversine_formula

    >>> round(geo_distance(make_position(50, 5), make_position(58, 3)), 1)
    559.2
    """
    earth_radius = 3963.2  # miles
    lat1, lat2 = [radians(p.latitude()) for p in (position1, position2)]
    lon1, lon2 = [radians(p.longitude()) for p in (position1, position2)]
    dlat, dlon = lat2-lat1, lon2-lon1
    a = sin(dlat/2) ** 2  + sin(dlon/2) ** 2 * cos(lat1) * cos(lat2)
    c = 2 * atan2(sqrt(a), sqrt(1-a));
    return earth_radius * c;

us_states = load_states()
