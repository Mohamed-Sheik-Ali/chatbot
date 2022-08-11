from flask import Blueprint, jsonify, request, render_template
from .models import Config, Messages, Conversations
from flask_cors import cross_origin

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template('index.html')


@core.route('/config', methods=['GET', 'POST'])
@cross_origin('*')
def config():

    if request.method == 'POST':

        topic = request.form.get('topic')
        context = request.form.get('context')
        domain_url = request.form.get('domain')

        config = Config(topic=topic, context=context, domain_url=domain_url)
        config.save()

    config = Config.objects.all()
    return jsonify(config), 200


@core.route('/conversation', methods=['GET', 'POST'])
@cross_origin('*')
def conversation():

    if request.method == 'POST':

        config_id = request.form.get('config_id')
        user1 = request.form.get('user1')
        user2 = request.form.get('user2')

        conversation = Conversations(
            config_id=config_id, user1=user1, user2=user2)
        conversation.save()

    conversations = Conversations.objects.all()
    return jsonify(conversations), 200


@core.route('/messages', methods=['GET', 'POST'])
@cross_origin('*')
def messages():

    if request.method == 'POST':

        conv_id = request.form.get('conv_id')
        sender = request.form.get('sender')
        text = request.form.get('text')

        msg = Messages(conv_id=conv_id, sender=sender, text=text)
        msg.save()

    msgs = Messages.objects.all()
    return jsonify(msgs), 200


@core.route('/filter_conv', methods=['GET', 'POST'])
@cross_origin('*')
def filter_conv():

    if request.method == 'POST':

        # config_id = request.form.get('config_id')
        conv_id = request.form.get('conv_id')

    # conversations = Conversations.objects.get(config_id=config_id)

    msgs = Messages.objects.get(conv_id=conv_id)

    if msgs is not None:

        msg = {
            'config': msgs.conv_id.config_id,
            'conversation': msgs.conv_id,
            'text': msgs.text,
            'time': msgs.time,
            'sender': msgs.sender
        }

        return jsonify(msg), 200

    # return jsonify(conversations), 200


@core.route('/conv', methods=['GET', 'POST'])
@cross_origin('*')
def conv():

    if request.method == 'POST':

        user1 = request.form.get('user1')
        user2 = request.form.get('user2')
        config_id = request.form.get('config_id')
        conv_id = request.form.get('conv_id')

        conv = Conversations.objects.get(
            config_id=config_id, user1=user1, user2=user2)

        msgs = Messages.objects.get(conv_id=conv)

    return jsonify(conv)

    # except:
    #     conv = Conversations(config_id=config_id, user1=user1, user2=user2)

    #     conv.save()

    #     print(conv.pk)

    # return 'Success'
