import time
import threading


n=0
def do(nums, first, second):
    global n
    n+=1
    for i in nums[first:second]:
        print("start: ",i)

threads = []
x = 0
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
th = int(input("how many thread\n"))
to_add = int(len(nums)/th)
for _ in range(0,th):
    first = x
    second = first+to_add
    # print(first, second)
    t = threading.Thread(target=do, args= (nums, first, second))
    t.start()
    threads.append(t)
    x = x+to_add

for thread in threads:
    thread.join()