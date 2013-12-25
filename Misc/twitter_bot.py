from twitter import Twitter, OAuth, TwitterHTTPError

OAUTH_TOKEN = "218804182-mgRGE5K7JU8CgOhcC3BvICoahvPGIyJmvQDTrG6Q"
OAUTH_SECRET = "e1KU101dJLRa5VBLEyaUhQpyyh5g5TC975YSjQIeg"
CONSUMER_KEY = "jyigk3zwe3BHqNYx9QtbCg"
CONSUMER_SECRET = "yHh8V3DARbCXvQMeTAY8yzoRa0mksBXlo6zF9i0"

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
    CONSUMER_KEY, CONSUMER_SECRET))

def search_tweets(q, count=100):
    return t.search.tweets(q=q, result_type='recent', count=count)

def fav_tweet(tweet):
    try:
        result = t.favorites.create(_id=tweet['id'])
        print "Favorited: {0}".format(result['text'])
        return result
    # when you have already favourited a tweet
    # this error is thrown
    except TwitterHTTPError as e:
        print "Error: ", e
        return None

def auto_fav(q, count=100):
    result = search_tweets(q, count)
    a = result['statuses'][0]['user']['screen_name']
    print a
    success = 0

    for tweet in result['statuses']:
        if fav_tweet(tweet) is not None:
            success += 1

    print "We favorited a total of {0} out of {1} tweets".format(success,
        len(result['statuses']))