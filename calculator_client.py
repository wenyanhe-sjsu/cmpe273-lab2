# In this small program, addends are given as command line arguments
# For example, in "python3 calculator_client.py 3 7"
# Both 3 and 7 are addends sent to the server side

from __future__ import print_function

import sys
import grpc
import calculator_pb2
import calculator_pb2_grpc

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(x = n1, y = n2))
    print("Calculation result: " + str(response.result))


if __name__ == '__main__':
    run()
