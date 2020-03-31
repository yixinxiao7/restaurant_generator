import numpy as np
import pandas as pd
import random

import parser

from dictionaries import states

# assumes csv file exists

def select_range(df, lower_range, upper_range):
    return df[df.stars >= lower_range and df.stars <= upper_range]

def select_location(df, state, city):
    state_acr = states[state]
    return df[df.state == state_acr and df.city == city]

def select_zipCode(df, zipcode):
    return df[df.postal_code == zipcode]

# returns lists of restaurants with any one of the desired categories
def select_categories(df, categories):
    res_list = set()
    skip = False
    res_index = 0
    for cats in df.categories:
        all_cats = cats.split(";")
        for cat in all_cats:
            for desired_cat in categories: #O(1)
                if(cat == desired_cat):
                    res_list.add(res_index)
                    skip = True
                    break
            if skip:
                break
        skip = False
        res_index += 1
    return res_list

def select_ran_res(df, res_list):
    res_list = np.array(res_list)
    rand_res = random.choice(res_list)
    return (df.iloc(rand_res)).name

def show_all_res(df, res_list):
    res_list = np.array(res_list)
    new_df = df.iloc(res_list)
    for name in new_df.name:
        print(name)

def main():

    # test
    df = parser.get_business_data()
    print(df.head())
    exit(1)
    yelp_business = pd.read_csv("./yelp_data/yelp_business.csv")
    
    print("Enter a state, no abbreviations") #fix this
    state = input()
    print("Enter a city")
    city = input()
    print("Enter a lower and upper bound for a desired rating of the restaurant, in this format: lower_bound,upper_bound")
    bounds = input()
    bounds = bounds.split(",")
    print("Enter a zipcode, if desired. If not, enter 0")
    zipcode = 0  # default value
    zipcode = input()
    print("Enter food categories, split with commas, no space.")
    categories = input()
    categories = categories.split(",")

    yelp_business = select_location(yelp_business, state, city)
    yelp_business = select_range(yelp_business, bounds[0], bounds[1])
    if zipcode != 0:
        yelp_business = select_zipCode(yelp_business, zipcode)
    yelp_business_array = select_categories(yelp_business, categories)
    
    print("Enter 0 for a random restaurant, and 1 for a list of restaurants")
    choice = input()
    if choice == 0:
        select_ran_res(yelp_business, yelp_business_array)
    else:
        show_all_res(yelp_business, yelp_business_array)
    
if __name__ == "__main__":
    main()
