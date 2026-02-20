array1 = [16, 17, 4, 3, 5, 2]

def find_leaders(arr):
    leaders = []
    max_right = float('-inf')

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    return leaders[::-1]


if __name__ == "__main__":
    print(find_leaders(array1))

input("Press any key to exit !")
