array=[-10, -3, 5, 6, -2]

def max_product_pair(array):
    if len(array) < 2:
        return None
    
    array.sort()
    
    product1 = array[-1] * array[-2]
    product2 = array[0] * array[1]
    
    if product1 > product2:
        return (array[-1], array[-2])
    else:
        return (array[0], array[1])


if __name__=="__main__":
    print(maxProductPair(array))

input("Press any key to exit!")
