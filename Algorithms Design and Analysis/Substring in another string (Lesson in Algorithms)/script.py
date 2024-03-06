def solution(s1, s2):
    for i in range(len(s1)-len(s2)+1):
        if s1[i:i+len(s2)] == s2:
            return "Match Found"
                
s1 = 'opengenus'

# Test case: no match found
s2 = '123'
print(s2, solution(s1, s2))

# Test case: single character
s2 = 'p'
print(s2, solution(s1, s2))

# Test case: match substring at the beginning (at index 0)
s2 = 'ope'
print(s2, solution(s1, s2))

# Test case: match substring somewhere in the middle
s2 = 'eng'
print(s2, solution(s1, s2))

# Test case: match substring at the end
s2 = 'nus'
print(s2, solution(s1, s2))

# Test case: match both the strings completely
s2 = 'opengenus'
print(s2, solution(s1, s2))