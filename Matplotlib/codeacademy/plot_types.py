# Plot types

# Simple Bar Charts

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)

plt.show()

# Side-by-Side Bars

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#Paste the x_values code here
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]

plt.bar(store1_x, sales1)

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]
plt.bar(store2_x, sales2)

plt.show()

# Staked Bars

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
  
plt.bar(range(len(drinks)), sales1)
plt.bar(range(len(drinks)), sales2, bottom=sales1)

plt.legend(["Location 1", "Location 2"])

plt.show()

# Error Bars

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5) # error bars and capsize determined here
plt.show()

# Line plot errors

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
y_lower = [i - 0.1 * i for i in revenue]
y_upper = [i + 0.1 * i for i in revenue] # create an upper and lower error limit

plt.plot(months, revenue)
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

plt.fill_between(months, y_lower, y_upper, alpha=0.2) # the error is like a fileld in section over the line

plt.show()

# Pie Charts

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs)
plt.axis('equal') # otherwise pie chart is tilted
plt.show()

# Labelling Pies

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, autopct='%0.1f%%') # sets values to 1 d.p
plt.axis('equal')
plt.legend(payment_method_names)
plt.show()

# Or
"""
plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%') # sets values to 1 d.p
"""

# Histograms

plt.hist(sales_times, bins=20)
plt.show()

# Multiple Histograms

from script import sales_times1
from script import sales_times2

plt.hist(sales_times1, bins=20, alpha=0.4, normed=True)
plt.hist(sales_times2, bins=20, alpha=0.4, normed=True)
#plot your other histogram here

plt.show()