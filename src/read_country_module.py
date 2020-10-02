import sys
from read_module import read 

import pandas as pd
class read_country(read):
    file = ""
    data_frame  = pd.DataFrame()
    USA_stats = pd.DataFrame()
    def __init__(self, file):
        self.file = file
    #reads file and processes the csv 
    def read_file(self):
        self.data_frame = pd.read_csv(self.file)
        self.data_frame['year_month_day'] = pd.to_datetime(self.data_frame['date'])
    #reformats the data column 
    def date_reformat(self):
        self.data_frame[['year','month']]= self.data_frame['date'].str.split('-', n = 1, expand = True)
        self.data_frame[['month','day']]= self.data_frame['month'].str.split('-', n = 1, expand = True)

    #calculates country statistics across all months
    def country_stats(self):
        self.USA_stats = self.data_frame.loc[self.data_frame.year_month_day == self.data_frame.year_month_day.max()]
 


#take the recent death and cases record


