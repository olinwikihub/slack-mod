import requests as req
from settings import config

API_WEB = "https://slack.com/api/%s"

def get_messages(channel):
    result = req.get(args(API_WEB % "channels.history", {"channel": channel.id, "count":"1000"}))
    return result.json()["messages"]



def get_channels():
    result = req.get(args(API_WEB % "channels.list", {"exclude_archived": "1"}))
    return result.json()["channels"]


def delete_message(message):
    print "Deleting ", message.text
    post = req.post(args(API_WEB % "chat.delete", {"channel": message.channel, "ts": message.id}))
    return post


def args(orig, tups = dict()):
    orig += "?token=" + config.token + "&"
    for key,entry in tups.items():
        orig += key + "=" + entry + "&"
    print orig[:-1]
    return orig[:-1]