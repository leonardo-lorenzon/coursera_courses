# python3
from collections import deque

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = dict()
        self.responses = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_responses(self):
        for i in self.responses:
            print(i)

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "add":
            hash_value = self._hash_func(query.s)
            if hash_value in self.elems:
                if query.s not in self.elems[hash_value]:
                    self.elems[hash_value].appendleft(query.s)
            else:
                self.elems[hash_value] = deque([query.s])

        elif query.type == "del":
            hash_value = self._hash_func(query.s)
            if hash_value in self.elems:
                if query.s in self.elems[hash_value]:
                    self.elems[hash_value].remove(query.s)

        elif query.type == "find":
            hash_value = self._hash_func(query.s)
            if hash_value in self.elems:
                if query.s in self.elems[hash_value]:
                    self.responses.append("yes")
                else:
                    self.responses.append("no")
            else:
                self.responses.append("no")

        else:
            if query.ind in self.elems and len(self.elems[query.ind])> 0:
                response = self.elems[query.ind][0]
                for i in range(1,len(self.elems[query.ind])):
                    response += " " + self.elems[query.ind][i]
                self.responses.append(response)
            else:
                self.responses.append("")

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
        self.write_responses()

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
