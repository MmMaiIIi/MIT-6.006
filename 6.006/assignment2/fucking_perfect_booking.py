def merge_booking(B1, B2):
    B = []
    n, m = len(B1), len(B2)
    i, j, x= 0, 0, 0 # x 是关键的更迭点
    while i + j < n + m:
        if i < n: k1, s1, e1 = B1[i] # 边界考虑
        if j < m: k2, s2, e2 = B2[j]
        if j == m:
            k, s, x = k1, max(x, s1), e1
            i += 1
        elif i == n:
            k, s, x = k2, max(x, s2), e2
            j += 1
        else:
            x = max(x, min(s1, s2))
            if s2 >= e1:
                k, s, x = k1, x, e1
                i += 1
            elif s1 >= e2:
                k, s, x = k2, x, e2
                j += 1
            elif x < s2: # critical -> which means s1 <= x < s2
                k, s, x = k1, x, s2 # cannot be k1, s1, s2
            elif x < s1:
                k, s, x = k2, x, s1
            else: # x >= s1 and x >= s2
                k, s, x = k1 + k2, x, min(e1, e2)
                if x == e1: i += 1
                if x == e2: j += 1
        B.append((k, s, x))

    B_ = [B[0]]
    for k, s, t in B[1:]:
        k_, s_, t_ = B_[-1]
        if(k == k_) and (t_ == s):
            B_.pop()
            s = s_
        B_.append((k, s, t))
    return B_

def satisfying_booking(R):
    if len(R) == 1:
        s, t = R[0]
        return ((1, s, t), )

    m = len(R) // 2
    R1, R2 = R[:m], R[m:]
    B1 = satisfying_booking(R1)
    B2 = satisfying_booking(R2)
    B = merge_booking(B1, B2)
    return B