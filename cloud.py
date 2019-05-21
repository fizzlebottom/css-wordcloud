from wordcloud import WordCloud, STOPWORDS
import matplotlib
import pandas as pd

import matplotlib.pyplot as plt
matplotlib.use("GTK3Agg")

# Read file
datafile = pd.read_csv(r"data/test.csv", encoding="utf-8")

comment_words = " "
stop_words = set(STOPWORDS)

# iterate through csv file
for val in datafile:
    # typecast each val to string
    val = str(val)

    #split the value
    tokens = val.split()

    #convert each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    for words in tokens:
        comment_words = comment_words + words + " "

wordcloud = WordCloud(width=800, height=800,
                    background_color="white", stopwords=stop_words,
                    min_font_size=10).generate(comment_words)

# plot the image
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
