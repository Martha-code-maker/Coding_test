def solution(name):
    answer = 0
    
    alpha = []
    for word in name:
        if ord(word) - ord('A') > 13:
            add_word_index = 26 - (ord(word) - ord('A'))
            alpha.append(add_word_index)
        else:  
            alpha.append(ord(word) - ord('A'))

    print(alpha)    
    count_choose_word = sum(alpha)
    answer += count_choose_word
    
    cnt = 0
    for word in name:
        if "A" in word:
            cnt += 1
    count_move = len(name) -1 -cnt
    
    answer += count_move
    
        
    return answer

solution("JEROEN")