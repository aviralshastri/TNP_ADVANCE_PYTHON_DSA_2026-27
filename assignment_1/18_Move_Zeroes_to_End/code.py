array1 = [0, 1, 0, 3, 12]

def move_zeroes(arr):
    insert_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_index], arr[i] = arr[i], arr[insert_index]
            insert_index += 1

    return arr


if __name__ == "__main__":
    print(move_zeroes(array1))

input("Press any key to exit !")
