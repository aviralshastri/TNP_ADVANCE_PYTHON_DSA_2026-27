
array=[1,2,3,4,5,6,5,2]

def remove_dupli(array):
    seen = set()
    i = 0
    while i < len(array):
        if array[i] in seen:
            array.pop(i)
        else:
            seen.add(array[i])
            i += 1
    return array


if __name__=="__main__":
    print(remove_dupli(array))

input("Press any key to exit !")
