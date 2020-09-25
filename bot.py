import tweepy
import json
import pprint
from colorama import Fore, Style
from tweepy import OAuthHandler

def get_permissions():
    text = open('permission.json').read()
    permissions = json.loads(text)
    return permissions

def setup_api():
    permissions = get_permissions()
    auth = OAuthHandler(permissions['consumer_key'],
                        permissions['consumer_secret'])
    auth.set_access_token(permissions['access_token'],
                          permissions['access_secret'])

    return tweepy.API(auth)

def print_timeline(api):
    pp = pprint.PrettyPrinter(indent=4)
    for status in tweepy.Cursor(api.home_timeline).items(10):
        # If you want the whole thing.
        # pp.pprint(status._json)
        print(f'{Fore.GREEN}@{status.user.name}{Style.RESET_ALL}: '
              f'{Fore.BLUE}{status.text}{Style.RESET_ALL}')
        print('-'*45)

api = setup_api()
print_timeline(api)
