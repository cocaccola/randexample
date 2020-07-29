import argparse
import messages_pb2
import messages_pb2_grpc
import grpc
import random
import time
from concurrent import futures
from datetime import datetime

class RandomNumberGeneratorServicer(messages_pb2_grpc.RandomNumberGeneratorServicer):

    def __init__(self, kind):
        random.seed()
        self.kind = kind

    def GetRandomNumber(self, request, context):
        print(f"{datetime.now()} {self.kind} Received request from {context.peer()}")
        return messages_pb2.RandomNumber(
           num=random.randint(request.start, request.end)
        )


def main():

    parser = argparse.ArgumentParser(description="random number service")
    parser.add_argument(
        'kind',
        metavar='kind',
        type=str,
        choices=['prod', 'canary'],
        default='prod',
        help='kind of deployment (prod or canary)'
    )
    args = parser.parse_args()

    server = grpc.server(futures.ThreadPoolExecutor())

    messages_pb2_grpc.add_RandomNumberGeneratorServicer_to_server(
        RandomNumberGeneratorServicer(args.kind), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()
