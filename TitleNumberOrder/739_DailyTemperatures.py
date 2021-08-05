class Solution:

    # 暴力法
    def dailyTemperatures(self, T):
        temp_queue = []
        id_queue = []
        opt = [0 for _ in T]
        for idx, val in enumerate(T):
            temp_memo = []
            id_memo = []
            for queue_i, queue_v in zip(id_queue, temp_queue):
                if val > queue_v:
                    opt[queue_i] = idx - queue_i
                else:
                    temp_memo.append(queue_v)
                    id_memo.append(queue_i)
            temp_queue = temp_memo
            id_queue = id_memo
            temp_queue.append(val)
            id_queue.append(idx)
        return opt

    # 暴力法
    def dailyTemperatures02(self, T):
        temp_queue = []
        opt = [0 for _ in T]
        for idx, val in enumerate(T):
            for temp_i in temp_queue[::-1]:
                if val > T[temp_i]:
                    opt[temp_i] = idx - temp_i
                    temp_queue.pop(-1)
            temp_queue.append(idx)

        return opt

    def dailyTemperatures03(self, T):
        temp_stack = []
        opt = [0 for _ in T]
        for idx, val in enumerate(T):
            while temp_stack and T[temp_stack[-1]] < val:
                this_i = temp_stack.pop(-1)
                opt[this_i] = idx - this_i
            temp_stack.append(idx)

        return opt

    def dailyTemperatures04(self, T):
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return opt

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
solution = Solution()
opt = solution.dailyTemperatures03(temperatures)
print(opt)