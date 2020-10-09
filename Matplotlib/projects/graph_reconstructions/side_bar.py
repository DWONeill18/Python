# Side by side Bar graph

from matplotlib import pyplot as plt

# Data in lists
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

# Function to determine where to put the bars when side by side
def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

# creating the bars x value
school_a_x = create_x(2, 0.8, 1, len(middle_school_a))
school_b_x = create_x(2, 0.8, 2, len(middle_school_b))

# create figure and axis
plt.figure(figsize=(10, 8))
ax = plt.subplot()
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)

# create a list of x-values for where we will put xticks
middle_x = [(i + j) / 2.0 for i, j in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

# Label title and axis
plt.legend(['Middle School A', 'Middle School B'])
plt.title("Test Averages on Different Units")
plt.xlabel("Unit")
plt.ylabel("Test Average")

# Save and show plot
plt.savefig("my_side_by_side.png")
plt.show()