**Project Title**: Iowa Forfeiture Trends and Patterns

**Team**: The Forfeiture Force

**Group**: 26


**Names of the Contributors**: Kaitlyn Schwarz, Hayden Baseri, and Ethan Futral


**Objective and Motivation**: 

 Our data we will be using for this project was published by the Office of the Attorney General and collected from different law enforcement agencies and courts in Iowa. It contains 5,000 cases of forfeitures collected from Iowa, the data set includes the agency involved, county, case number, and forfeited assets and more. This data was collected to track asset forfeiture cases in Iowa, and for different counties to compare their cases amounts. It provides a record of money, vehicles, and real estate forfeited, along with their individual case details. Our motivation is to use this information to investigate how forfeiture amounts have changed over time, how they differ between counties, and more. The most useful data from this data set is the fiscal year opened/closed, county name, case ID, and total money forfeited.

**Specific Questions**:

**Question 1**. 

 How has the total amount of money forfeited changed over the years? We will create a line graph to identify trends and determine whether forfeiture amounts have changed over time. Some potential benefits of this analysis include identifying trends in forfeiture amounts over time and determining which years had higher/lower amounts of money forfeited. This can help understand how asset forfeiture activity has changed in Iowa over the years and help counties continue to have high total forfeited sums of money. We will complete this by using the data included in our dataset such as the fiscal year each case was closed and the total amount of money forfeited. We can group cases by their year and calculate the total money forfeited each year. We will then create a line graph to identify trends and determine whether forfeiture amounts have changed over time. We expect to see changes in the total amount of money forfeited each year, once the counties with the highest sums are found the lower counites can see what they did differently those years so they can improve there standings.


**Question 2**.

How do the average amounts of money forfeited differ between counties in Iowa? We will create a bar graph comparing these averages to see which counties have higher/lower average forfeiture amounts. This bar graph will help us determine which counties have higher/lower averages and better understand how forfeiture amounts vary across Iowa. We will use smoothing signal processing to reduce random fluctuations to reveal trends in our data which can help identify the trend of higher and lower overall cases in across the different counties. Some potential benefits of this analysis include identifying differences in average forfeiture amounts between counties; this is important as the counties with higher averages can train the counties with lower averages to improve the overall averages. We will use the data included in our dataset such as the county name and the amount of money forfeited for each case. We can group the cases by county and calculate the average amount of money forfeited per case. We expect to see differences in the average amounts of money forfeited between counties. 

**Question 3**.

What is the relationship between the number of forfeiture cases and the average amount of money forfeited per case in each county? We will create a scatter plot to determine if counties with more cases have higher or lower average forfeiture amounts. We will use data fitting to reduce noise in the data set and make our data cleaner to read and analyze as well as see if the high forfeiture amounts fall relatively within the same counties. Benefits of this analysis include determining whether counties with more forfeiture cases tend to have higher average forfeiture amounts. This could help us identify relationships between the number of cases and the amount of money forfeited across counties. We will use the data provided in our dataset such as the case ID, county name, and total money forfeited. We can count the number of cases in each county and calculate the average money forfeited per case. We expect to see whether counties with more forfeiture cases tend to have higher or lower average amounts of money forfeited, as well as allow us to see if the high forfeiture amounts fall relatively within the same counties.



**Implementation Details**: 

**Question 1**: 

We will group the data by year and calculate the total amount of money forfeited during each year. The main metric of measurement will be the annual total forfeiture amount in dollars. Then we will use Pandas to group the records by year and total amount of forfeiture. We will then use Matplotlib to make a line graph with the years on the x-axis and forfeiture amounts on the y-axis. This will show how the amount in forfeitures changes over the years.

# Preliminary Question One Graph:

 <img width="467" height="281" alt="image" src="https://github.com/user-attachments/assets/5d335afe-f2ea-4250-bef1-825d990f9557" />

**Question 2**: 

We will use Pandas to group the data by county and calculate the average amount of money forfeited per case. Then we use Matplotlib to make a bar graph comparing the average amounts across counties. This will show the difference in forfeiture amounts in each county and show which areas have either a higher or lower.

 # Preliminary Question Two Graph:
 
<img width="468" height="203" alt="image" src="https://github.com/user-attachments/assets/d27c8c48-942f-477c-bd20-3493ecd74b5c" />

**Question 3**: 

We use Pandas to get the number of forfeiture cases and the average forfeiture amount for each county. Then we use Matplotlib to make a scatter plot with the number of cases on the x-axis and the average amount forfeited on the y-axis. We would then make a trendline using NumPy to see if counties with more cases tend to have higher or lower average forfeiture amounts.

#  Preliminary Question Three Graph:

<img width="466" height="278" alt="image" src="https://github.com/user-attachments/assets/602d1191-58ed-4357-aa1d-88d6642a13e3" />

**Results for Three Questions**:

**Question 1**:

Total Money Forfeited by Year:

2017: $1,681,501

2018: $1,798,930

2019: $1,938,900

2020: $1,377,436

2021: $1,519,558

2022: $2,455,855

2023: $1,714,183

2024: $1,626,563

2025: $1,325,289

2026: $1,437,166


 <img width="479" height="407" alt="image" src="https://github.com/user-attachments/assets/9a16ce5d-3bac-4dda-b508-a25d76717615" />

 
**Answering Our Questions**:

**Question 1**: 

Our results show that the total amount of money forfeited in Iowa changed significantly between 2017 and 2026. The highest amount was recorded in 2022, with $2.46 million forfeited, while the lowest amount was recorded in 2025, with $1.33 million. Forfeiture totals increased overall from 2017 to 2019, decreased in 2020, and reached their highest point in 2022. After 2022, the total amount decreased, with a small increase in 2026. Overall, the results show that forfeiture amounts fluctuate from year to year and don't follow distinct trends. From our results, we can conclude that the total amount of money forfeited in Iowa varies between the years. This information will help counties understand state wide forfeiture trends and compare them with their own forfeiture amounts. Counties should investigate why 2022 had the highest total and determine what to changes in their own counties. These changes may involve changes in enforcement activity, total case number amounts, or other factors. Counties can also use these results to better understand trend in forfeiture amounts and improve county planning. 
**Conclusions**:


**References/Source files**:
State of Iowa - State of Iowa Forfeiture Cases 

