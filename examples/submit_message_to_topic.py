import sys
from hedera import TopicId, TopicMessageSubmitTransaction
from get_client import client

if len(sys.argv) < 3:
    exit("Need a topicId and message")

topicId = TopicId.fromString(sys.argv[1])
message = " ".join(sys.argv[2:])

txn = (TopicMessageSubmitTransaction()
       .setTopicId(topicId)
       .setMessage(message)
       .execute(client))
receipt = txn.getReceipt(client)
print("seq #:", receipt.topicSequenceNumber)
