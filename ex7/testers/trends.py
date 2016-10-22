#!/usr/bin/env python3
"""Visualizing Twitter Sentiment Across America"""

from data import load_tweets, load_sentiments
from datetime import datetime
from doctest import run_docstring_examples
from maps import draw_state, draw_name, draw_dot, wait, message, clear, get_img_copy
from string import ascii_letters
from geo import us_states,geo_distance,Position
from ucb import main, trace, interact, log_current_line
from tweet import Tweet
from geo_tweet_tools import find_centroid,find_center,find_closest_state,find_containing_state,group_tweets_by_state
from nation_mood import most_talkative_state,average_sentiments,group_tweets_by_hour
from imgtools import MapImage

# Interaction (You don't need to read this section of the program):

def print_sentiment(text = 'Are you virtuous or verminous?'):
    """Print the words in text, annotated by their sentiment scores."""
    word_sentiments = load_sentiments()
    tweet = Tweet(text.lower(),datetime.now(),0,0)
    #words = extract_words(text.lower())
    words = tweet.get_words()
    assert words, 'No words extracted from "' + text + '"'
    layout = '{0:>' + str(len(max(words, key=len))) + '}: {1:+}'
    for word in words:
        s = word_sentiments.get(word,None)
        if s != None:
            print(layout.format(word, s))

def draw_centered_map(center_state='TX', n=10, canvas=None):
    """Draw the n states closest to center_state."""
    us_centers = {n: find_center(s) for n, s in us_states.items()}
    center = us_centers[center_state.upper()]
    dist_from_center = lambda name: geo_distance(center, us_centers[name])
    for name in sorted(us_states.keys(), key=dist_from_center)[:int(n)]:
        draw_state(us_states[name], canvas=canvas)
        draw_name(name, us_centers[name], canvas=canvas)
    draw_dot(center, 1, 10, canvas=canvas)  # Mark the center state with a red dot
    wait(canvas=canvas)

def draw_state_sentiments(state_sentiments={}, canvas=None):
    """Draw all U.S. states in colors corresponding to their sentiment value.

    Unknown state names are ignored; states without values are colored grey.

    state_sentiments -- A dictionary from state strings to sentiment values
    """
    if canvas: clear(canvas=canvas)
    for name, shapes in us_states.items():
        sentiment = state_sentiments.get(name, None)
        draw_state(shapes, sentiment, canvas=canvas)
    for name, shapes in us_states.items():
        center = find_center(shapes)
        if center is not None:
            draw_name(name, center, canvas=canvas)

def draw_map_for_term(find_state, term='my job', canvas=None):
    """Draw the sentiment map corresponding to the tweets that contain term.

    Some term suggestions:
    New York, Texas, sandwich, my life, justinbieber
    """

    word_sentiments = load_sentiments()
    tweets = load_tweets(term)
    tweets_by_state = group_tweets_by_state(tweets, find_state)
    state_sentiments = average_sentiments(tweets_by_state,word_sentiments)
    draw_state_sentiments(state_sentiments, canvas=canvas)
    for tweet in tweets:
        s = tweet.get_sentiment(word_sentiments)
        if s != None:
            draw_dot(tweet.get_location(), s, canvas=canvas)
    wait(canvas=canvas)

def draw_map_by_hour(find_state, term='my job', pause=0.5, canvas=None, imglist=None):
    """Draw the sentiment map for tweets that match term, for each hour."""

    word_sentiments = load_sentiments()
    tweets = load_tweets(term)
    tweets_by_hour = group_tweets_by_hour(tweets)
    
    for hour in range(24):
        current_tweets = tweets_by_hour[hour]
        tweets_by_state = group_tweets_by_state(current_tweets, find_state)
        state_sentiments = average_sentiments(tweets_by_state,word_sentiments)
        draw_state_sentiments(state_sentiments, canvas=canvas)
        message("{0:02}:00-{0:02}:59".format(hour), canvas=canvas)
        wait(pause, canvas=canvas)
        if imglist is not None:
            imglist.append(get_img_copy(canvas))

def run_doctests(names):
    """Run verbose doctests for all functions in space-separated names."""
    g = globals()
    errors = []
    for name in names.split():
        if name not in g:
            print("No function named " + name)
        else:
            if run_docstring_examples(g[name], g, True) is not None:
                errors.append(name)
    if len(errors) == 0:
        print("Test passed.")
    else:
        print("Error(s) found in: " + ', '.join(errors))

@main
def run(*args):
    """Read command-line arguments and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Run Trends")
    parser.add_argument('--print_sentiment', '-p', action='store_true')
    parser.add_argument('--run_doctests', '-t', action='store_true')
    parser.add_argument('--draw_centered_map', '-d', action='store_true')
    parser.add_argument('--draw_state_sentiments', '-s', action='store_true')
    parser.add_argument('--draw_map_for_term', '-m', action='store_true')
    parser.add_argument('--draw_map_by_hour', '-b', action='store_true')
    parser.add_argument('--containing_state', '-c', action='store_true')
    parser.add_argument('--file', '-f', type=str, default=None)
    parser.add_argument('text', metavar='T', type=str, nargs='*',
                        help='Text to process')
    args = parser.parse_args()

    if (args.__dict__['containing_state']):
            find_state = find_containing_state(us_states)
    else:
        us_centers = {n: find_center(s) for n, s in us_states.items()}
        find_state = find_closest_state(us_centers)
    
    if args.__dict__['file']:
        canvas = MapImage(960,500)
    else:
        canvas = None
    for name, execute in args.__dict__.items():
        if name != 'text' and name != 'containing_state' and name != 'file' and execute:
            if name == 'draw_map_for_term':
                draw_map_for_term(find_state, ' '.join(args.text), canvas=canvas)
                if canvas: canvas._img.save(args.file+'.png', "PNG")
            elif name == 'draw_map_by_hour':
                imglist = [] if canvas else None
                draw_map_by_hour(find_state, ' '.join(args.text), canvas=canvas, imglist=imglist)
                if canvas:
                    for i in range(24):
                        imglist[i].save(args.file+'_'+str(i).zfill(2)+'.png', "PNG")
            elif name == 'draw_centered_map':
                draw_centered_map(' '.join(args.text), canvas=canvas)
                if canvas: canvas._img.save(args.file+'.png', "PNG")
            elif name == 'draw_state_sentiments': 
                draw_state_sentiments(average_sentiments(group_tweets_by_state(load_tweets(' '.join(args.text)), find_state),load_sentiments()), canvas=canvas) 
                wait(canvas=canvas)
                if canvas: canvas._img.save(args.file+'.png', "PNG")
            else:
                globals()[name](' '.join(args.text))
