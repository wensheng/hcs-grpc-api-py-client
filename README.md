# pip install hcs-grpc-client

This is a [Hedera](https://hedera.com/) Consensus Service (HCS) gRPC mirror node API Python client.

It only has functionality to subscribe to a HCS topic on mirror node.

For mirror node REST API, use curl or something like Python [`requests`](https://pypi.org/project/requests/).

For all other interactions with Hedera, use an SDK:
[Python](https://github.com/wensheng/hedera-sdk-py),
[Java](https://github.com/hashgraph/hedera-sdk-java),
[Javascript](https://github.com/hashgraph/hedera-sdk-js), or
[Go](https://github.com/hashgraph/hedera-sdk-go).

## How to Use
```python
import grpc
from hcs_grpc_client import TopicID, ConsensusTopic, ConsensusServiceStub
request = ConsensusTopicQuery(topicID=TopicID(2010293))
channel = grpc.insecure_channel("hcs.testnet.mirrornode.hedera.com:5600")
stub = ConsensusServiceStub(channel)
stream = stub.subscribeTopic(request)
for resp in stream:
    # do whatever you need
    print(resp)
```

Make sure the topic exists or create your own topic with an SDK.  An example is given in `examples/`.

See [examples](https://github.com/wensheng/hcs-grpc-api-py-client/tree/main/examples) for mainnet example and other usages.


## How to Build
(**Ignore this section unless you want to customized the client and/or want to contribute to this project**)

Clone this repo:

    git clone --recurse-submodules https://github.com/wensheng/hcs-grpc-api-py-client.git

Setup virtual env for python then install dependencies:

    cd hcs-grpc-api-py-client
    python3 -m venv venv
    ./venv/bin/python install -r requirements.txt

Generate code (compile .proto to .py):

    ./compile.sh  # make sure deps.txt match compile_deps.sh
    ./compile_deps.sh

Build package:

    rm -fr build dist
    ./venv/bin/python -m build

Test package:

    ./venv/bin/pip uninstall hcs-grpc-client
    ./venv/bin/pip install dist/hcs-grpc-client-(current_version)-py3-none-any.whl

Upload to Pypi (**don't do this unless you're me**):

    python -m twine upload dist/*
