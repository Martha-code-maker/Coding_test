def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = 0
    for i in reserve[:]: #list 제거시 [:] 중요!!
        if i in lost[:]:
            lost.remove(i)
            reserve.remove(i)
    
    for p in reserve:   
        answer += 1
        n -= 1
        if p-1 in lost:
            answer += 1
            lost.remove(p-1)
            n-=1
        elif p+1 in lost:
            answer += 1
            lost.remove(p+1)
            n-=1
            
    n-= len(lost)
    answer += n

    
    return answer