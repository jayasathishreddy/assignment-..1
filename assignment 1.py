#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Exercise 1: Arithmetic Operations",
#Take two numbers as input and calculate their sum, difference, product, quotient, and remainder using arithmetic operators
a = float(input("Enter the 1 number: "))
b = float(input("Enter the 2 number: "))

# Calculate and print the results
sum_result = a + b
difference_result = a - b
product_result = a * b
quotient_result = a / b
remainder_result = a % b

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Remainder:", remainder_result)


# In[3]:


# Exercise 2: Comparison Operators
#take 2 numbers and compare each other
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Compare and print the results
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)


# In[1]:


# Exercise 3: Logical Operators
a = bool(input("Enter the first boolean value (True or False): "))
b = bool(input("Enter the second boolean value (True or False): "))

# Perform logical operations and print the results
print("AND:", a and b)
print("OR:", a or b)
print("NOT (for the first value):", not a)
print("NOT (for the second value):", not b)


# In[2]:


# Exercise 4: Bitwise Operations
m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))

# Perform bitwise operations and print the results
print("Bitwise AND:", m & n)
print("Bitwise OR:", m | n)
print("Bitwise XOR:", m ^ n)
print("Bitwise NOT (for the first value):", ~m)
print("Bitwise NOT (for the second value):", ~n)


# In[3]:


# Exercise 5: Precedence of Operators
p = float(input("Enter the first number: "))
q = float(input("Enter the second number: "))
r = float(input("Enter the third number: "))

# Create and print the expression with operator precedence
result = p + q - r * p / q
print("Result:", result)


# In[ ]:





# In[ ]:




