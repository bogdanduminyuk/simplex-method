
def PrintOut():
    GetDual()
    nCost = 0

    for x in range(n):
        out_string = ''

        for y in range(m):
            nCost += aCost[x][y] * aRoute[x][y]
            if aRoute[x][y] == 0:
                out_string += '%i(0)\t' % (aCost[x][y])
            else:
                out_string += '%i(%i)\t' % (aCost[x][y], aRoute[x][y] + 0.5)

        # print(' : %i' % aSupply[x])
        print(out_string)
    print('F(x): ', round(nCost))


def NorthWest():
    """ The simplest method to get an initial solution.
    Not the most efficient"""
    global aRoute
    u = 0
    v = 0
    aS = [0] * m
    aD = [0] * n
    while u <= n - 1 and v <= m - 1:
        if aDemand[v] - aS[v] < aSupply[u] - aD[u]:
            z = aDemand[v] - aS[v]
            aRoute[u][v] = z
            aS[v] += z
            aD[u] += z
            v += 1
        else:
            z = aSupply[u] - aD[u]
            aRoute[u][v] = z
            aS[v] += z
            aD[u] += z
            u += 1


def NotOptimal():
    global PivotN
    global PivotM
    nMax = -nVeryLargeNumber
    GetDual()
    for u in range(0, n):
        for v in range(0, m):
            x = aDual[u][v]
            if x > nMax:
                nMax = x
                PivotN = u
                PivotM = v
    return nMax > 0


def GetDual():
    global aDual
    for u in range(0, n):
        for v in range(0, m):
            aDual[u][v] = -0.5  # null value
            if aRoute[u][v] == 0:
                aPath = FindPath(u, v)
                z = -1
                x = 0
                for w in aPath:
                    x += z * aCost[w[0]][w[1]]
                    z *= -1
                aDual[u][v] = x


def FindPath(u, v):
    aPath = [[u, v]]
    if not LookHorizontaly(aPath, u, v, u, v):
        print('Path error, press key', u, v)
        input()
    return aPath


def LookHorizontaly(aPath, u, v, u1, v1):
    for i in range(0, m):
        if i != v and aRoute[u][i] != 0:
            if i == v1:
                aPath.append([u, i])
                return True  # complete circuit
            if LookVerticaly(aPath, u, i, u1, v1):
                aPath.append([u, i])
                return True
    return False  # not found


def LookVerticaly(aPath, u, v, u1, v1):
    for i in range(0, n):
        if i != u and aRoute[i][v] != 0:
            if LookHorizontaly(aPath, i, v, u1, v1):
                aPath.append([i, v])
                return True
    return False  # not found


def BetterOptimal():
    global aRoute
    aPath = FindPath(PivotN, PivotM)
    nMin = nVeryLargeNumber
    for w in range(1, len(aPath), 2):
        t = aRoute[aPath[w][0]][aPath[w][1]]
        if t < nMin:
            nMin = t
    for w in range(1, len(aPath), 2):
        aRoute[aPath[w][0]][aPath[w][1]] -= nMin
        aRoute[aPath[w - 1][0]][aPath[w - 1][1]] += nMin


# my example
aCost = [
    [2, 4, 1, 6, 7],
    [3, 100, 5, 100, 2],
    [8, 9, 6, 3, 4],
]
aDemand = [80, 60, 70, 100, 50]
aSupply = [120, 110, 130]

n = len(aSupply)
m = len(aDemand)
nVeryLargeNumber = 99999999999
# add a small amount to prevent degeneracy
# degeneracy can occur when the sums of subsets of supply and demand equal
elipsis = 0.001
for k in aDemand:
    k += elipsis / len(aDemand)
aSupply[1] += elipsis
# initialisation
aRoute = []
for x in range(n):
    aRoute.append([0] * m)
aDual = []
for x in range(n):
    aDual.append([-1] * m)
NorthWest()
PivotN = -1
PivotM = -1
# MAIN
while NotOptimal():
    BetterOptimal()

PrintOut()
