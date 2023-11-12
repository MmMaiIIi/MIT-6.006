class Priority_Queue:
    def __init__(self):
        self.A = []
    
    def insert(self, x):
        self.A.append(x)
    
    def delete_max(self):
        if len(self.A) < 1:
            raise IndexError('pop from empty priority queue')
        return self.A.pop()
    
    @classmethod
    def sort(Queue, A):
        pq = Queue()
        for x in A:
            pq.insert(x)
        out = [pq.delete_max() for _ in A]
        out.reverse()
        return out