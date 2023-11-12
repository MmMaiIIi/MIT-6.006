def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    if len(S) == 0: return
    
    k = len(S[0])
    D = Construct_A(T, k)

    for S_i in S:
        A.append(single_count_anagram(D, S_i))

    print(A)
    return tuple(A)


def Construct_A(A, k):
    n = len(A)
    C = [None] * n 
    for i in range(n):
        C[i] = ord(A[i]) - 87

    D = [0] * int(1e7)

    for i in range(n - k + 1):
        D[construct_2k_digit(C, i, k)] += 1

    return D


def single_count_anagram(D, B):
    k = len(B)
    C = [None] * k
    for i in range(k):
        C[i] = ord(B[i]) - 87

    return D[construct_2k_digit(C, 0, k)]


def construct_2k_digit(C, i, k):
    B = C[i : i + k]
    B.sort()
    num = 0
    for j in range(0, k):
        num *= 100
        num += B[j]

    # 使用hash来压缩空间  （有概率会出错
    a, b, p, e = 437213, 73117, 190237, int(1e7)
    num = ((a*num + b) % p) % e

    return num