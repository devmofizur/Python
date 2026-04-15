# Multiprocessing is the manual process of telling the OS, "These tasks are independent; please run them on different cores simultaneously." Without those specific commands (e.g., multiprocessing.Process(target=heavy_logic, args=(list,))), the additional cores of  CPU stay "parked" and unused for that specific application, leaving the heavy lifting to only one core.


import os
import time
import multiprocessing

def independent_function_2D(nums=[]):
    print(f"Process ID: {os.getpid()} | Handling task...")
    for i in nums:
        time.sleep(0.5)
        print("2D : ",i*i)

def independent_function_3D(nums=[]):
    print(f"Process ID: {os.getpid()} | Handling task...")
    for i in nums:
        time.sleep(0.7)
        print("3D : ",i*i*i)

def independent_function_4D(nums=[]):
    print(f"Process ID: {os.getpid()} | Handling task...")
    for i in nums:
        time.sleep(0.3)
        print("4D : ",i*i*i*i)

if __name__ == "__main__":

    
    list = [1, 18, 994, 56, 23] # 810, 44, 672, 129, 3, 550, 881, 34, 912, 102, 67, 431, 725, 19, 2]
    t = time.time()

    task1 = multiprocessing.Process(target=independent_function_2D, args=(list,))
    task2 = multiprocessing.Process(target=independent_function_3D, args=(list,))
    task3 = multiprocessing.Process(target=independent_function_4D, args=(list,))

    task1.start()
    print("Task 1 started")
    task2.start()
    print("Task 2 started")
    task1.join()
    task3.start()
    print("Task 3 started")
    task2.join()
    task3.join()
    
   
    print("All task finished in ",time.time()-t, "sec")