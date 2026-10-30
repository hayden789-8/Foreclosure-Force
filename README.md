Project Title : Iowa Forfeiture Trends and Patterns 


Team Name and Names of the Contributors: The Forfeiture Force
Kaitlyn Schwarz, Hayden Baseri, and Ethan Futral


Objective and Motivation: 
Our data which was published by the Office of the Attorney General and collected from different law enforcement agencies and courts in Iowa. Each of the 5,000 cases includes the agency involved, county, case number, and forfeited assets and more. This data was most likely collected to track asset forfeiture cases in Iowa. It provides a record of money, vehicles, and real estate forfeited, along with their individual case details. Our motivation is to use this information to investigate how forfeiture amounts have changed over time, how they differ between counties, and more. The most useful data is the fiscal year opened/closed, county name, case ID, and total money forfeited.

Specific Questions:
1. How has the total amount of money forfeited changed over the years? We expect to see changes in the total amount of money forfeited each year. We will create a line graph to identify trends and determine whether forfeiture amounts have changed over time. Some potential benefits of this analysis include identifying trends in forfeiture amounts over time and determining which years had higher/lower amounts of money forfeited. This could help understand how asset forfeiture activity has changed in Iowa over the years.

2. How do the average amounts of money forfeited differ between counties in Iowa? We will create a bar graph comparing these averages to see which counties have higher/lower average forfeiture amounts. We expect to see differences in the average amounts of money forfeited between counties. We will use signal processing called smoothing to reduce random fluctuations to reveal trends which could help us be able to see the trend of higher to lower cases in different counties. Some potential benefits of this analysis include identifying differences in average forfeiture amounts between counties. This helps us determine which counties have higher/lower averages and better understand how forfeiture amounts vary across Iowa.

3. What is the relationship between the number of forfeiture cases and the average amount of money forfeited per case in each county? We will create a scatter plot to determine if counties with more cases have higher average forfeiture amounts. We expect to see whether counties with more forfeiture cases tend to have higher or lower average amounts of money forfeited. We will use data fitting to reduce noise in the data set to be cleaner to read and analyze as well as see if the high forfeiture amounts fall relatively within the same counties. Some potential benefits of this analysis include determining whether counties with more forfeiture cases also tend to have higher average forfeiture amounts. This could help us identify relationships between the number of cases and the amount of money forfeited.

Implementation Details: 
In this section, you will go over the methods (with metrics, tools, and plots) to be used to answer the questions. This is the main body of the repo.

 Question 1: We will group the data by year and calculate the total amount of money forfeited during each year. The main metric of measurement will be the annual total forfeiture amount in dollars. Then we will use Pandas to group the records by year and total amount of forfeiture. We will then use Matplotlib to make a line graph with the years on the x-axis and forfeiture amounts on the y-axis. This will show how the amount in forfeitures changes over the years.
# first graph:
 <img width="467" height="281" alt="image" src="https://github.com/user-attachments/assets/5d335afe-f2ea-4250-bef1-825d990f9557" />

 Question 2: We will use Pandas to group the data by county and calculate the average amount of money forfeited per case. Then we use Matplotlib to make a bar graph comparing the average amounts across counties. This will show the difference in forfeiture amounts in each county and show which areas have either a higher or lower
 # second graph:
<img width="468" height="203" alt="image" src="https://github.com/user-attachments/assets/d27c8c48-942f-477c-bd20-3493ecd74b5c" />

 Question 3: We use Pandas to get the number of forfeiture cases and the average forfeiture amount for each county. Then we use Matplotlib to make a scatter plot with the number of cases on the x-axis and the average amount forfeited on the y-axis. We would then make a trendline using NumPy to see if counties with more cases tend to have higher or lower average forfeiture amounts.
# third graph:
<img width="466" height="278" alt="image" src="https://github.com/user-attachments/assets/602d1191-58ed-4357-aa1d-88d6642a13e3" />

Results (Answers to the Questions):

Conclusions:

Actions that need to be completed:
 List all the actions that need to be completed (a checklist). Think about this as a guide to who wants to duplicate the project. Mention the issues that the group is facing for each action, if any.

References/Source files:

State of Iowa - State of Iowa Forfeiture Cases 

