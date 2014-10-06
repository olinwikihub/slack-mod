import slackapi as api

class Channel:
    def __init__(self, values):
        self.id = values["id"]
        self.messages = []
        self.name = values["name"]
        self.latest = 0
        self.oldest = 0

    def get_messages(self):
        self.messages = [Message(json, self.id) for json in api.get_messages(self) if "subtype" in json]

    def filter(self):
        for message in self.messages:
            if message.subtype in ["channel_join", "channel_leave"] and message.subtype != "message_deleted":
                message.delete()



class Message:
    def __init__(self, values, channel):
        self.id = values["ts"]
        self.subtype = values["subtype"]
        self.channel = channel
        self.text = "message deleted"
        if "text" in self.text:
            self.text = values["text"]


    def delete(self):
        api.delete_message(self)