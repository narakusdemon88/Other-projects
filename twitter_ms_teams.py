import tweepy
import time
import datetime
import pymsteams
import logging


logging.basicConfig(
	filename='output.log',
	level = logging.INFO,
	format='%(asctime)s:%(levelname)s:%(message)s')

logging.info('Code started')


# Twitter credentials
CONSUMER_KEY = '[CONSUMER KEY GOES HERE]'
CONSUMER_SECRET = '[CONSUMER SECRET GOES HERE]'
ACCESS_TOKEN = '[ACCESS TOKEN GOES HERE]'
ACCESS_TOKEN_SECRET = '[ACCESS TOKEN SECRET GOES HERE]'


# Production Webhook:
OUTLOOK_WEBHOOK = 'OUTLOOK_WEBHOOK_GOES_HERE'


def create_api():

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth , wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

	try:
		api.verify_credentials()
		logging.info('API credentials successfully verified')

	except:
		logging.warning('API credentials unsuccessfully verified')

	tweets = api.search(
		# Modify query results here
		q= 'this OR that -filter:retweets -bad_words',
		lang='ja',
		result_type='recent',
		count=40)

	myTeamsMessage = pymsteams.connectorcard(OUTLOOK_WEBHOOK)

	for tweet in tweets:

		try:
			# Create a URL for easy clicking within chat
			# Twitter URLs follow this format- https://twitter.com/[USERNAME]/status/[TWEET ID]
			url = str('https://twitter.com/' + tweet.user.screen_name + '/status/' + str(tweet.id))
			myTeamsMessage = pymsteams.connectorcard(OUTLOOK_WEBHOOK)
			myTeamsMessage.addLinkButton(url, url)
			myTeamsMessage.text(
				# Create format of text message
				'Username: ' + tweet.user.name + '\n' + '\n' +
				'Screen Name: ' + tweet.user.screen_name + '\n' + '\n' +
				'Sent time: ' + str(tweet.created_at + datetime.timedelta(hours=9)) + '\n' + '\n' +
				'URL: '+ url + '\n' + '\n' +
				'Body: ' + tweet.text + '\n' + '\n'

				)
			logging.info('Tweet # ' + str(tweet.id) + ' created')

			myTeamsMessage.send()
			logging.info('Tweet # '+ str(tweet.id) + ' sent')

			tweet_list = []

			for tweet.id:
				tweet_list.append(tweet.id)

			print(tweet_list)

			# Get only tweets within the last hour
			curr = datetime.datetime.now()

			tweet_time = tweet.created_at + datetime.timedelta(hours=9)

			hours = str(curr - tweet_time)[0]

			# if(hours == '0'):

				# myTeamsMessage.send()

		except:
			logging.warning('Failed to create tweets')

# Call the function here
if __name__ == '__main__':
	create_api()
	logging.info('Code finished')
