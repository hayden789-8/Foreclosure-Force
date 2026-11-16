
############### 1 ############################
#potential 1st question code
#pandas to read the CSV file and calculate yearly forfeiture totals
import pandas as pd 

#matplotlib to create a line graph
import matplotlib.pyplot as plt 

#read CSV file
#data=pd.read_csv("Data/state_of_iowa_forfeiture_cases_957_rows.csv")
from pathlib import Path
file_path=Path(__file__).resolve().parent/"Data"/"state_of_iowa_forfeiture_cases_957_rows.csv"
data=pd.read_csv(file_path)

#keep cases closed from 2017-2025 to compare,removes 2003/2027 from the graph
data=data[(data["fiscal_year_closed"]>=2017)&(data["fiscal_year_closed"]<=2026)]

#group cases by their closing year and add the money forfeited 
yearly_totals=data.groupby("fiscal_year_closed")["total_money_forfeited"].sum()

#print yearly totals with commas, :.0f removes decimal places
print("Total Money Forfeited by Year:")
for year,money in yearly_totals.items():
    print(f"{year:.0f}: ${money:,.0f}")

#line graph fiscal years and their total forfeiture amounts, marker adds a dot at each year
plt.plot(yearly_totals.index,yearly_totals.values,marker="o")

#graph title and label both axes 
plt.title("Total Money Forfeited in Iowa (2017-2026)")
plt.xlabel("Fiscal Year Closed")
plt.ylabel("Total Money Forfeited ($)")

#y-axis to display dollar signs and commas
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x,pos:f"${x:,.0f}"))

#display 2017-2026 x-axis
plt.xticks(range(2017,2027))

#gridlines to make it easier to compare 
plt.grid(True)

#spacing for title and labels 
plt.tight_layout()

#completed line graph



################# 2 #########################

#compare the forfeitere amounts between different counties in Iowa
import matplotlib.pyplot as plt
import pandas as pd

# 1.get data set from file
df = pd.read_csv("Data/state_of_Iowa_forfeiture_cases_957_rows.csv")

# 2. make sure columns names are correct for forfeiture amounts
print(df.columns)

# 3. group by county and sum the forfeiture amounts
county_forfeitures = (
    df.groupby("county_name")["total_money_forfeited"].sum().reset_index()
)

#4.make bar graph to compare forfeiture amounts by county
county_forfeitures = county_forfeitures.sort_values(
    by="total_money_forfeited", ascending=False
).head(10)

plt.figure(figsize=(12, 6))
plt.bar(
    county_forfeitures["county_name"],
    county_forfeitures["total_money_forfeited"],
    color="steelblue",
    edgecolor="black",
)

#5.edit graph title and labels
plt.title("Top 10 Counties by Total Money Forfeited in Iowa")
plt.xlabel("County")
plt.ylabel("Total Money Forfeited ($ in Millions)")
plt.xticks(rotation=45, ha="right") # rotate for readability
plt.tight_layout()

# 6. Save and display the plot
plt.savefig("county_forfeitures_bar_graph.png", dpi=300)





#################Task 3#########################
plt.show()
