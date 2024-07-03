import random


def findIndex(check):
    res = int()
    for idx in range(len(check)):
        if check[idx] is None:
            res = idx
            break
    return res





def ai_action(game_state):

    Ch_Idx = 0
    idx = 0
    indexes = list(range(25))
    condition = [
            # horizontal
            (game_state[0], game_state[1], game_state[2], game_state[3]),
            (game_state[1], game_state[2], game_state[3], game_state[4]),
            (game_state[5], game_state[6], game_state[7], game_state[8]),
            (game_state[6], game_state[7], game_state[8], game_state[9]),
            (game_state[10], game_state[11], game_state[12], game_state[13]),
            (game_state[11], game_state[12], game_state[13], game_state[14]),
            (game_state[15], game_state[16], game_state[17], game_state[18]),
            (game_state[16], game_state[17], game_state[18], game_state[19]),
            (game_state[20], game_state[21], game_state[22], game_state[23]),
            (game_state[21], game_state[22], game_state[23], game_state[24]),

            # vertical
            (game_state[0], game_state[5], game_state[10], game_state[15]),
            (game_state[5], game_state[10], game_state[15], game_state[20]),
            (game_state[1], game_state[6], game_state[11], game_state[16]),
            (game_state[6], game_state[11], game_state[16], game_state[21]),
            (game_state[2], game_state[7], game_state[12], game_state[17]),
            (game_state[7], game_state[12], game_state[17], game_state[22]),
            (game_state[3], game_state[8], game_state[13], game_state[18]),
            (game_state[8], game_state[13], game_state[18], game_state[23]),
            (game_state[4], game_state[9], game_state[14], game_state[19]),
            (game_state[9], game_state[14], game_state[19], game_state[24]),

            # diagonal
            (game_state[0], game_state[6], game_state[12], game_state[18]),
            (game_state[6], game_state[12], game_state[18], game_state[24]),
            (game_state[4], game_state[8], game_state[12], game_state[16]),
            (game_state[8], game_state[12], game_state[16], game_state[20]),
            (game_state[1], game_state[7], game_state[13], game_state[19]),
            (game_state[5], game_state[11], game_state[17], game_state[23]),
            (game_state[3], game_state[7], game_state[11], game_state[15]),
            (game_state[9], game_state[13], game_state[17], game_state[21]),

        ]

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


    output = int()
    for check in condition:
        if check.count(True) == 3:
            Ch_Idx = condition.index(check)
            idx = findIndex(check)
            output = Mycondition[Ch_Idx][idx]
        else:
            emptyStates = []
            for i in range(0,25):     
                if game_state[i] is None:
                    emptyStates.append(i)               
            output = random.choice(emptyStates)
    
    return output   





    # row1 = [0,1,2,3,4]
    # row2 = [5,6,7,8,9]
    # row3 = [10,11,12,13,14]
    # row4 =[15,16,17,18,19]  
    # row5 = [20, 21, 22, 23, 24]
    # col1 = [0, 5, 10, 15, 20]
    # col2 = [1, 6, 11, 16, 21]
    # col3 = [2, 7, 12, 17, 22]
    # col4 = [3, 8, 13, 18, 23]
    # col5 = [4, 9, 14, 19, 24]
    # dia1 = [1, 7, 13, 19]
    # dia2 = [0, 6, 12, 18, 24]
    # dia3 = [5, 11, 17, 23]
    # dia4 = [3,7, 11, 15]
    # dia5 = [4, 8, 12 ,16, 20]
    # dia6 = [9, 13, 17, 21]
    # # rows = [row1, row2, row3, row4, row5]
    # # cols = [col1, col2, col3, col4, col5]
    # # diagonals = [dia1, dia2, dia3, dia4, dia5, dia6]

    # all = [row1, row2, row3, row4, row5, col1, col2, col3, col4, col5,dia1, dia2, dia3, dia4, dia5, dia6]
    # res = int()

    # for dim in all:
    #     ls = []
    #     for idx in dim:
    #         ls.append(game_state[idx])
    #         if ls.count(True) == 3:
    #             res = findIndex(ls)
    #             break
    #         else:
    #             emptyStates = []
    #             for i in range(0,25):     
    #                 if game_state[i] is None:
    #                     emptyStates.append(i)               
    #             res = random.choice(emptyStates)
    # return res







     