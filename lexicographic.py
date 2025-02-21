# Testing for Lexicographic

# Algorithm Phases:

# 1-Find the largest x such that p[x] < p[x+1].
# (If no such x exists, the permutation is the last permutation.) -> break statement
# 2-Find the largest y such that p[x] < p[y].
# 3-Swap p[x] and p[y].
# 4-Reverse P[x+1 .. n].
# 5-Loop untill break statement reaches.

def lexicographic_ordering(n):
    def swap(_list, index1, index2):
        _list[index1], _list[index2] = _list[index2], _list[index1]
        return _list

    items = [i for i in range(n)]

    yield items

    while True:
        #step 1
        largets_i = -1
        for i in range(len(items)-1):
            if items[i] < items[i+1]:
                largets_i = i
        if largets_i == -1:
            break

        #step 2
        largest_j = 0
        for j in range(len(items)):
            if items[largets_i] < items[j]:
                largest_j = j

        #step 3
        items = swap(items, largets_i, largest_j)

        #step 4
        left_half = items[:largets_i+1]
        right_half = items[largets_i+1:]
        right_half.reverse()
        items = left_half + right_half

        yield items