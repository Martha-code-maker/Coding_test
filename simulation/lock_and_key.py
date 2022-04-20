def rotate_matrix_90_degrees(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = a[i][j]
            
    return result

def check_sum(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    new_lock = [[0]* (n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate_matrix_90_degrees(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check_sum(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False


