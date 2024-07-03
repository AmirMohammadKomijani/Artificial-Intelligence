indexes = list(range(25))

Mycondition = [
            # horizontal
            (indexes[0], indexes[1], indexes[2], indexes[3]),
            (indexes[1], indexes[2], indexes[3], indexes[4]),
            (indexes[5], indexes[6], indexes[7], indexes[8]),
            (indexes[6], indexes[7], indexes[8], indexes[9]),
            (indexes[10], indexes[11], indexes[12], indexes[13]),
            (indexes[11], indexes[12], indexes[13], indexes[14]),
            (indexes[15], indexes[16], indexes[17], indexes[18]),
            (indexes[16], indexes[17], indexes[18], indexes[19]),
            (indexes[20], indexes[21], indexes[22], indexes[23]),
            (indexes[21], indexes[22], indexes[23], indexes[24]),

            # vertical
            (indexes[0], indexes[5], indexes[10], indexes[15]),
            (indexes[5], indexes[10], indexes[15], indexes[20]),
            (indexes[1], indexes[6], indexes[11], indexes[16]),
            (indexes[6], indexes[11], indexes[16], indexes[21]),
            (indexes[2], indexes[7], indexes[12], indexes[17]),
            (indexes[7], indexes[12], indexes[17], indexes[22]),
            (indexes[3], indexes[8], indexes[13], indexes[18]),
            (indexes[8], indexes[13], indexes[18], indexes[23]),
            (indexes[4], indexes[9], indexes[14], indexes[19]),
            (indexes[9], indexes[14], indexes[19], indexes[24]),

            # diagonal
            (indexes[0], indexes[6], indexes[12], indexes[18]),
            (indexes[6], indexes[12], indexes[18], indexes[24]),
            (indexes[4], indexes[8], indexes[12], indexes[16]),
            (indexes[8], indexes[12], indexes[16], indexes[20]),
            (indexes[1], indexes[7], indexes[13], indexes[19]),
            (indexes[5], indexes[11], indexes[17], indexes[23]),
            (indexes[3], indexes[7], indexes[11], indexes[15]),
            (indexes[9], indexes[13], indexes[17], indexes[21]),

        ]

#print(Mycondition[1][2])

ls = (True,True,False,True,False)
ls1 = (True,True,False,False,False)
ls2 = (True,False,False,False,False)

lss = [ls,ls1,ls2]

ans = int()
def findIndex(check):
    res = int()
    for idx in range(len(check)):
        if check[idx] is False:
            res = idx
            break
    return res


for idx in lss:
    if idx.count(False) == 3:
        ans = lss.index(idx)
        x = findIndex(idx)

print(ans,x)
print(Mycondition[ans][x])



