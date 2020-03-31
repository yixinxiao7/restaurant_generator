import json
import pandas as pd

# converts json strings to dataframe table
# TODO: edit so business hours are included
def get_business_data():
    with open("../data/yelp_academic_dataset_business.json") as f_p:
        all_JSON = f_p.readlines()
        i = 0
        all_data = []
        row_id = []
        for obj in all_JSON:
            bus_info = json.loads(all_JSON[i])
            if bus_info['is_open']:
                all_data.append([
                                 bus_info['name'], bus_info['address'], bus_info['city'], 
                                 bus_info['state'], bus_info['stars'], bus_info['review_count']
                                ])
                row_id.append(bus_info['business_id'])
            i += 1
        # create dataframe table
        return pd.DataFrame(
                            all_data, 
                            columns=['name', 'address', 'city', 'state', 'stars', 'review_count'],
                            index=row_id
                           )

        
        
