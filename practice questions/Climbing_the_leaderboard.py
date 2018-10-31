def climbingLeaderboard(scores, alice):
    denseRanking = [1]
    for item in range(1,len(scores)):
        if scores[item] == scores[item-1]:
            denseRanking.append(denseRanking[-1])
        else:
            denseRanking.append(denseRanking[-1]+1)
    result = []
    for aliceIndex in range(len(alice)):
        ascore = alice[aliceIndex]
        for index in range(len(scores)):
            rank = scores[index]
            if rank <= ascore:
                result.append(denseRanking[index])
                print(denseRanking[index])
                break
        if len(result) <= aliceIndex:
            result.append(denseRanking[-1]+1)
            print(denseRanking[-1]+1)


scores = [100,100,50,40,40,20,10]
alice = [5, 25,50,120]
climbingLeaderboard(scores, alice)