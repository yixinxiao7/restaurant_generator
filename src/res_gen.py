import numpy as np
import pandas as pd
import random

from recommender import Recommender
from dictionaries import states
import parser


def select_location(df, state, city):
    state_acr = states[state]
    return df[(df.state == state_acr) & (df.city == city)]


def select_range(df, lower_range, upper_range):
    return df[(df.stars >= lower_range) & (df.stars <= upper_range)]


# returns lists of restaurants with any one of the desired categories.
def select_categories(df, categories):
    # lower words in categories
    lower_categories = []
    for word in categories:
        lower_categories.append(word.lower())
    res_list = set()
    skip = False
    res_index = 0
    for cats in df.categories:
        all_cats = cats.split(",")
        for cat in all_cats:
            mod_cat = (cat.lstrip()).lower()
            for desired_cat in lower_categories: #O(1)
                if(mod_cat == desired_cat):
                    res_list.add(res_index)
                    skip = True
                    break
            if skip:
                break
        skip = False
        res_index += 1
    return res_list


def get_place_ids(all_data_df, category_data_df, categories):
    def grab_filtered_places_id(df):
        return list(df.index)
    filtered_places_busids = grab_filtered_places_id(all_data_df)
    selected_cats = category_data_df.loc[filtered_places_busids]
    return select_categories(selected_cats, categories)


def select_ran_res(df, res_list, time_data_df):
    if len(res_list) != 0:
        rand_res = random.choice(res_list)
        new_df = df.iloc[[rand_res]]
        times = time_data_df.loc[new_df.index[0]]

        print("Store Name: ")
        print(new_df.name[0])
        print("Store hours:")
        for day, time in zip(['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'], times):
            print(str(day) + ': ' + str(time))
    else:
        print("No restaurants found.")



def show_all_res(df, res_list):
    if len(res_list) != 0:
        new_df = df.iloc[res_list]
        for name in new_df.name:
            print(name)
    else:
        print("No restaurants found.")


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
    all_data_df = select_range(all_data_df, float(bounds[0]), float(bounds[1]))
    place_ids = get_place_ids(all_data_df, category_data_df, categories)

    print("Enter 0 for a random restaurant, and 1 for a list of restaurants")
    choice = input()
    if int(choice) == 0:
        select_ran_res(all_data_df, list(place_ids), time_data_df)
        print("See recommendation? <Y/N>")
        recommendation = input()
        if recommendation == "Y":
            recommender = Recommender(all_data_df, list(place_ids))
            recommender.print_random()
    else:
        show_all_res(all_data_df, list(place_ids))
    
if __name__ == "__main__":
    main()
