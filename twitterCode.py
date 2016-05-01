import twitter
import twitterSecrets

api = twitter.Api(consumer_key=twitterSecrets.consumer_key,
                  consumer_secret=twitterSecrets.consumer_secret,
                  access_token_key=twitterSecrets.access_token,
                  access_token_secret=twitterSecrets.access_token_secret)

print(api.VerifyCredentials())
