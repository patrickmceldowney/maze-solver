from abc import ABCMeta, abstractmethod
from fibonacci_heap import FibHeap
from typing import Self
from queue import Queue
import itertools
import heapq


class PriorityQueue:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def insert(self, node):
        pass

    @abstractmethod
    def minimum(self, node):
        pass

    @abstractmethod
    def remove_minimum(self):
        pass

    @abstractmethod
    def decrease_key(self, node, new_priority):
        pass


class FibPQ(PriorityQueue):
    def __init__(self) -> None:
        self.heap = FibHeap()

    def __len__(self):
        return self.heap.count

    def inesrt(self, node):
        self.heap.insert(node)

    def minimum(self):
        return self.heap.minimum()

    def remove_minimum(self):
        return self.heap.remove_minimum()

    def decrease_key(self, node, new_priority):
        return self.heap.decrease_key(node, new_priority)


class HeapPQ(PriorityQueue):
    def __init__(self) -> None:
        self.pq = []
        self.removed = set()
        self.count = 0

    def __len__(self):
        return self.count

    def insert(self, node):
        entry = node.key, node.value
        if entry in self.removed:
            self.removed.discard(entry)
        heapq.heappush(self.pq, entry)
        self.count += 1

    def minimum(self):
        priority, item = heapq.heappop(self.pq)
        node = FibHeap.Node(priority, item)
        self.insert(node)
        return node

    def remove_minimum(self):
        while True:
            (priority, item) = heapq.heappop(self.pq)
            if (priority, item) in self.removed:
                self.removed.discard((priority, item))
            else:
                self.count -= 1
                return FibHeap.Node(priority, item)

    def remove(self, node):
        entry = node.key, node.value
        if entry not in self.removed:
            self.removed.add(entry)
            self.count -= 1

    def decrease_key(self, node, new_priority):
        self.remove(node)
        node.key = new_priority
        self.insert(node)


class QueuePQ(PriorityQueue):
    def __init__(self) -> None:
        self.pq = Queue.PriorityQueue()
        self.removed = set()
        self.count = 0

    def __len__(self):
        return self.count

    def insert(self, node):
        entry = node.key, node.value
        if entry in self.removed:
            self.removed.discard(entry)

        self.pq.put(entry)
        self.count += 1

    def minimum(self):
        (priority, item) = self.pq.get_nowait()
        node = FibHeap.Node(priority, item)
        self.insert(node)
        return node

    def remove_minimum(self):
        while True:
            (priority, item) = self.pq.get_nowait()
            if (priority, item) in self.removed:
                self.removed.discard((priority, item))
            else:
                self.count -= 1
                return FibHeap.Node(priority, item)

    def remove(self, node):
        entry = node.key, node.value
        if entry not in self.removed:
            self.removed.add(entry)
            self.count -= 1

    def decrease_key(self, node, new_priority):
        self.remove(node)
        node.key = new_priority
        self.insert(node)
