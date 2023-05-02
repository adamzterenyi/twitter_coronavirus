#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
keys = []
values = []
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items[:10]:
    print(k,':',v)
    keys = [k] + keys
    values = [v] + values
print("keys, values=", keys, values)

# make bar graph
plt.rcParams["figure.figsize"] = (11, 8)
plt.ylabel('Number of Tweets', labelpad = 10) 
plt.xticks(range(len(keys)), keys)
plt.bar(range(len(keys)), values, color = 'orange', width = 0.4)

if 'country' in args.input_path:
    plt.xlabel('Country')
    plt.savefig(f'{args.key}_country.png')
elif 'lang' in args.input_path:
    plt.xlabel('Language')
    plt.savefig(f'{args.key}_language.png')
