import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

reddit = praw.Reddit(client_id='f8W3xbrawZEKHeL96XalrQ',
                     client_secret='bePFLSyIMZqgjsxxgTt3Qr6f0NNIfA',
                     user_agent='MyRedditApp/1.0 by Robin')


def analyze_sentiment(comment):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(comment)

    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'


def reddit_post_analyzer():
    post_url = input("Enter the URL of the Reddit post: ")
    submission = reddit.submission(url=post_url)
    submission.comments.replace_more(limit=None)
    positive_comments = []
    negative_comments = []
    neutral_comments = []

    for comment in submission.comments.list():
        sentiment = analyze_sentiment(comment.body)
        if sentiment == 'Positive':
            positive_comments.append(comment.body)
        elif sentiment == 'Negative':
            negative_comments.append(comment.body)
        else:
            neutral_comments.append(comment.body)

    print("Positive Comments:")
    print('\n'.join(positive_comments))
    print("\nNegative Comments:")
    print('\n'.join(negative_comments))
    print("\nNeutral Comments:")
    print('\n'.join(neutral_comments))


if __name__ == "__main__":
    reddit_post_analyzer()