# This script is used to generate gRPC code.  Just run it in a terminal window

python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./calculator.proto
