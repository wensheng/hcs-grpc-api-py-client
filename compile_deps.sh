# put the filenames from deps.txt here
./venv/bin/python -m grpc_tools.protoc \
    --proto_path=hedera-protobufs/services \
    --python_out=src/hcs_grpc_client \
    hedera-protobufs/services/timestamp.proto \
    hedera-protobufs/services/basic_types.proto \
    hedera-protobufs/services/consensus_submit_message.proto
