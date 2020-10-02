from read_country_module import read_country

import pandas as pd
class read_state(read_country):
    state_stats = pd.DataFrame()
    #calculates the number of cases and deaths for each state 
    def per_state_stats(self):
        self.state_stats = self.data_frame.loc[self.data_frame.groupby('state')['year_month_day'].idxmax()]
        self.state_stats = self.state_stats[['state', 'cases', 'deaths']]
 
    
    







