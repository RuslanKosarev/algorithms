
# evaluate height of tree defined as a list of parents


def tree_height(parents):
    n = len(parents)

    a = [[] for i in range(n + 1)]
    for i in range(n):
        a[parents[i]] += [i]

    root, lev = a[-1], 0
    while len(root):
        q, root = root, []
        for b in q:
            root += a[b]
        lev += 1

    return lev


tree = [4, -1, 4, 1, 1]
print(tree_height(tree))




