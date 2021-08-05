

def solution(n, k):

    if n<k:
        return None

    if n < 7:
        # print(" ".join(list(map(str, range(1, n+1)))))
        k_tup = range(1, n+1)
    else:
        k_tup = [k - 2, k - 1, k, k + 1, k+2]

        if 1 == k -3:
            k_tup = [1]+ k_tup + ["..."] + [n]
        elif n == k+3:
            k_tup = [1, "..."] + k_tup+ [n]
        elif 1 in k_tup:
            for i, item in enumerate(k_tup[::-1]):
                if item == 1:
                    k_tup = k_tup[len(k_tup)-i-1:]
                    break

            k_tup = k_tup + ["..."] + [n]
        elif n in k_tup:
            for item in k_tup[::-1]:
                if item != n:
                    k_tup.pop(-1)
                else:
                    break

            k_tup = [1, "..."] + k_tup
        else:
            k_tup = [1, "...", k - 2, k - 1, k, k + 1, k + 2, "...", N]

    return " ".join(" ".join(list(map(str, k_tup))))





N = 8
K = 4
# N = 3
# K = 1
ans = solution(N, K)
print(ans)
