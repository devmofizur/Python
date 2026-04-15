# Multithreading is the manual process of telling the OS, "These tasks are independent; please manage them concurrently within this process." Without those specific commands (e.g., threading.Thread(target=independent_function, args=(list,))), the rest of the CPU's power stays "parked" and unused for that specific application, as the program will only execute one instruction at a time in a single sequence.
import os
import time
import threading

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

    task1 = threading.Thread(target=independent_function_2D, args=(list,))
    task2 = threading.Thread(target=independent_function_3D, args=(list,))
    task3 = threading.Thread(target=independent_function_4D, args=(list,))

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
