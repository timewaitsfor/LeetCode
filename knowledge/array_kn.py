# 1. create an array
a = []

# 2. add element
# time complexity: O(1)
a.append(1)
a.append(2)
a.append(3)

# 3. insert element
# time complexity: O(N)
a.insert(2, 99)

# 4. access element
# time complexity: O(1)
tmp = a[2]

# 5. update element
a[2] = 88

# 6. remove element
# time complexity: O(N)
a.remove(88)
a.pop(1)
a.pop() # time complexity: O(1)

# 7. get array size
size = len(a)

# 8. iterate array
# time complexity: O(N)

for i in a:
    pass
for idx,val in enumerate(a):
    pass
for i in range(0, len(a)):
    pass

# 9. find an element
# time complexity: O(N)
idx = a.index(2)

# 10. sort an array
# time complexity: O(NlogN)

a.sort() # from small to big
a.sort(reverse=True) # from big to small