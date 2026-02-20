array=[1,4,52,6,0]

def min_max(array):
    curr_max=float("-inf")
    curr_min=float("inf")

    for i in range(len(array)):
        curr_max=max(array[i],curr_max)
        curr_min=min(array[i],curr_min)

    return curr_max,curr_min

if __name__=="__main__":
    arr_min, arr_max = min_max(array)
    print("Max:",arr_min,"Min:",arr_max)

input("Press any key to exit !")
