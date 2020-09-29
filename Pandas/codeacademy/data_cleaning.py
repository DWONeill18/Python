# Data Cleaning with Pandas

# Diagnose the Data

import codecademylib3_seaborn
import pandas as pd

df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")

print(df1.head())
print(df2.head())

print(df1.info())
print(df2.info())

print(df1.describe())
print(df2.describe())

print(df1.columns)
print(df2.columns)

#print(df1.value_counts())
#print(df2.value_counts())


# Dealing with Multiple Files

import glob

student_files = glob.glob("exams*.csv") # opening multiple files usign regex in glob library

df_list = []

for file in student_files:
  data = pd.read_csv(file)
  df_list.append(data)

students = pd.concat(df_list)

print(students)
print(len(students))

# Reshaping your Data

print(students.columns)
students = pd.melt(frame=students, id_vars=['full_name','gender_age','grade'], value_vars=['fractions', 'probability'], value_name='score', var_name='exam')

print(students.head())
print(students.columns)
print(students.exam.value_counts())

# Dealing with Duplicates

from students import students

#print(students)
duplicates = students.duplicated()  
#print(duplicates.value_counts())

students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.value_counts())


# Splitting by Index

from students import students

print(students)

print(students.columns) # Looks like gender_age column contains two sets of data
print(students.gender_age.head())

students['gender'] = students['gender_age'].str[0:1] # Seaprating gender and age into different columns
students['age'] = students['gender_age'].str[1:3]

print(students.head())

students = students[['full_name', 'grade', 'exam', 'score', 'gender', 'age']] # Selecting only the relavent columns
print(students.head())


# Splitting by Character

print(students)

name_split = students.full_name.str.split(' ') # Create a series object that splits by ""

students['first_name'] = name_split.str.get(0) # create a column that takes the first item from name_split
students['last_name'] = name_split.str.get(1) # second item

print(students.head())

# Looking at data types

print(students.dtypes) # To see the dtype of each column

print(students.score.mean()) # Doesn't work cause score has type object NOT int


# String Parsing

students.score = students['score'].replace('[\%,]', '', regex=True) # Removes the % via a regex

students.score = pd.to_numeric(students.score) # Converts string to an float64

###############

print(students.grade.head())

students.grade = students.grade.str.split('(\d+)', expand=True)[1] # Using regex to just get the number from the string

print(students.dtypes)

students.grade = pd.to_numeric(students.grade) # Convert object to float
avg_grade = students.grade.mean() # Now we can calculate the average

print(avg_grade)

# Missing Values

score_mean = students.score.mean()

students = students.fillna(value=
{
  "score":0
})
# Fills nans with a value of our choice

score_mean_2 = students.score.mean()
print(score_mean_2) # Can now calculate a better mean 