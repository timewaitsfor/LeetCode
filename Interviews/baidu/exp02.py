a= [1,2,3,4,4,5]


def solution(nums):
    # memo = {}
    # new_memo = []
    length = len(nums)
    # for i in range(length):
    i = 0
    k = 0
    while True:
        if k >= length:
            break
        if i==0:
            continue

        for j in range(i):
            if nums[i] == nums[j]:
                nums.pop(i)
            else:
                i+=1
        k+=1

    print(nums)

solution(a)



