# put the filenames from deps.txt here
./venv/bin/python -m grpc_tools.protoc \
    --proto_path=hedera-protobufs/services \
    --python_out=src/hcs_grpc_client \
    hedera-protobufs/services/Timestamp.proto \
    hedera-protobufs/services/BasicTypes.proto \
    hedera-protobufs/services/ConsensusSubmitMessage.proto
