import heapq

class Test:
    def test(self):
        # create minheap
        minheap = []
        heapq.heapify(minheap)

        # add element
        heapq.heappush(minheap, 10)
        heapq.heappush(minheap, 8)
        heapq.heappush(minheap, 9)
        heapq.heappush(minheap, 2)
        heapq.heappush(minheap, 1)
        heapq.heappush(minheap, 11)

        print(minheap)

        # peek
        print(minheap[0])

        # delete
        heapq.heappop(minheap)

        # Size
        len(minheap)

        # iteration
        while len(minheap) != 0:
            print(heapq.heappop(minheap))


t = Test()
t.test()