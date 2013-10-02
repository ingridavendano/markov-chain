import twitter


def make_status(random_text):
    api = twitter.Api(consumer_key='consumer_key',
consumer_secret='consumer_secret', access_token_key='access_token', access_token_secret='access_token_secret')

    status = api.PostUpdate(random_text)
    print "TWEETED! ", status.text