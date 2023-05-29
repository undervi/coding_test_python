def solution(name, yearning, photo):
    score_map = {}
    for i in range(len(name)):
        score_map[name[i]] = yearning[i]
    
    answer = []
    for i in range(len(photo)):
        score = 0
        for x in photo[i]:
            if x in score_map:
                score += score_map[x]
        answer.append(score)
        
    return answer