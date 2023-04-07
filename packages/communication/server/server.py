import grpc
from ..protocol_buffers import evaluate_pb2
from ..protocol_buffers import evaluate_pb2_grpc
from concurrent import futures

class PhaFic(evaluate_pb2_grpc.PhaFicServicer):
    def evaluate(self, request, context):
        print("evaluate function called")
        print("request: ", request)
        return evaluate_pb2.response(error_code=1, distance=4.0, time_taken=45)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    evaluate_pb2_grpc.add_PhaFicServicer_to_server(PhaFic(), server)
    print("Server Started!")
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

main()
