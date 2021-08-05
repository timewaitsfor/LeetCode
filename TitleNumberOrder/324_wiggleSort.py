class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        half_l = int(l/2)

        arr_max = []
        arr_max.append(0)

        for i in range(1, l):
            if len(arr_max) < half_l:
                for j in range(len(arr_max)):
                    if nums[i] > nums[arr_max[j]]:
                        arr_max.insert(j+1, i)
                        break
                    else:
                        arr_max.insert(0, i)
                        break
            else:
                if nums[i] > nums[arr_max[0]]:
                    for j in range(half_l)[::-1]:
                        if nums[i] > nums[arr_max[j]]:
                            arr_max.insert(j+1, i)
                            arr_max.pop(0)
                            break

        opt_arr = []
        i = 0
        for k, n in enumerate(nums):
            if k not in arr_max:
                opt_arr.append(n)
                if len(arr_max) != 0:
                    opt_arr.append(nums[arr_max[i]])
                    i+=1

        nums = opt_arr
        print(nums)



nums = [1,5,1,1,6,4]
solution = Solution()
ans = solution.wiggleSort(nums)
