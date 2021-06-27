# hcs-grpc-client examples

Frist you need a topic to subscribe to.  You can pick an existing one such as testnet: [0.0.2010293](https://testnet.dragonglass.me/hedera/topics/0.0.2010293), or create a new one:

    python create_new_topic.py

You need [Python SDK](https://github.com/wensheng/hedera-sdk-py) for this. You can also use other SDK's.

To use an SDK, you need to set OPERATOR_ID/OPERATOR_KEY or HEDERA_CONFIG_FILE environment variables to set up a valid SDK client.  Refer to the SDK for more details.

Please note the TopicID you get back, for example: 0.0.1234567.  

You can then subscribe to this topic.  Open another terminal and in this 2nd terminal:

    python subscribe_topic_testnet.py 1234567

You are now subscribed to the topic and are listening to any messages that'are send to the topic.

Now you (or someone else) need to submit message to the topic.  From the first terminal:

    python submit_message_to_topic.py 0.0.1234567 hello world

You should receive in the 2nd terminal the message that was sent from the first or anywhere else.

## TopicID

Right now you can specify a TopicID by:
```python
topicId = TopicID(123456)
topicId = TopicID(topicNum=123456)
```

In the future, when hashgraph is sharded, you may have to provide all required fields:

    topidId = TopicID(realmNum=0, shardNum=123, topicNum=123456)

