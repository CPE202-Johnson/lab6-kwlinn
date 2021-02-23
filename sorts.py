import random
import time

def selection_sort(list):
    count = 0
    for i in range(0, len(list) - 1):
        min_idx = i  
        for j in range(i + 1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
            count += 1
        list[min_idx], list[i] = list[i], list[min_idx]        
    return count
    
def insertion_sort(list):
    count = 0
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            list[j - 1], list[j]  = list[j], list[j - 1]
            j -= 1
        count += 1
    return count

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

