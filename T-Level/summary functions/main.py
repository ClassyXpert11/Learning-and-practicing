import pandas as pd

wr = pd.read_csv("wine_reviews.csv")

print(wr.points.mean())
# this is giving me the mean for all of the points in the csv file

print(wr["country"].unique())
# this is telling all the countries that are in the csv file, it is only telling me each one once. no duplicates.

print(wr["country"].value_counts())
# this is telling me how many times a country shows up

reviews_per_country = wr[["country","title"]].value_counts()
print(reviews_per_country)
# this is like the previous one but is being more specific about what it wants
