import os

def duplicate(data):
    #Brute Force approach O(N2)
    print(f"data {sorted(data)}")
    sorted_data = sorted(data)
    start_index =0
    end_index = len(sorted_data)
    for i in range(start_index,end_index-1):
        if sorted_data[i] == sorted_data[i+1]:
            return True
    return False

def check_for_abs(data):
    #TODO

if __name__ == '__main__':

    print(duplicate([1,2,1,4,3]))
    print(duplicate([1, 2, 6, 4, 3]))
    print(duplicate([1,4,5,4,3,4]))