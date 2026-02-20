array1 = [7, 10, 4, 3, 20, 15]
k = 3

def kth_smallest(array, k):
    array.sort()
    return array[k - 1]


if __name__ == "__main__":
    print(kth_smallest(array1, k))

input("Press any key to exit !")
