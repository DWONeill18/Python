# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  message = "The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars."
  print(message)
  return estimated_cost

def insurance_difference(insurance_cost_A, insurance_cost_B):
  difference = insurance_cost_A - insurance_cost_B
  print("The difference in insurance cost is " + str(difference) + " dollars.")
  return difference


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)

# Initial variables for Omar
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

# Difference between the two
insurance_difference(maria_insurance_cost, omar_insurance_cost)