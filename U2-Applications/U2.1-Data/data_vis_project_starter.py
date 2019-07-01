'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

# #Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# # Continue your program below! 
# polaritylist = []
# for tweet in tweetData:
#     tweetblob = TextBlob(tweet["text"])
#     polaritylist.append(tweetblob.polarity)
# # Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.sentiment)
polarityList = []
subjectivityList = []

tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet['text']
    tweetblob = TextBlob(tweet['text'])
    polarityList.append(tweetblob.polarity)
    subjectivityList.append(tweetblob.subjectivity)
print(tweetstring)

tweetBlob = TextBlob(tweetstring)

# print(tweetBlob.translate(to = 'ko'))
# print(polarityList)
# print(subjectivityList)

my_list = polarityList
print(sum(my_list)/len(my_list))

my_list2 = subjectivityList
print(sum(my_list2)/len(my_list2))


word_dict = {}

for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]

print(word_dict)

import matplotlib.pyplot as plt


plt.hist(my_list, bins=[-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1, 1.1, 0, 60])
plt.grid(True)
plt.show()