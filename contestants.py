# CONTEST FUNCTIONS MUST START WITH contest_
import heapq
import itertools

def contest_sort(l):
    l.sort()

    max_ = 1
    curr = 1
    a, b = itertools.tee(l)
    next(b, None)

    for i, j in zip(a, b):
        if j == i+1:
            curr += 1
        else:
            max_ = max(max_, curr)
            curr = 1

    return max_

def contest_joao_menkes(nums):

    if not nums:
        return 0
    
    nums = set(nums)
    max_total = 0
    for x in nums:
        if (x - 1) not in nums:
            total = 1
            while (x + 1) in nums:
                total += 1
                x += 1
            max_total = max(max_total, total)
            
    return max_total

def contest_hq(h):
    heapq.heapify(h)

    max_ = 1
    curr = 1

    i = heapq.heappop(h)
    while len(h) > 0:
        j = heapq.heappop(h)
        if j == i+1:
            curr += 1
        else:
            curr = 1
        i = j
        max_ = max(max_, curr)
        if max_ >= len(h):
            return max_

    return max_

def contest_consume_set(l):
    s = set(l)

    max_ = 1

    while len(s) > 0:
        curr = 1
        i = s.pop()

        # check up
        j = i+1
        while j in s:
            s.remove(j)
            j += 1
            curr += 1

        # check down
        j = i-1
        while j in s:
            s.remove(j)
            j -= 1
            curr += 1

        max_ = max(max_, curr)
        if max_ >= len(s):
            return max_

    return max_

def contest_blind_set(l):
    s = set(l)

    max_ = 1

    for i in s:
        curr = 1
        # check up
        j = i+1
        while j in s:
            j += 1
            curr += 1

        # check down
        j = i-1
        while j in s:
            j -= 1
            curr += 1

        max_ = max(max_, curr)

    return max_
