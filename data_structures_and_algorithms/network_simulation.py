# python3
from collections import deque

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = deque()
        self.ind = False

    def Process(self, request):
        

        if self.ind == False:
            real_time = request.arrival_time
        else:
            real_time = self.finish_time_[len(self.finish_time_) - 1]
        self.finish_time_.append(real_time + request.process_time)
        
        if self.ind == True and request.arrival_time >= self.finish_time_[0]:
                self.finish_time_.popleft()
        self.ind = True




        if real_time <= request.arrival_time:
            return Response(False, request.arrival_time)
        else:
            if len(self.finish_time_) <= self.size:
                return Response(False, real_time)
            else:
                self.finish_time_.pop()
                return Response(True, -1)


        
def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
