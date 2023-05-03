# Coronavirus Twitter Analysis

For this project, I analyzed a dataset of all geotagged tweets from 2020 andvisualized these tweets' use of Covid-19 related hashtags.

## Summary

I did this through several steps:
1. MapReduce:
    1. Partitioning the dataset into zip files for each day of the year (this was already done for me);
    1. Mapping the dataset using `map.py`,
        * Whichs count the number of times a hashtag was used in each day's tweets, groups tweets by either countries-of-origin or their languages and, finally, pushes the grouped data into the `outputs` folder;
        * (I looped over the files using `run_maps.sh`, a shell script)
    1. Reducing the dataset using `reduce.py`,
        * Which combines the partitioned files in `outputs` and creates two combined files based on country-of-origin and language-of-tweet: `reduced.country` and `reduced.lang`.
1. Visualization: 
    * With the data now combined, I then visualized it by creating graphs using the matplotlib library.
    * `visualize.py` creates bar graphs showcasing either the top ten countries or languages tweets were written.
    * `alternative_reduce.py` allows for tweets to be filtered by one or more hashtags, creating line graphs instead.

## Graphs

I made six graphs: four using `visualize.py` and two using `alternative_reduce.py`.

I used
```
$ ./src/visualize.py --input_path=reduced_country --key='#coronavirus'
```
To output:
### Tweets Using #coronavirus (sorted by top 10 countries for 2020)
<img src=https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%23coronavirus_country.png />

I used
```
$ ./src/visualize.py --input_path=reduced_lang --key='#coronavirus'
```
To output:
### Tweets Using #coronavirus (sorted by top 9 languages for 2020)
<img src=https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%23coronavirus_language.png />

I used
```
$ ./src/visualize.py --input_path=reduced_country --key='#코로나바이러스'
```
To output: 
### Tweets Using #코로나바이러스 (sorted by top 10 countries for 2020)
<img src=https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4_country.png />

I used
$ ./src/visualize.py --input_path=reduced_lang --key='#코로나바이러스'
To output:
### Tweet Using #코로나바이러스 (sorted by top 10 languages for 2020)
<img src=https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4_language.png />
