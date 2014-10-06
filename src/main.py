import slackapi as api
from models import Channel
import pickle as p
import os


def load_channels():
    with open(os.path.join("settings", "saved.p")) as f:
        f.write()
    return

if __name__ == "__main__":
    channels = [Channel(chan) for chan in  api.get_channels()]
    for channel in channels:
        print "Filtering channel: ", channel.name, "id", channel.id
        channel.get_messages()
        channel.filter()        
