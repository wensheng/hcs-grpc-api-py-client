import sys
import logging
import grpc
from hcs_grpc_client import ConsensusTopicQuery, TopicID, ConsensusServiceStub


def run(tid: TopicID):
    request = ConsensusTopicQuery(topicID=tid)
    # to use a different mirror node, such as a locally deployed:
    # channel = grpc.insecure_channel("127.0.0.1:5600")
    channel = grpc.secure_channel("mainnet-public.mirrornode.hedera.com:443",
                                  grpc.ssl_channel_credentials())
    stub = ConsensusServiceStub(channel)
    stream = stub.subscribeTopic(request)
    try:
        for resp in stream:
            print(resp)
    except grpc.RpcError as e:
        print(e)


if __name__ == '__main__':
    tid = TopicID(topicNum=int(sys.argv[1]))
    logging.basicConfig()
    run(tid)
