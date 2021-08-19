class Solution:

    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:

        memo1 = {}
        for n1 in nums1:
            if n1 in memo1:
                memo1[n1] += 1
            else:
                memo1[n1] = 1

        memo2 = {}
        for n2 in nums2:
            for n_ in memo1.keys():
                n_2 = n_ + n2
                if n_2 in memo2:
                    memo2[n_2] += memo1[n_]
                else:
                    memo2[n_2] = memo1[n_]

        memo3 = {}
        for n3 in nums3:
            for n_ in memo2.keys():
                n_3 = n_ + n3
                if n_3 in memo3:
                    memo3[n_3] += memo2[n_]
                else:
                    memo3[n_3] = memo2[n_]

        memo4 = {}
        for n4 in nums4:
            for n_ in memo3.keys():
                n_4 = n_ + n4
                if n_4 in memo4:
                    memo4[n_4] += memo3[n_]
                else:
                    memo4[n_4] = memo3[n_]

        if 0 in memo4:
            return memo4[0]
        else:
            return 0


solution = Solution()
print(solution.fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1]))