def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        sentence = s[0:step]
        count = 1

        for j in range(step,len(s),step):
            if sentence == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + sentence if count >= 2 else sentence
                sentence = s[j:j+step]
                count = 1
        compressed += str(count) + sentence if count>=2 else sentence 
        answer = min(answer, len(compressed))


    return answer

print(solution("aabbaccc"))