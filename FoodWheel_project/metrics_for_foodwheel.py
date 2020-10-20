# Metrics for FoodWheel

"""
FoodWheel is a startup delivery service that takes away the struggle of deciding where to eat! 
FoodWheel picks you an amazing local restaurant and lets you order through the app. 
Senior leadership is getting ready for a big board meeting, and as the resident Data Analyst, 
you have been enlisted to help decipher data and create a presentation to answer several key questions:

What cuisines does FoodWheel offer? Which areas should the company search for more restaurants to partner with?
How has the average order amount changed over time? What does this say about the trajectory of the company?
How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?
"""

# What cuisiner does FoodWheel offer?

"""
The board wants to make sure that FoodWheel offers a wide, diverse, variety of restaurants. 
Having many different options makes customers more likely to come back. 
You’ve been provided with a CSV, restaurants.csv , which contains all of the restaurants that partner with FoodWheel.

Let’s create pie chart showing the different types of cuisines available on FoodWheel.
"""

from matplotlib import pyplot as plt
import pandas as pd

# Load the csv file into a DataFrame
restaurants = pd.read_csv('restaurants.csv')
print(restaurants.head())

# How many unique cuisines are on offer?
cuisine_options_count = restaurants.cuisine.nunique()

# Count the numebr of restaurants for each cuisine
cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()
print(cuisine_counts)

# store values in a list
cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values

# create pie chart
plt.pie(counts, autopct='%d%%', labels=cuisines)
plt.axis('equal')
plt.title('Cuisines that FoodWheel offers')
plt.show()

# Orders over Time

"""
FoodWheel is a relatively new startup. They launched in April, and have grown more popular since then. 
Management suspects that the average order size has increased over time. 
They’d like you to investigate if this claim is true and answer these questions:

How has the average order amount changed over time?
What does this say about the trajectory of the company?
"""

orders = pd.read_csv('orders.csv')

print orders.head()

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])

print orders.head()

avg_order = orders.groupby('month').price.mean().reset_index()

std_order = orders.groupby('month').price.std().reset_index()

