







if __name__ == '__main__':
    A = [47, 61, 36, 52, 56, 33, 92]
    
    c = 2
    while(1):
        hash_p = {}
        flag = True
        for x in A:
            x = ((10 * x + 4) % c) % 7
            if x in hash_p:
                flag = False
                break
            hash_p[x] = 1
        if(flag):
            print(hash_p)
            break
        if(flag == False):
            c += 1
            continue

    print(c)