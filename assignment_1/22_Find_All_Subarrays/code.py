array = [1, 2, 3]

def subarrays(arr):
    n = len(arr)
    subarrays = []
    
    for i in range(n):
        for j in range(i, n):
            subarrays.append(arr[i:j+1])
    
    return subarrays


if __name__=="__main__":
    print(subarrays(array))

input("Press any key to exit !")
