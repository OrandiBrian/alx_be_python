#!/usr/bin/python3

"""Python script to calculate the simple interest on a given prinicpal amount, rate of interest and time"""

# defining variables
principal = 1000 # representing $1000
rate = 0.05 # representing 5% annual interest rate
time = 3 # represeting 3 years

# simple interest
interest = principal * rate * time

# result
print("The simple interest is: {}".format(interest))
