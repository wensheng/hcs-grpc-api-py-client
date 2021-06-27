import sys
import logging
import grpc
from hcs_grpc_client import ConsensusTopicQuery, TopicID, ConsensusServiceStub


def run(tid: TopicID):
    request = ConsensusTopicQuery(topicID=tid)
    channel = grpc.insecure_channel("hcs.testnet.mirrornode.hedera.com:5600")
    stub = ConsensusServiceStub(channel)
    stream = stub.subscribeTopic(request)
    try:
        for resp in stream:
            # print(resp)
            timestamp = "{}@{}".format(resp.consensusTimestamp.seconds,
                                       resp.consensusTimestamp.nanos)
            print("timestamp", timestamp)
            print("message:", resp.message.decode())
            print("sequence#:", resp.sequenceNumber)
    except grpc.RpcError as e:
        print(e)


if __name__ == '__main__':
    tid = TopicID(topicNum=int(sys.argv[1]))
    logging.basicConfig()
    run(tid)
