array = [1, 3, 4, 5, 6]

def first_missing_positive(array):
    n = len(array)
    freq = {}

    for num in array:
        if num > 0:
            freq[num] = freq.get(num, 0) + 1

    for i in range(1, n + 1):
        if i not in freq:
            return i

    return n + 1

if __name__=="__main__":
    print(first_missing_positive(array))

input("Press any key to exit !")
