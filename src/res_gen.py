import numpy as np
import pandas as pd
import random

from dictionaries import states
import parser


def select_location(df, state, city):
    state_acr = states[state]
    return df[df.state == state_acr and df.city == city]

def select_range(df, lower_range, upper_range):
    return df[df.stars >= lower_range and df.stars <= upper_range]

# returns lists of restaurants with any one of the desired categories.
# TODO: CHANGE THIS TO NOT RETURN INDICES BUT INSTEAD IDS
def select_categories(df, categories):
    res_list = set()
    skip = False
    res_index = 0
    for cats in df.categories:
        all_cats = cats.split(",")
        print(all_cats)
        exit(1)
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
    all_data_df, time_data_df, category_data_df = parser.get_business_data()
    print("Enter a state, no abbreviations") #fix this
    state = input()
    print("Enter a city")
    city = input()
    print("Enter a lower and upper bound for a desired rating of the restaurant, in this format: lower_bound,upper_bound")
    bounds = input()
    bounds = bounds.split(",")
    print("Enter food categories, split with commas, no space.")
    categories = input()
    categories = categories.split(",")

    all_data_df = select_location(all_data_df, state, city)
    all_data_df = select_range(all_data_df, bounds[0], bounds[1])
    place_ids = select_categories(category_data_df, categories)
    # yelp_business_array = select_categories(yelp_business, categories)
    
    print("Enter 0 for a random restaurant, and 1 for a list of restaurants")
    choice = input()
    if choice == 0:
        select_ran_res(yelp_business, yelp_business_array)
    else:
        show_all_res(yelp_business, yelp_business_array)
    
if __name__ == "__main__":
    main()
