


import matplotlib.pyplot as plt
import tweepy
from textblob import TextBlob



def percentange(partial, total):
    return 100 * float(partial) / float(total)


consumerKey = 'QpHy217uFPdn4trUuLeNI8nkJ'
consumerSecret = 'LU7G5lBegPKPbnoDtaX8A49osMCuLXC54Z19E1mx7IWXFOnUqG'
accessToken = '1405895032612159488-J2zvzmSZhqrauJppB95QxRu3fSJWJq'
accessTokenSecret = '3HKdBgpiraTK0TzZjAUxmWaf1dEoajMc9glIqrtOQG3aa'


authenticate = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
authenticate.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(authenticate)


searchTerm = input("Enter the term to be analysed:")
noOfSearchTerms = int(input("Enter the number of tweet to be analysed:"))


tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(noOfSearchTerms)

positive,negative,neutral,polarity,overall=0,0,0,0,0


for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    print(analysis.sentiment.polarity)
    overall += 1
    if (analysis.sentiment.polarity == 0):
        neutral += 1
        print("neutral increased " + str(neutral))

    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
        print("negative increased " + str(negative))

    elif (analysis.sentiment.polarity > 0.00):
        positive += 1
        print("positive increased " + str(positive))

print("positive " + str(positive))
print("negative " + str(negative))
print("neutral " + str(neutral))
positive = percentange(positive, overall)
negative = percentange(negative, overall)
neutral = percentange(neutral, overall)
positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')
print("positive %" + str(positive))
print("negative %" + str(negative))
print("neutral %" + str(neutral))
print("Reaction of people on #" + searchTerm + " by analyzing " + str(noOfSearchTerms) + ' Tweets:')
if (positive > neutral and positive > negative):
    print("positive")
elif (neutral > negative):
    print("neutral")
elif (negative > neutral):
    print("negative")


labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellow', 'green', 'blue']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('Reactions of people on #' + searchTerm + '  by analyzing ' + str(noOfSearchTerms) + ' Tweets:')
plt.axis('equal')
plt.tight_layout()
plt.show()