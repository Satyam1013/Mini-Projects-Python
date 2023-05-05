import time;

# def calTime():
#     for i in range(500):
#         print(i)

# init = time.time()

# calTime()

# print(time.time() - init)

t = time.localtime()
format_time = time.strftime("%Y/%m/%d  %H:%M:%S",t)
print(format_time)
