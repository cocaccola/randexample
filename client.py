import messages_pb2
import messages_pb2_grpc
import grpc
import time
import random
from datetime import datetime
from os import environ

def main():

    address = environ.get('ADDRESS', 'localhost:50051')
    print(f"address: {address}")

    # sleep for a random amount of time to stagger requests with other clients
    random.seed()
    sleep_time = random.randint(0, 3)
    print(f"sleeping for {sleep_time}")
    time.sleep(sleep_time)

    request = messages_pb2.Request(start=0, end=100)
    with grpc.insecure_channel(address) as channel:
        stub = messages_pb2_grpc.RandomNumberGeneratorStub(channel)
        while True:
            try:
                n = stub.GetRandomNumber(request)
            except grpc.RpcError as e:
                print(f"{datetime.now()} ERROR {e.code()}: {e.details()}")
            else:
                print(f"{datetime.now()} Received: {n.num}")

            time.sleep(10)

if __name__ == '__main__':
    main()

