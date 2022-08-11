import mongoengine as mongo
from datetime import datetime
from pytz import timezone


ind_time = datetime.now(timezone("Asia/Kolkata")
                        ).strftime('%Y-%m-%d %H:%M:%S.%f')


class Config(mongo.Document):
    topic = mongo.StringField(required=True)
    context = mongo.StringField(required=True)
    domain_url = mongo.URLField(required=True)

    # def __init__(self, topic, context, domain_url):
    #     self.topic = topic
    #     self.context = context
    #     self.domain_url = domain_url


class Conversations(mongo.Document):
    config_id = mongo.ReferenceField(Config)
    user1 = mongo.EmailField()
    user2 = mongo.EmailField()

    # def __init__(self, config_id, user1, user2):
    #     self.config_id = config_id
    #     self.user1 = user1
    #     self.user2 = user2


class Messages(mongo.Document):
    conv_id = mongo.ReferenceField(Conversations)
    sender = mongo.EmailField()
    text = mongo.StringField(max_length=255)
    time = mongo.DateTimeField(auto_now_add=True, default=ind_time)

    # def __init__(self, conv_id, sender, text, time):
    #     self.conv_id = conv_id
    #     self.sender = sender
    #     self.text = text
    #     self.time = time
