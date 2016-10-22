#############################################################
# FILE : tweet.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex7 200132014
# DESCRIPTION:tweet class
#############################################################
from doctest import run_docstring_examples
from geo import Position, albers_projection, geo_distance
import datetime
import string
import functools

class Tweet:
    def __init__(self, text, time, lat, lon):
        """ This function initializes a Tweet

        Args:
        text: a string, the text of the tweet.
        time: a datetime object, when the tweet was posted.
        latitude: a floating-point number, the latitude of the tweet's location.
        longitude: a floating-point number, the longitude of the tweet's location.
        """
        self.text = text
        self.time = time
        self.Position = Position(lat, lon)
        self.words = None
        self.sentiment = None

        
    def get_words(self):
        """Return the words in a tweet, not including punctuation.
        """
        if not self.words:
            self.words = list("".join([char.lower()
                                       if char in string.ascii_letters
                                       else " "
                                       for char in self.text]).split())
        return self.words


    def get_text(self):
        """Return the text of the tweet."""
        return self.text


    def get_time(self):
        """Return the datetime that represents when the tweet was posted."""
        return self.time


    def get_location(self):
        """Return a Position (see geo.py) that represents the tweet's location."""
        return self.Position


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.get_text() == other.get_text() and
                    self.get_location() == other.get_location() and
                    self.get_time() == other.get_time())
        else:
            return False


    def __str__(self):
        """Return a string representing the tweet."""
        return '"{0}" @ {1} : {2}'.format(self.get_text(), 
                                          self.get_location(), 
                                          self.get_time())

    #These lines are too long, but they are not mine...
    def __repr__(self):
        """Return a string representing the tweet."""
        return 'Tweet({0}, {1}, {2}, {3})'.format(*map(repr,(self.get_text(),
                                                             self.get_time(),
                                                             self.get_location().latitude(),
                                                             self.get_location().longitude())))


    
    def get_sentiment(self,word_sentiments, count = [0]):
        """ Return a sentiment representing the degree of positive or negative
        sentiment in the given tweet, averaging over all the words in the tweet
        that have a sentiment value.
        """
        #  This function recalculate the sentiment each time,
        #  saving memory but taking more time.
        #  If time is more important it is possible to save
        #  the answers, but each word sentimens will be saved
        #  taking a lot of space if changed often.
        listed = [word_sentiments[word] for word in self.get_words()
                    if word in word_sentiments]
        if not listed:
            return
        return sum(listed)/len(listed) if word_sentiments else None
