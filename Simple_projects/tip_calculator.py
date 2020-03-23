# Tip calculator

# Set variables
meal = 44.50
restaurant_tax = 0.0675
tip = 0.15

# Meal calculation cost
meal += meal * restaurant_tax

# Meal + tip
total = meal + (meal * tip)

# Prints total as a float with 2dp
print ("%.2f" % total)