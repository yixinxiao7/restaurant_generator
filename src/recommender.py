import numpy as np
import pandas as pd

import random


class Recommender:
    def __init__(self, df, place_ids):
        self._df = df
        self._place_ids = place_ids
    
    def print_random(self):       
        ran_choice = random.choice(self._place_ids)
        choice = self._df.iloc[ran_choice]
        print('Restaurant: ' + str(choice[0]))
        print('Address: ' + str(choice[1]) + ', ' + str(choice[2]) + ' ' + str(choice[3]))
        print('Rating: ' + str(choice[4]))
