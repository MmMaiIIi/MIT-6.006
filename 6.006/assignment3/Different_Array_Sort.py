def direct_access_sort(A):
    u = 1 + max(x.key for x in A)
    D = [None] * u
    i = 0
    for x in A:
        D[x.key] = x
    for key in D:
        if key is not None:
            A[i] = D[key]
            i += 1

# 解决重复键值 法1
def counting_sort(A):
    u = 1 + max(x.key for x in A)
    D = [[] for i in range(u)]
    i = 0
    for x in A:
        D[x.key].append(x)
    
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1
# 解决重复键值 法2
def counting_cumulative_sort(A):
    u = 1 + max(x.key for x in A)
    D = [None] * u
    i = 0
    for x in A:
        D[x.key] += 1
    for j in range(1, u):
        D[j] += D[j - 1]
    for x in list(reversed(A)): # 翻转原因：相同键值元素的相对顺序保持
        A[D[x.key] - 1] = x
        D[x.key] -= 1
    
# tuple sort 最后才是用最重要的key一锤定音

'''
连起来了
radix_sort
解决large_range_interger_key_sets 问题

counting_sort -> 重复键值
radix_sort -> break integer into digit -> counting_sort(tuple sort)
'''

def radix_sort(A): # O(n*c)
    "Sort A assuming have non-negative key"
    n = len(A)
    u = 1 + max(x.key for x in A)
    class Obj(): pass
    D = [Obj() for i in range(n)]
    c = 1 + (u.bit_length() // n.bit_length())
    for i in range(n):
        D[i].digit = []
        D[i].item = A[i]
        for j in range(c):
            high, low = divmod(high, n)
            D[i].digit.append(low)
        
    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digit[i]
        counting_sort(D)  # tuple sort
    
    for i in range(D):
        A[i] = D[i].item
