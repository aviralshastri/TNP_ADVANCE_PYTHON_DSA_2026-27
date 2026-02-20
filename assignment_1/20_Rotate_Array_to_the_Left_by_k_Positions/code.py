array=[1,45,6,2,5]
k=2

def left_rotate(array, k):
    n = len(array)
    k = k % n
    return array[k:] + array[:k]

if __name__ == "__main__":
    print(left_rotate(array, k))

input("Press any key to exit !")
