array1 = [2,4,5,1,6]
array2 = [5,3,6,2,4,2]

def intersection(array1, array2):
    freq = {}
    intersection_ele = []

    for i in range(len(array1)):
        if not freq.get(array1[i], 0):
            freq[array1[i]] = 1
            
    for i in range(len(array2)):
        if freq.get(array2[i], 0):
            intersection_ele.append(array2[i])
            freq[array2[i]] = 0

    return intersection_ele


if __name__ == "__main__":
    print(intersection(array2, array1))

input("Press any key to exit !")
