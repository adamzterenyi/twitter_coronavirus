#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# dataset creation

total = {}
number_of_tweets = 0

for hashtag in args.input_paths:
    days_tweets = {}
    for day in sorted(os.listdir('outputs')):
        output = os.path.join('outputs', day)
        date = output[18:26]
        if os.path.isfile(output):
            if 'lang' in output:
                with open(output) as f:
                    tweets = json.load(f)
                    for k in tweets:
                        if hashtag == k:
                            for key in tweets[k]:
                                number_of_tweets += tweets[k][key]
                days_tweets[date] = number_of_tweets
                # print("number_of_tweets=", number_of_tweets)
    total[hashtag] = days_tweets

# plotting time
for hashtag, total_days in total.items():
    keys = []
    values = []
    dates = []
    for k, v in total_days.items():
        keys.append(k)
        values.append(v)
        dates.append(k)
    plt.plot(range(len(keys)), values, label = hashtag)
plt.rcParams["figure.figsize"] = [12, 10]
plt.xlabel('Date', labelpad = 10)
plt.ylabel('Number of Tweets Using Hashtag')
plt.xticks(range(len(keys))[::30], dates[::30], rotation = 45)
plt.legend()
plt.subplots_adjust(bottom=0.21)
plt.savefig(f'{args.input_paths}.png')
