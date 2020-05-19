class BinaryHeap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def get(self, i):
        return self.items[i]

    def get_min(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def extract_min(self):
        if self.size() == 0:
            return None
        largest = self.get_min()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.min_heapify(0)
        return largest

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= self.size() - 1 and self.get(l)[1] < self.get(i)[1]):
            largest = l
        else:
            largest = i
        if (r <= self.size() - 1 and self.get(r)[1] < self.get(largest)[1]):
            largest = r
        if (largest != i):
            self.swap(largest, i)
            self.min_heapify(largest)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def add(self, key):
        index = self.size()
        self.items.append(key)

        while (index != 0):
            p = self.parent(index)
            if self.get(p)[1] > self.get(index)[1]:
                self.swap(p, index)
            index = p

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False
