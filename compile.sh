./venv/bin/python -m grpc_tools.protoc \
    --proto_path=hedera-protobufs/mirror \
    --proto_path=hedera-protobufs/services \
    --python_out=src/hcs_grpc_client \
    --grpc_python_out=src/hcs_grpc_client \
    --dependency_out=deps.txt \
    hedera-protobufs/mirror/ConsensusService.proto
