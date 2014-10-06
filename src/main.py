import slackapi as api
from models import Channel
import pickle as p
import os


def load_channels():
    """
    TO-DO: don't filter messages we've already filtered before
    """
    with open(os.path.join("saved", "saved.p")) as f:
        f.write()
    return

if __name__ == "__main__":
    for channel in api.get_channels():
        Channel(channel).get_messages().filter()



