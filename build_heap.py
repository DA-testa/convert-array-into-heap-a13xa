# python3
# Aleksandra Červinska 221RDB069 12.grupa

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range (n // 2, -1, -1):
        j = i
        while j < n:
            maz = j
            if j*2+1 < n and data[j*2+1] < data[maz]:
                maz = j*2+1
            if j*2+2 < n and data[j*2+2] < data[maz]:
                maz = j*2+2
            if maz == j:
                break
            data[j], data[maz] = data[maz], data[j]
            swaps.append((j,maz))
            j = maz
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    ievade = input("Input I or F:  ")
    if "I" in ievade:
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    # checks if lenght of data is the same as the said lenght
        assert len(data) == n
    elif "F" in ievade:
        fails = "./tests/" + input("Input filename(04): ")
        if "a" in fails:
            print("wrong file name")
            return
        with open(fails) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
    else:
        print("wrong input")
        return
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    swaps_n = len(swaps)
    assert swaps_n < 4*len(data)

    # output all swaps
    print(swaps_n)
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
