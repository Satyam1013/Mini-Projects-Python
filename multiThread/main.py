# import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
  print(seconds)
  time.sleep(seconds)
  return seconds
# def main():
#   time1 = time.perf_counter()
#   # func(5)
#   # func(2)
#   # func(4)
  
#   #usefull in downloading so many files in the same time
  
#   t1 = threading.Thread(target=func, args=[5])
#   t2 = threading.Thread(target=func, args=[2])
#   t3 = threading.Thread(target=func, args=[3])
  
#   #it will run in background
#   t1.start()
#   t2.start()
#   t3.start()
  
#   #if you want to wait
#   t1.join()
#   t2.join()
#   t3.join()
  
#   time2 = time.perf_counter()
  
#   print(time2-time1)

# another way to do it you can pass your func here

def poolingDemo():
  with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(func, 4)
    # future2 = executor.submit(func, 1)
    # future3 = executor.submit(func, 3)
    
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())

    #shortcut map method
    l = [1,2,3,4]
    results = executor.map(func, l)
    for result in results:
      print(result)
      
poolingDemo()