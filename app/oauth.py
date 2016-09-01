#Yelp API oauth
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import io

with io.open("config_secret.json", "r") as cred:
	creds = json.load(cred)
	auth = Oauth1Authenticator(**creds)
	client = Client(auth)
