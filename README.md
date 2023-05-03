# Coronavirus Twitter Analysis

For this project, I analyzed a dataset of all geotagged tweets from 2020 and visualized these tweets' use of Covid-19-related hashtags.

## Summary

I did this through several steps:
1. MapReduce:
    1. Partitioning the dataset into zip files for each day of the year (this was already done for me);
    1. Mapping the dataset using `map.py`,
        * Which counts the number of times a hashtag was used in each day's tweets, groups tweets by either country-of-origin or their language and, finally, pushes the grouped data in `.zip` format into the `outputs` folder,
        * (I looped over the files with `map.py` using `run_maps.sh`, a shell script); and
    1. Reducing the dataset using `reduce.py`,
        * Which combines the partitioned files in `outputs` and can create one of two combined files (based on your specification) based on country-of-origin and language-of-tweet: `reduced.country` and `reduced.lang`.
1. Visualization: 
    * With the data now combined, I then visualized it by creating graphs using the matplotlib library.
    * `visualize.py` creates bar graphs showcasing either the top ten countries or languages tweets were written from or in.
        * You can filter by one hashtag and use either `reduced.lang` or `reduced.country` as the input.
    * `alternative_reduce.py` allows for tweets to be filtered by one or more hashtags, creating line graphs instead.
        * Additionally, it creates line graphs with a line for each hashtag.

## Graphs Using `visualize.py`

I made four graphs using `visualize.py`:

#### Graph 1
I used
```
$ ./src/visualize.py --input_path=reduced_country --key='#coronavirus'
```
To output:
### Tweets Using #coronavirus (sorted by top 10 countries for 2020)
<img src=https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%23coronavirus_country.png />

#### Graph 2
I used
```
$ ./src/visualize.py --input_path=reduced_lang --key='#coronavirus'
```
To output:
### Tweets Using #coronavirus (sorted by top 9 languages for 2020)
<img src=https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%23coronavirus_language.png />

#### Graph 3
I used
```
$ ./src/visualize.py --input_path=reduced_country --key='#코로나바이러스'
```
To output: 
### Tweets Using #코로나바이러스 (sorted by top 10 countries for 2020)
<img src=https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4_country.png />

#### Graph 4
I used
```
$ ./src/visualize.py --input_path=reduced_lang --key='#코로나바이러스'
```
To output:
### Tweets Using #코로나바이러스 (sorted by top 9 languages for 2020)
<img src=https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4_language.png />

## Graphs Using `alternative_reduce`

Finally, using `alternative_reduce`, I created two more graphs:

#### Graph 1
I used
```
$ ./src/alternative_reduce.py --keys '#doctor' '#nurse' '#hospital'
```
To output:
### Number of Tweets Using #doctor, #nurse, and #hospital (2020)
![](https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%5B'%23doctor'%2C%20'%23nurse'%2C%20'%23hospital'%5D.png)
* I thought this graph was interesting as these three healthcare-related hashtags were used not in concert, but at different frequencies throughout the year, instead.

#### Graph 2
I used
```
$ ./src/alternative_reduce.py --keys '#corona' '#coronavirus'
```
To output:
### Number of Tweets Using #corona and/or #coronavirus (2020)
![](https://github.com/adamzterenyi/twitter_coronavirus/blob/master/%5B'%23corona'%2C%20'%23coronavirus'%5D.png)
* I thought this graph was interesting because #corona is more informal than #coronavirus. I was wrong in expecting the former's use to increase past #coronavirus' frequency as the pandemic set in through 2020.
