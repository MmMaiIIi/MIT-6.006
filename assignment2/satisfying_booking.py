import operator
def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    
    '''
    数组记录数量，每次出上一个，维护好好一个边界
    from start to cost_s_t[0]: met a end, append(start, end, c), start = end
    two pointer: i, j, i -> start, j -> end
    find a patern: the number of booking room equals to the number of non-adjacent stop-point 
    '''
    m = len(R)
    R = sorted(R, key=operator.itemgetter(0))
    stop_point = list()
    for items in R:
      for item in items:
        stop_point.append(item)

    stop_point = list(set(stop_point))
    stop_point.sort()
    print('\n', stop_point, "\n", end='')

    # record the number of people in the room in each period of time
    people_in_room = [0] * m * 100 # OPTIMIZATION! just record the number in each point stayed in each period
    for cost_s_t in R:
      for i in range(cost_s_t[0], cost_s_t[1]):
        people_in_room[i] += 1

    print()
    # deliminate the repeat number in R
    R1 = R
    R = []
    seen_keys = set()
    for t in R1:
        key = t[0]
        if key not in seen_keys:
            R.append(t)
            seen_keys.add(key)
    R.sort()
    m = len(R)
    for c in R: print(" ", c[0], end='')
    print()

    # APPEND ACCORDING TO EACH STOP_POINT
    # NEED TO TAKE THE COVER SITUATION INTO CONSIDERATION!
    i, j, st = 0, 0, 0
    while j < m:
      while stop_point[i] < R[j][0]:
        st = i
        i += 1
        while stop_point[i] <= R[j][0] and people_in_room[stop_point[i] - 1] == people_in_room[stop_point[i]]:
          i += 1
        if(people_in_room[stop_point[st]]): 
          B.append((people_in_room[stop_point[st]], stop_point[st], stop_point[i]))
          # st need to put into stop_point hhh
      j += 1
      while j < m - 1 and people_in_room[R[j][0]] == people_in_room[R[j + 1][0]]:
        j += 1
    
    n = len(stop_point)
    end = stop_point[n - 1]
    while stop_point[i] <= end:
      st = i
      i += 1
      B.append((people_in_room[stop_point[i] - 1], stop_point[st], stop_point[i]))
      if stop_point[i] == end:
        break
    
    print('\n', B)
    return tuple(B)


