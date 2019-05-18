import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib

# Choose backend for live graph display
# https://matplotlib.org/faq/usage_faq.html#what-is-a-backend
matplotlib.use("GTK3Agg")

import matplotlib.pyplot as plt
#%matplotlib inline

# Load the dataframe
dataframe = pd.read_csv("data/winemag-data-130k-v2.csv", index_col=0)

# Looking at first 5 rows of datasheet
dataframe.head()

'''print("\nThere are {} observations and {} freatures in this dataset. \n" .format(dataframe.shape[0], dataframe.shape[1]))

print("There are {} types of of wine in this dataset such as {}... \n" .format(len(dataframe.variety.unique()),
                                                                                ", ".join(dataframe.variety.unique()[0:5])))

print("There are {} countries producing wine in this dataset such as {}... \n".format(len(dataframe.country.unique()),
                                                                                        ", ".join(dataframe.country.unique()[0:5])))
'''

# First three columns
dataframe[["country", "description", "points"]].head()

# Make comparisons between groups of a feature by using groupby(), then compute summary stats
# Group by country
country = dataframe.groupby("country")

# Summary stat of all countries
country.describe().head()

# Select top 5 highest avg points among 44 countries
country.mean().sort_values(by="points", ascending=False).head()

# Plot number of wines by country
plt.figure(figsize=(15,10))
country.size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Country of Origin")
plt.ylabel("Number of Wines")

# Save graph to image file
plt.savefig("test.png", bbox_inches="tight")

plt.show()
