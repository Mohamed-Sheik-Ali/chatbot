# FLASK CHAT BOT 

### A Pluggable chatbot application

# BUILD WITH FLASK==2.1.3 and MONGODB


## Authors

- [@anandrajB](https://github.com/anandrajB)
- [@Mohamed-Sheik-Ali](https://github.com/Mohamed-Sheik-Ali)



# DATABASE REQUIREMENTS

1. flask-mongoengine==1.0.0
2. mongoengine==0.24.2

## INSTALLATION AND RUNNING

1. pip install -r requirements.txt
2. flask run

## API Reference
#### Post a configuration and get a configuration

```http
  POST and GET /config
```

| Parameter | Type     | Description                |  Request          |
| :-------- | :------- | :------------------------- |:-----------------|
| `topic` | `string` | **Required**. topic obtained from Xpath |  body  |
| `context` | `string` | **Required**. context based on Xpath |  body  |
| `domain` | `URL field` | **Required**. URL of a page|  body  |


#### Post a conversation and get all conversations

```http
  POST and GET /conversation
```

| Parameter | Type     | Description                |  Request   |
| :-------- | :------- | :------------------------- |:------------|
| `config_id` | `string` | **Required**. Config reference |  body  |
| `user1` | `email` | **Required**. User |  body  |
| `user2` | `email` | **Required**. User|  body  |

#### Post a message

```http
  POST /messages
```

| Parameter | Type     | Description                |  Request   |
| :-------- | :------- | :------------------------- |:------------|
| `conv_id` | `string` | **Required**. Conversation reference |  body  |
| `sender` | `email` | **Required**. User |  body  |
| `text` | `email` | **Required**. Message to be sent|  body  |


#### Filter messages

```http
  POST /filter_conv
```

| Parameter | Type     | Description                |  Request   |
| :-------- | :------- | :------------------------- |:------------|
| `conv_id` | `string` | **Required**. Conversation reference |  body  |


## HEROKU URL

https://flask-chat-app-scf.herokuapp.com