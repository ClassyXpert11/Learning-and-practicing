import pandas as pd

wr = pd.read_csv("wine_reviews.csv")

# Exercise 1 - Select the description column from the reviews and assign the result the variable desc
desc = wr["description"]
print(desc)

#Exercise 2 - Select the first value from the description column of reviews, assigning it to variable first_description
first_description = wr["description"][0]
print(first_description)

#Exercise 3 - Select the first row of data (the first record) from reviews, assigning it to the variable first_row
first_row = wr.iloc[0]
print(first_row)

#Exercise 4 - Select the first 10 values from the description column in reviews, assigning the result to variable first_description. --I changed the variable name to first_ten_description because it would have replaced the previous variable if i called it that.
first_ten_description = wr["description"][0:11:1]
print(first_ten_description)

#Exercise 5 - Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to variable sample_reviews
sample_reviews = wr.iloc[[1, 2, 3, 5, 8]]
print(sample_reviews)

#Exercise 6 - Create a variable df containing the country, province, region_1 and region_2 columns of the records with the index labels 0, 1, 10, 100
df = wr.loc[[0, 1, 10, 100], wr.columns.isin(["country", "province", "region_1 ", "region_2"])]
print(df)

#Exercise 7 - Create a variable df containing the country and variety columns of the first 100 records.
dff = wr.loc[1:101, wr.columns.isin(["country", "variety"])]
print(dff)

#Exercise 8 - Create a DataFrame italian_wines containing reviews of wines made in Italy
italian_wines = wr.loc[wr["country"] == "Italy"]
print(italian_wines)

#Exercise 9 - Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand
top_oceania_wines = wr.loc[(wr["country"].isin(["Australia", "New Zealand"])) & (wr["points"] >= 95)]
print(top_oceania_wines)
