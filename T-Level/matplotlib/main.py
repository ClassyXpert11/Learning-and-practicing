import matplotlib.pyplot as plt
import pandas as pd

pkm_dta = pd.read_csv("pokemon.csv")
pkm_nms = pkm_dta["Name"].loc[16:21]
pkm_ttl = pkm_dta["Total"].loc[16:21]

#d = {
  #"name": ["Abdullah", "Tim", "Anzar", "Carl", "Jai","Ashley"],
  #"point": [1, 2, 2, 3, 6, 6]
#}

#fields = d["name"]
#ypoints = d["point"]

plt.bar(pkm_nms, pkm_ttl)
# marker is the thing that shows up on the exact points, you can change it to "o" or "x".
# linestyle (ls is the shorter version) is the line that runs through the points, it can be changed to dotted or dashed or solid.
# linewidth (lw is the shorter version) is the actual width of the line and can be changed to be either thick on thin depending on the number
# color is simply the colour you want the line and points to be
plt.xlabel("Names")
# naming the x axis
plt.ylabel("Total")
# naming the y axis
plt.title("This is a graph")
# giving it a title
plt.show()
# printing it out