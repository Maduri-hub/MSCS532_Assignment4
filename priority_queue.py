class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            raise IndexError("extract_max from an empty priority queue")
        self._swap(0, len(self.heap) - 1)
        max_task = self.heap.pop()
        self._heapify_down(0)
        return max_task

    def increase_key(self, task, new_priority):
        index = self.heap.index(task)
        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

pq = PriorityQueue()
pq.insert(Task(1, 5, "08:00", "10:00"))
pq.insert(Task(2, 3, "09:00", "11:00"))
pq.insert(Task(3, 8, "07:00", "09:00"))

while not pq.is_empty():
    task = pq.extract_max()
    print(f"Task ID: {task.task_id}, Priority: {task.priority}")