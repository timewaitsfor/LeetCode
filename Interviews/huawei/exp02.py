a = input().split(',')
i, x = int(a[0]), float(a[1])
tt = (i+1)*i/2
remain = x-tt
if remain <= 0 or remain >= (i+1):
    print('0.0000')
else:
    m = i//2
    s = 1
    for j in range(m):
        s = s*(i-j)/(j+1)
    ans = (s-1)/(1<<i)*remain
    ans = str(ans).split('.')
    tail = ans[1] + '0000'
    print(ans[0]+'.'+tail[:4])