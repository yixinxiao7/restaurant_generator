import json
import pandas as pd

import parser_helper

# converts json strings to dataframe table
# TODO: edit so business hours are included
def get_business_data():
    with open("../data/yelp_academic_dataset_business.json") as f_p:
        all_JSON = f_p.readlines()
        i = 0
        all_data = []
        all_hours = []
        all_categories = []
        row_id = []
        for obj in all_JSON:
            temp_hours = {'Monday': 'x', 'Tuesday': 'x', 'Wednesday': 'x', 'Thursday': 'x', 'Friday': 'x', 'Saturday': 'x', 'Sunday': 'x'}
            bus_info = json.loads(all_JSON[i])
            if bus_info['is_open']:
                # hours info
                if isinstance(bus_info['hours'], dict):
                    for day, time in bus_info['hours'].items():
                        temp_hours[day] = time
                    hours = parser_helper.get_hours(temp_hours)
                else:  # hours is null in json
                    hours = ['NA','NA','NA','NA','NA','NA','NA']
                # append all data
                if isinstance(bus_info['categories'], str):
                    all_categories.append([bus_info['categories']])  # one column. format: cat1,cat2,cat3
                else:
                    all_categories.append(['NA'])
                all_hours.append(hours)   
                all_data.append([
                                 bus_info['name'], bus_info['address'], bus_info['city'], 
                                 bus_info['state'], bus_info['stars'], bus_info['review_count']
                                ])
                # append row id data
                row_id.append(bus_info['business_id'])
            i += 1
        # create dataframe table
        all_data = pd.DataFrame(
                                all_data, 
                                columns=['name', 'address', 'city', 'state', 'stars', 'review_count'],
                                index=row_id
                               )
        time_data = pd.DataFrame(
                                 all_hours,
                                 columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                                 index=row_id
                                )
        category_data = pd.DataFrame(
                                 all_categories,
                                 columns=['categories'],
                                 index=row_id
                                )
        return all_data, time_data, category_data
