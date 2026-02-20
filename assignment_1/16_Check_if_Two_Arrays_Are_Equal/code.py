array1=[1,3,3,4,5]
array2=[1,1,3,4,5]


def check_same(array1, array2):
    if len(array1) != len(array2):
        return False

    freq = {}

    for num in array1:
        freq[num] = freq.get(num, 0) + 1

    for num in array2:
        if not freq.get(num,0):
            return False
        freq[num] -= 1
        if freq[num] < 0:
            return False

    return True


if __name__=="__main__":
    print(check_same(array1,array2))

input("Press any key to exit !")
