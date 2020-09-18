# class program
#  {
#      static void Main(string[] args)
#      {
#          int i;
#          i = x(x(8));
#      }
#      static int x(int n)
#      {
#          if (n <= 3)
#              return 1;
#          else
#              return x(n - 2) + x(n - 4) + 1;
#      }
#  }
CNT = 0

class Runner(object):
    def __init__(self):
        self.cnt = 0
        pass

    def source_xf(self, n):
        self.cnt += 1
        if n <= 3:
            return 1
        else:
            return self.source_xf(n - 2) + self.source_xf(n - 4) + 1


# def source_xf(n):
#     CNT += 1
#     if n <= 3:
#         return 1
#     else:
#         return source_xf(n - 2) + source_xf(n - 4) + 1
#
# def x(n, cnt):
#     cnt += 1
#     if n <= 3:
#         return 1, cnt
#     else:
#         return x(n - 2, cnt) + x(n - 4, cnt) + 1, cnt


def binary_search():
    pass



if __name__ == '__main__':

    # aet 1:
    # p1, p1_cnt = x(8, 0)
    # x_res, x_cnt = x(p1, p1_cnt)
    # print(x_cnt)
    # CNT = 0
    shelf = Runner()
    shelf.source_xf(shelf.source_xf(8))

    print(shelf.cnt)

