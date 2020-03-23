# Supermarket project

# List of things we want to buy
shopping_list = ["banana", "orange", "apple"]

# Dictionaries of current stock and their prices in the store
stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Function that loops through each item in our list, checks if it's in stock, then adds the price to our total
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total = total + prices[item]
      stock[item] -= 1
  return total

# Prints out the total of our shopping list
print compute_bill(shopping_list)