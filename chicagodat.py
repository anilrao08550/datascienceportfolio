#this project is about visualizing and understanding information of 30000+ Chicago public employees, department and their salaries
#import databases for data analysis and viz. This project was completed in IPython Notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
%pylab inline
#The first thing we are going to do is read in the data using Pandas. Then in the first part we will understand the data
#In the 2nd step we will delve deeper into the data to help us answer fundamental questions
chicago = pd.read_csv('chicagosalaries.csv')

# grouping your results by department
chicagodat = chicago.groupby('Department')

#highest average salary graph

x = chicagodat.Salary.mean().order(ascending=True)
print x
figure(figsize=(12, 9))
x.plot(kind='barh')
plt.xlabel('Average Salary')
plt.title('Average Salary based on industry', fontsize=16)

#ordering departments by who has the most people
#graphing it into a histogram

mostnumber = chicago.groupby('Department').size().order(ascending=False)[:40]
print mostnumber
figure(figsize=(12, 9)) 
mostnumber.hist(bins = 15)
plt.title("How many people per department in Chicago?", fontsize = 16)
plt.ylabel('Number of departments')
plt.xlabel('Number of People')


# Plotting the distribution of salaries, it looks normally distributed
figure(figsize=(10.0, 7.5)) 
plt.hist(chicago.Salary.dropna(), bins = 7)
plt.title("Chicago Employee Salary Distribution", fontsize=16)
plt.ylabel('Number of people')
plt.xlabel('Employee Salary')

# Future look at the data via boxplot, again looks like a normal distribution, not too many outliers
sns.boxplot(chicago.Salary, vert = False)
plt.title('Boxplot of Chicago employee salaries', fontsize=16)

#Another look at the Data via Kernel Density Estimate Plot
#Again another indicator that salaries are normally distributed. 
figure(figsize=(12, 9)) 
sns.kdeplot(chicago.Salary.dropna(), shade = True )

#We have got 32160 public employees in Chicago, with a mean salary of $75559.11
#Max salary is $260,000
print chicago.describe()
print "The median is %d" % chicago.Salary.median()

#Violin Plot for overall salaries
figure(figsize=(12, 9))  
plt.title('Violin plot of Salary Distribution', fontsize=16)
sns.violinplot(chicago.Salary.dropna(), color='green')

#Violin Plot below allows us to look at Salary skews by Department
figure(figsize=(12, 9))  
plt.title('Salary by Department', fontsize=16)
sns.violinplot(chicago.Salary.dropna(), chicago.Department, vert =False)

#Make a Culmative Distrubutive Function
#Virtually no employee in the State of Chicago makes more than $175,000 
figure(figsize=(10, 7.5))  
sns.kdeplot(chicago.Salary.dropna(), cumulative=True)
plt.title('Culmative Distrbutive Function of Salaries', fontsize=16)
plt.xlabel('Salary')

#bar graph plot of employees per department

figure(figsize=(10, 7.5))
ax = subplot(111)  
ax.spines["top"].set_visible(False)  
ax.spines["right"].set_visible(False) 
ax.get_xaxis().tick_bottom()  
ax.get_yaxis().tick_left()  
xticks(fontsize=14)  
mostnumber.plot(kind='bar')
plt.title('Number of Employees by Department', fontsize=16)
plt.ylabel('Number of Employees')
plt.xlabel('Department')

#Who makes more than $175,000?

mask = chicago.Salary > 175000
f = chicago[mask].groupby('Name')
f.Salary.mean().order(ascending=False)

#$2.42 Billion dollars is spent on the salaries of Chicago Public Employees + Benefits and Pensions. 
print Chicago.salary.sum()
