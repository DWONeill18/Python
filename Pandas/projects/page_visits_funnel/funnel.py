# Page Visits Funnel

import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# Funnel for Cool T-shirts Inc

"""
Inspect the DataFrames using print and head
"""

print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))

"""
Combine visits and cart using a left merge.
"""

visits_cart = pd.merge(
  visits,
  cart,
  how='left'
)

"""
How long is your merged DataFrame?
"""

print(len(visits_cart))
# 2000 rows x 3 columns - 2000 different ids

"""
How many of the timestamps are null for the column cart_time?

What do these null rows mean?
"""

null_values = visits_cart[visits_cart.cart_time.isnull()]
print(len(null_values))

# 1652 null values, they-re null as the customer didn't add anything into their cart

"""
What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
"""

no_buy_tshirt = float(len(null_values)) / (len(visits_cart))
print(no_buy_tshirt)

# 82.6%

"""
Repeat the left merge for cart and checkout and count null values. 
What percentage of users put items in their cart, but did not proceed to checkout?
"""

cart_checkout = pd.merge(
  cart,
  checkout,
  how='left'
)

checkout_null_values = cart_checkout[cart_checkout.checkout_time.isnull()]
print(len(checkout_null_values))

cart_no_checkout = float(len(checkout_null_values)) / (len(cart_checkout))
print(cart_no_checkout)

# 25.3 % put items in the cart but don't checkout

"""
Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data.
"""

all_data = visits_cart.merge(checkout, how='left').merge(purchase, how='left')

print(all_data.head(5))

"""
What percentage of users proceeded to checkout, but did not purchase a t-shirt?
"""

purchase_null_values = all_data[all_data.checkout_time.isnull()]

checkout_no_purchase = float(len(purchase_null_values)) / (len(all_data))
print(checkout_no_purchase)

# 74.8% of users proceeded to checkout but didnt purchase

"""
Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?

How might Cool T-Shirts Inc. change their website to fix this problem?
"""

# visits to cart has the highest percentage of null values
# 



# Average Time to Purchase

"""
Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. 
"""

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

average_time = all_data.time_to_purchase.mean()
print(average_time)

# 0 days 00:43:53.360160

