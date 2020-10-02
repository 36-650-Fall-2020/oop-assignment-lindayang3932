import sys
from read_state_module import read_state

import pandas as pd
class read_county(read_state):
    county_state = pd.DataFrame()
    county_name = ''
    state_name = ''
    # obtain user selection and save
    def set_user_selection(self, county, state):
        self.county_name = county
        self.state_name = state
    # filters data set for the county and state selected by user. Returns cases and deaths for that county and state
    def per_state_county(self):
        self.county_state = self.data_frame.loc[(self.data_frame['county'].str.lower() == self.county_name.lower()) & (self.data_frame['state'].str.lower() == self.state_name.lower())]
        self.county_state = self.county_state.loc[self.county_state.year_month_day == self.county_state.year_month_day.max()]
        self.county_state = self.county_state[['state', 'county', 'cases', 'deaths']]
