import pandas as pd

wr = pd.read_csv("wine_reviews.csv", index_col=0)

# Exercise 1
print(wr.groupby("taster_twitter_handle")["taster_twitter_handle"].count())
# this is using the .groupby() function to not only give us the people who left the most reviews but has also put them in a series. value_counts() is just a shortcut of this.

# Exercise 2
print(wr.groupby("price").points.max())
# this is getting the maximum number of points for each price. it has also put them in acending order

# Exercise 3
print(wr.groupby(["variety"]).price.agg([min, max]))
# using .agg here to run a couple of functions at the same time. whatever has been put in the square brackets [] will need to be defined at the end there with agg (when using it).

# Exercise 4
sorted_values = wr.groupby(["variety"]).price.agg([min, max])
print(sorted_values.sort_values(by = ["min", "max"], ascending = False))
# ask for help


# Exercise 5
print(wr["taster_name"].value_counts().points.mean())


# Exercise 6

