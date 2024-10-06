import pandas as pd

my_data_set = {
  "cars" : ["BMW", "Volvo", "Ford"],
  "passings" : [3,7,2]
}

df = pd.DataFrame({
  "Bob" : ["I liked it." , "It was awful."],
  "sue" : ["Pretty good." , "Bland."]
},
index=["Product A", "Product B"]
)
print(df)


hj = pd.Series([30, 35, 40],
                index=["2015 Sales", "2016 Sales", "2017 Sales"],
                name="Product A"
)
print(hj)

wine_reviews = pd.read_csv("wine_reviews.csv")
print(wine_reviews.head())

print(wine_reviews.iloc[60:65], [1,5])
# this is selecting the data you want with slicing

print(wine_reviews["province"])
# this is printing a specific part. You can input whatever you needed in that string

print(wine_reviews["province"][0])
# this is the same thing as before but prints the first province.

print(wine_reviews.iloc[0])
# this selects the first row of data in the dataframe

print(wine_reviews.iloc[1:3,0])
# this is selecting the second and third entries

print(wine_reviews.iloc[[0,1,2], 0])
# it's also possible as a list

print(wine_reviews.iloc[-5:])
# you can also use negative numbers. This will start counting from the end of the list

print(wine_reviews.loc[wine_reviews["winery"] == "Ponzi"])
# here we are using .loc to find something specific. We wanted to find "Ponzi" in the "winery" column. If we wanted to find "California" in the "province" column we would replace the words in the string accordingly

tt = wine_reviews.loc[[0,1,10,100], wine_reviews.columns.isin (["country", "province", "region_1 ", "region_2"])]
print(tt)
# This line of code is saying that we DO want the items in the strings and prints only them and indexed numbers we wanted from the list. Additional note: putting the indexed numbers in the list allowed me to select which rows i wanted otherwise, .loc / .iloc would have taken only one argument.


tt = wine_reviews.loc[[0,1,10,100], ~wine_reviews.columns.isin (["country", "province", "region_1 ", "region_2"])]
print(tt)
#This line of code is saying that we DO NOT want the items in the strings and will print out everything but those things