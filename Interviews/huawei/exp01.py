# ipt = [4, 2, [0],[1,0],[1,1],[2,0,1]]

lines = "4\n2\n1,0\n1,1\n2,0,1"


ipt_raw = lines.split('\n')
ipt = []

for ipt_ in ipt_raw:
    if ipt_.__contains__(","):
        ipt.append(ipt_.split(','))
    else:
        ipt.append(ipt_)


# ipt = input().split('\n')


task_num = ipt[0]
this_task_num = ipt[1]
task_list = ipt[2:]
task_dict = {}
for ti, task in enumerate(task_list):
    if len(task) == 1:
        task_dict[ti] = None
    else:
        task_dict[ti] = task[1:]

# this_task_line = task_dict[this_task_num]
task_queue = []
task_queue.append(this_task_num)
pro_count = 0
ans = []
while True:
    if len(task_queue) == 0:
        break
    this_task_id = int(task_queue.pop(0))
    this_task_line = task_dict[this_task_id]
    ans.append(this_task_id)
    if this_task_line == None:
        continue
    for this_task_i in this_task_line:
        task_queue.append(this_task_i)

    pro_count += 1
    if pro_count > 100:
        print("-1")
        break

print(ans)
