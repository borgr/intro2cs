def get_alignment_score(DNA1, DNA2, match = 1, mismatch = -1, gap = -2):

    score = 0

    while len(DNA1) > len(DNA2):
##        DNA2.append('-')
        DNA2 = DNA2 + '-'
    while len(DNA1) < len(DNA2):
##        DNA1.append('-')
        DNA1 = DNA1 + '-'
        
    for index in range(len(DNA1)):
        if DNA1[index] == DNA2[index]:
            score += match
        elif DNA1[index] != DNA2[index] \
             and DNA1[index] != '-' and DNA2[index] != '-':
            score += mismatch
        else:
            score += gap

    return score
            

DNA1 = 'AT'
DNA2 = 'CA'

def get_best_alignment_score(DNA1, DNA2, match = 1, mismatch = -1, gap = -2):

##    DNA1 = list(DNA1)
##    DNA2 = list(DNA2)
    print('DNA1 is:', DNA1)
    print('DNA2 is:', DNA2)
    print()

##    # Short calculations for specific conditions:
##    if gap >= match and gap >= mismatch:
##        print('specific condition 1')
##        for i in range(len(DNA2)):
##            DNA1.insert(0, '-')
##        for i in range(len(DNA1)):
##            DNA2.append('-')
##
##        print('DNA1 is:', DNA1)
##        print('DNA2 is:', DNA2)   
##        return DNA1, DNA2
##
##    if match == mismatch == gap > 0:
##        print('specific condition 2')
##        for i in range(len(DNA2)):
##            DNA1.insert(0, '-')
##        for i in range(len(DNA1)):
##            DNA2.append('-')
##
##        print('DNA1 is:', DNA1)
##        print('DNA2 is:', DNA2)
##        return DNA1, DNA2
##
##    if match == mismatch == gap <= 0:
##        print('specific condition 3')
##        while len(DNA1) > len(DNA2):
##            DNA2.append('-')
##        while len(DNA1) < len(DNA2):
##            DNA1.append('-')
##
##        print('DNA1 is:', DNA1)
##        print('DNA2 is:', DNA2)
##        return DNA1, DNA2


    def compare(DNA1, DNA2):

        if len(DNA1) < 1 or len(DNA1) < 1:#why dna 1 twice?
            print('basecase')
            score = get_alignment_score(DNA1, DNA2)
            print('score is:', score)
            print('DNA1 is:', DNA1)
            print('DNA2 is:', DNA2)
            print()
            return score, DNA1, DNA2

        # Case 1
        print('Case 1')
        DNA1_head = DNA1[0]
        DNA2_head = DNA2[0]
        print('DNA1_head is:', DNA1_head)
        print('DNA2_head is:', DNA2_head)

        compare1 = compare(DNA1[1:], DNA2[1:])
        print('compare1 is:', compare1)

        DNA1_1 = DNA1_head + compare1[1]
        DNA2_1 = DNA2_head + compare1[2]
        print('DNA1_1 is:', DNA1_1)
        print('DNA2_1 is:', DNA2_1)

        if DNA1[0] == DNA2[0]:
            value = match
        else:
            value = mismatch

        score1 = compare1[0] + value
        

        # Case 2
        print('Case 2')
        print('DNA1 is:', DNA1)
        print('DNA2 is:', DNA2)
        DNA1_case2 = DNA1 + '-' #it will look like "ag-" [0]= a not -

        DNA1_head = DNA1_case2[0]
        DNA2_head = DNA2[0]
        print('DNA1_head is:', DNA1_head)
        print('DNA2_head is:', DNA2_head)
#DNA1_case2 you never use it... you probably wanted it on the next compare
        compare2 = compare(DNA1[1:], DNA2[1:])#from agc and atg > gc and tg? what about gaps >agc tg?

        DNA1_2 = DNA1_head + compare1[1]
        DNA2_2 = DNA2_head + compare1[2]

        score2 = compare2[0] + gap


        # Case 3
        print('Case 3')
        DNA2_case3 = DNA2 + '-'#it is just the same, note that you have replicated code, might make a function for that
        #maybe it will add - to the first strand and return whateveryou want
        #and then send once the 

        DNA1_head = DNA1[0]
        DNA2_head = DNA2_case3[0]
        print('DNA1_head is:', DNA1_head)
        print('DNA2_head is:', DNA2_head)

        compare3 = compare(DNA1[1:], DNA2[1:])

        DNA3_1 = DNA1_head + compare1[1]
        DNA3_2 = DNA2_head + compare1[2]

        score3 = compare3[0] + gap


        if score1 == max(score1, score2, score3):#does not matter much, but maxis a function why callit twice instead of using a variable
            return score1, DNA1_1, DNA2_1
        elif score2 == max(score1, score2, score3):
            return score2, DNA1_2, DNA2_2
        else:
            return score3, DNA3_1, DNA3_2
    


    results = compare(DNA1, DNA2)

    score = results[0]
    DNA1 = results[1]
    DNA2 = results[2]

    return score, DNA1, DNA2


