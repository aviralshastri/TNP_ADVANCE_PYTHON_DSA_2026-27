array=[1,5,3,6,2,2,2,5,3,5,6,6,6,8,1]

def ele_freq(array):
    freq={}
    for i in array:
        if freq.get(i,0):
           freq[i]+=1
        else:
            freq[i]=1
    return freq

if __name__=="__main__":
    print(ele_freq(array))

input("Press any key to exit !")
