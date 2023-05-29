def solution(players, callings):
    ranks = {}
    
    for i, player in enumerate(players):
        ranks[player] = i
    
    for x in callings:
        i = ranks[x]
        ranks[x], ranks[players[i-1]] = i-1, i
        players[i], players[i-1] = players[i-1], players[i]
        
                
    return players