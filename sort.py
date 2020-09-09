import random
import time

def create_random_list():
    lists = []
    while len(lists) < 5000:
        n = random.randint(1, 5000)
        if n not in lists:
            lists.append(n)
    return lists

# バブルソート
def buble_sort(lists):
    for i in range(0, len(lists)):
        for j in range(len(lists)-1, i, -1):
            if lists[j] > lists[j-1]:
                lists[j], lists[j-1] = lists[j-1], lists[j]
    return lists

# バケットソート
def bucket_sort(lists):
    bucket = [0 for i in range(len(lists))]
    for n in lists:
        bucket[n-1] = n
    return bucket

# 基数ソート
def redix_sort(lists):
    bucket = [list() for i in range(10)]

    for d in range(1, len(str(max(lists)))+1):
        r = 10**(d-1)

        for val in lists:
            key = val // r % 10
            bucket[key].append(val)

        i = 0
        for values in bucket:
            for val in values:
                lists[i] = val
                i += 1

        bucket = [list() for i in range(len(bucket))]

    return lists


# ヒープソート
class heap():
    def __init__(self, lists):
        self.heap = [0 for i in range(len(lists))]
        self.num = 0
        self.target = 0

    def insert(self, a):
        self.heap[self.num] = a
        self.num += 1
        i = self.num
        j = i // 2

        while i > 1 and self.heap[i-1] < self.heap[j-1]:
            self.heap[i-1], self.heap[j-1] = self.heap[j-1], self.heap[i-1]
            i, j = j, i//2

    def deletemin(self):
        self.num -= 1
        r, self.heap[0] = self.heap[0], self.heap[self.num]
        i = 1
        j = i * 2

        while j <= self.num:
            if j + 1 <= self.num and self.heap[j-1] > self.heap[j]:
                j += 1

            if self.heap[i-1] > self.heap[j-1]:
                self.heap[i-1], self.heap[j-1] = self.heap[j-1], self.heap[i-1]

            i, j = j, i*2

        return r

    def heap_sort(self, lists):
        for target in range(len(lists)):
            self.insert(lists[target])

        target = 0
        while self.num > 0:
            lists[target] = self.deletemin()
            target += 1

        return lists

# 選択ソート
def selection_sort(lists):
    length = len(lists)
    for i in range(length-1):
        lowset = i
        lowkey = lists[i]
        for j in range(i+1, length):
            if lists[j] < lowkey:
                lowset = j
                lowkey = lists[j]
        lists[i], lists[lowset] = lists[lowset], lists[i]

    return lists


# 挿入ソート
def insert_sort(lists):
    for i in range(1, len(lists)):
        j = i
        while j >= 1 and lists[j-1] > lists[j]:
            lists[j], lists[j-1] = lists[j-1], lists[j]
            j -= 1


# シェルソート
def shell_sort(lists):
    length = len(lists)
    h = 1
    while h < length / 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, length):
            j = i
            while j >= h and lists[j-h] > lists[j]:
                lists[j], lists[j-h] = lists[j-h], lists[j]
                j -= h

        h = int(h/3)
    return lists

# クイックソート
def quick_sort(lists):
    return quick_sort_sub(lists, 0, len(lists)-1)

def quick_sort_sub(lists, left, right):
    l = left
    r = right
    pivot = lists[int((l+r)/2)]

    while l <= r:
        while lists[l] < pivot:
            l += 1
        while lists[r] > pivot:
            r -= 1

        if l <= r:
            lists[l], lists[r] = lists[r], lists[l]
            l += 1
            r -= 1

    if r > left:
        lists = quick_sort_sub(lists, left, r)
    if l < right:
        lists = quick_sort_sub(lists, l, right)

    return lists

# マージソート
MAX_ELEMENTS = 5000
tmp_array = [None for _ in range(MAX_ELEMENTS)]
def merge_sort(lists, low, high):
    if low >= high:
        return

    mid = int((low+high)/2)
    merge_sort(lists, low, mid)
    merge_sort(lists, mid+1, high)

    for i in range(low, mid+1):
        tmp_array[i] = lists[i]
    j = high
    for i in range(mid+1, high+1):
        tmp_array[i] = lists[j]
        j -= 1
    i = low
    j = high
    for k in range(low, high+1):
        if tmp_array[i] <= tmp_array[j]:
            lists[k] = tmp_array[i]
            i += 1
        else:
            lists[k] = tmp_array[j]
            j -= 1

    return lists

if __name__ == "__main__":
    sort_dict = {}
    random_lists = create_random_list()

    start_time = time.time()
    result = sorted(random_lists)
    processing_time = time.time() - start_time
    sort_dict["system sort    : "] = processing_time
    print("system sort    : {}".format(processing_time))

    # start_time = time.time()
    # result = buble_sort(random_lists)
    # processing_time = time.time() - start_time
    # print("buble sort : {}".format(processing_time))

    start_time = time.time()
    result = bucket_sort(random_lists)
    processing_time = time.time() - start_time
    sort_dict["bucket sort    : "] = processing_time
    print("bucket sort    : {}".format(processing_time))

    start_time = time.time()
    result = redix_sort(random_lists)
    processing_time = time.time() - start_time
    sort_dict["redix sort     : "] = processing_time
    print("redix sort     : {}".format(processing_time))

    heap_class = heap(random_lists)
    start_time = time.time()
    result = heap_class.heap_sort(random_lists)
    processing_time = time.time() - start_time
    sort_dict["heap sort      : "] = processing_time
    print("heap sort      : {}".format(processing_time))
    # print(result)

    start_time = time.time()
    result = selection_sort(random_lists)
    processing_time = time.time() - start_time
    sort_dict["selection sort : "] = processing_time
    print("selection sort : {}".format(processing_time))
    # print(result)

    start_time = time.time()
    result = insert_sort(random_lists)
    processing_time = time.time() - start_time
    sort_dict["insert sort    : "] = processing_time
    print("insert sort    : {}".format(processing_time))
    # print(result)

    start_time = time.time()
    result = shell_sort(random_lists)
    processing_time = time.time() - start_time
    sort_dict["shell sort     : "] = processing_time
    print("shell sort     : {}".format(processing_time))
    # print(result)

    start_time = time.time()
    result = quick_sort(random_lists)
    processing_time = time.time() - start_time
    sort_dict["quick sort     : "] = processing_time
    print("quick sort     : {}".format(processing_time))
    # print(result)

    start_time = time.time()
    result = merge_sort(random_lists, 0, len(random_lists)-1)
    processing_time = time.time() - start_time
    sort_dict["merge sort     : "] = processing_time
    print("merge sort     : {}".format(processing_time))
    # print(result)





