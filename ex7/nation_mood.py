#############################################################
# FILE : nation_mood.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex7 200132014
# DESCRIPTION:nation wide tweet functions
#############################################################
from data import load_tweets
from geo import us_states, Position, geo_distance
from tweet import Tweet
from geo_tweet_tools import find_center, find_closest_state, group_tweets_by_state

def most_talkative_state(tweets,find_state):
    """Return the state that has the largest number of tweets containing term.
    >>> state_centers = {n: find_center(s) for n, s in us_states.items()}
    >>> tweets = load_tweets('texas')
    >>> find_state = find_closest_state(state_centers);
    >>> most_talkative_state(tweets,find_state)
    'TX'
    >>> tweets = load_tweets('sandwich')
    >>> most_talkative_state(tweets,find_state)
    'NJ'
    """
    most_tweets = -float("inf")
    most_state = None
    grouped = group_tweets_by_state(tweets,find_state)
    for state in grouped:
        state_tweets = len(grouped[state])
        if most_tweets < state_tweets:
           most_tweets = state_tweets
           most_state = state
    return most_state
    


def average_sentiments(tweets_by_state,word_sentiments):
    """Calculate the average sentiment of the states by averaging over all
    the tweets from each state. Return the result as a dictionary from state
    names to average sentiment values (numbers).

    If a state has no tweets with sentiment values, leave it out of the
    dictionary entirely.  Do NOT include states with no tweets, or with tweets
    that have no sentiment, as 0.  0 represents neutral sentiment, not unknown
    sentiment.

    tweets_by_state -- A dictionary from state names to lists of tweets
    """
    avarage = {}
    for state in tweets_by_state.keys():
        sentiments = []
        for tweet in tweets_by_state[state]:
            sentiment = tweet.get_sentiment(word_sentiments)
            if sentiment is not None:
                sentiments.append(Sentiment)
        if sentiments:
            print(state, sentiments)
            avarage.update({state: sum(sentiments)/len (sentiments)})
    return avarage

def group_tweets_by_hour(tweets):
    """Return a list of lists of tweets that are gouped by the hour 
    they were posted.

    The indexes of the returned list represent the hour when they were posted
    - the integers 0 through 23.

    tweets_by_hour[i] is the list of all
    tweets that were posted between hour i and hour i + 1. Hour 0 refers to
    midnight, while hour 23 refers to 11:00PM.

    To get started, read the Python Library documentation for datetime 
    objects:
    http://docs.python.org/py3k/library/datetime.html#datetime.datetime

    tweets -- A list of tweets to be grouped
    """
    return [[tweet for tweet in tweets
                  if tweet.get_time().hour == hour]
            for hour in range(24)]


