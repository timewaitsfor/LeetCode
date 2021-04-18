def maxDensity(a, n):
    import heapq
    pq = []
    heapq.heapify(pq)
    result = 0
    k = 0
    for i in range(n):
        k += 1
        heapq.heappush(pq, (a[i], i))
        while pq[0][1] <= i - k:
            k -= 1
            heapq.heappop(pq)
        while pq and pq[0][0] < k:
            k -= 1
            heapq.heappop(pq)
        result = max(result, k)
    return result

# a = [1,3,4,5,2]
a = [3, 1, 4, 5, 2]
n = 5
print(maxDensity(a, n))