# Import the Pandas library.
import pandas as pd

# My chosen dataset with the read_csv command.
mc = pd.read_csv("Mall_Customers.csv", header=0)

print(mc)


# Question 1: What is the highest (max) spending score in this dataset? Lowest (min) spending score?

# Maximum spending score
spending_score_max = mc['Spending_Score'].max()
print("Maximum spending score: ", spending_score_max)

# Minimum spending score
spending_score_min = mc['Spending_Score'].min()
print("Minimum spending score: ", spending_score_min)
print()

# Question 2: What is the average customer age in this dataset?
customer_age_avg = mc['Age'].mean()
print("Average customer age: ")
print(round(customer_age_avg))
print()

# Stretch Challenge
# Question 3: What is the total count of male and female customers in this dataset?
print(mc.Genre.value_counts())  # value_counts returns a series containing counts of unique values
