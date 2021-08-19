from datetime import datetime
import time

a=datetime.now()
# time.sleep(60)
b=datetime.now()

while True:
    time.sleep(10)
    b = datetime.now()
    secondsDiff = (b-a).seconds
    if secondsDiff < 60:
        print(secondsDiff, "秒")
    else:
        # minutesDiff = round(secondsDiff / 60, 1)
        minutesDiff = secondsDiff // 60
        secondsDiff = secondsDiff % 60
        print(minutesDiff, "分钟", secondsDiff, "秒")
    # print(minutesDiff)

# res = (b-a).seconds
# print(a)
# print(res)