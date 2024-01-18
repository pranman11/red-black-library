from time import time
from math import floor

class MinHeapNode:
    def __init__(self, data, priority, insert_time):
        self.data = data
        self.priority = priority
        self.insert_time = insert_time

class MinBinaryHeap:
    def __init__(self):
        self.nodes = []

    def add(self, data, priority):
        node = MinHeapNode(data, priority, time())  
        self.nodes.append(node)
        if len(self.nodes) == 1:
            return
        prev_index = len(self.nodes) - 1
        i = floor(prev_index / 2)
        while i >= 0 and self.nodes[i].priority >= node.priority:
            if self.nodes[i].priority == node.priority:
                if self.nodes[i].insert_time > node.insert_time:
                    self.nodes[i], self.nodes[prev_index] = self.nodes[prev_index], self.nodes[i]
                    break
            self.nodes[i], self.nodes[prev_index] = self.nodes[prev_index], self.nodes[i]
            prev_index = i
            i = floor((i - 1) / 2)

    def get_root(self):
        # null check ??
        return self.nodes[0] if self.nodes else None

    def get_heap_data(self):
        return str([node.data for node in self.nodes])

    def get_min_child(self, left_child, right_child):
        if self.nodes[left_child].priority > self.nodes[right_child].priority:
            return right_child
        if self.nodes[left_child].priority == self.nodes[right_child].priority:
            return left_child if self.nodes[left_child].insert_time < self.nodes[right_child].insert_time else right_child
        return left_child

    def heapify(self):
        i = 0
        while True:
            min_child = i
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child >= len(self.nodes) and right_child >= len(self.nodes):
                break
            if right_child >=len(self.nodes):
                min_child = self.get_min_child(min_child, left_child)
            else:
                candidate = self.get_min_child(left_child, right_child)
                min_child = self.get_min_child(min_child, candidate)
            if min_child != i:
                self.nodes[i], self.nodes[min_child] = self.nodes[min_child], self.nodes[i]
                i = min_child
            else:
                break
        
    def remove_min(self):
        if len(self.nodes) == 0:
            return None
        min = self.nodes[0]
        self.nodes[0] = self.nodes[len(self.nodes) - 1]
        self.nodes = self.nodes[:len(self.nodes) - 1]
        if len(self.nodes) == 1:
            return min
        self.heapify()
        return min