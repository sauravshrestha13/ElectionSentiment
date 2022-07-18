
import pandas as pd
from lib.data import DataLayer

searchTags = []

class Main:
    def getInterval(r):
        intervals = []
        length = len(r)
        print(length)
        for i in range(0,length-1):
            intervals.append([r[i],r[i+1]])
        return intervals

    def processEnglishNews(intervals):
        for interval in intervals:
            data = DataLayer.englishNewsByDate(interval[0], interval[1])
            

    def init():
        periodRange = pd.date_range(start='2017-01-01', end='2018-01-01', freq="3M")
        intervals = Main.getInterval(periodRange)
        print(intervals)
        Main.processEnglishNews(intervals)
        # processNepaliNews(intervals)
        # processTweets(intervals)

Main.init()