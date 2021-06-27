from hedera import TopicCreateTransaction
from get_client import client

resp = (TopicCreateTransaction()
        .setTopicMemo("my topic memo")
        .execute(client))
topicId = resp.getReceipt(client).topicId
print("New TopicID: ",  topicId.toString())
