#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# car MATRIX Generation #

import pandas as pd
import numpy as np

def generate_car_matrix(file_path):
    df = pd.read_csv(file_path)
    return df  # Add this line to return the DataFrame

df1 = generate_car_matrix("A:/mapupdataset/dataset-1.csv")

# Pivot the DataFrame using 'id_1' as columns and 'id_2' as index, with 'car' values as data
df2 = df1.pivot(index='id_1', columns='id_2', values='car')

# Replace NaN values with zero
df2.fillna(0, inplace=True)

# Extract a subset for 'id_1' values 801 to 806 and 'id_2' values 801 to 806
subset_df = df2.loc[801:806, 801:806]

subset_df = subset_df * 2

np.fill_diagonal(subset_df.values, 0)

print(subset_df)



#Bus Count Index Retrieval#
import pandas as pd

def get_bus_indexes(data_frame):
    mean_bus_value = data_frame['bus'].mean()

  
    bus_indexes = data_frame[data_frame['bus'] > 2 * mean_bus_value].index.tolist()


    bus_indexes.sort()

    return bus_indexes
dataset = pd.read_csv("A:/mapupdataset/dataset-1.csv")  
bus_indices = get_bus_indexes(dataset)
print(bus_indices)



#Route Filtering#

import pandas as pd

def filter_routes(data_frame):
    # Calculate the mean value of the 'truck' column
    mean_truck_value = data_frame['truck'].mean()

    # Filter rows where the mean of 'truck' column is greater than 7
    filtered_routes = data_frame[data_frame['truck'] > 7]['route'].tolist()

    # Remove duplicate routes and sort the list in ascending order
    filtered_routes = sorted(set(filtered_routes))

    return filtered_routes


dataset = pd.read_csv("A:/mapupdataset/dataset-1.csv")
filtered_routes_list = filter_routes(dataset)
print(filtered_routes_list)



