# Sal's Shipping

"""
Sal’s Shippers has several different options for a customer to ship their package. 
They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. 
Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. 
They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
"""

"""
Write a program that asks the user for the weight of their package and then tells them which method of shipping 
is cheapest and how much it will cost to ship their package using Sal’s Shippers.
"""

def ground_shipping(weight):
  if weight > 10:
    return (weight * 4.75) + 20.00
  elif weight > 6:
    return (weight * 4.00) + 20.00
  elif weight > 2:
    return (weight * 3.00) + 20.00
  else:
    return (weight * 1.50) + 20.00

print(ground_shipping(8.4))

premium_ground_shipping = 125.00

def drone_shipping(weight):
  if weight > 10:
    return (weight * 14.25)
  elif weight > 6:
    return (weight * 12.00)
  elif weight > 2:
    return (weight * 9.00)
  else:
    return (weight * 4.50)

print(drone_shipping(1.5))

def info(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_ground_shipping

  if ground <= drone and ground <= premium:
    return "ground: " + str(ground)
  elif drone <= ground and drone <= premium:
    return "drone: " + str(drone)
  else:
    return "premium: " + str(premium)

"""
Great job! Now, test your function!

What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

"""

print(info(4.8))
print(info(41.5))

