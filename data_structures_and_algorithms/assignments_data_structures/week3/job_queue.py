# python3
import heapq

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        times_workers = [(0,w) for w in range(self.num_workers)]

        heapq.heapify(times_workers)

        for i in range(len(self.jobs)):

            (self.start_times[i], self.assigned_workers[i]) = heapq.heappop(times_workers)
            heapq.heappush(times_workers, (self.start_times[i] + self.jobs[i], self.assigned_workers[i]))





    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
