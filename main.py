def minWindow(s, t):
    if not containsAll(s, t):
        return ''
    
    answer = s
    for length in range(len(s)-1, 0, -1):
        for subLength in range(len(s) - length + 1):
            candidate = s[subLength:length+subLength:]
            if containsAll(candidate, t):
                answer = candidate

    return answer

def containsAll(a, b): #returns true if a contains all the letters in b
    temp1 = a
    for letter in b:
        index = temp1.find(letter)
        if index < 0:
            return False
        temp1 = temp1[:index] + temp1[index+1:]
    return True

# Example 1:
# Input: 
s = "ADOBECODEBANC"
t = "ABC"
print('"' + minWindow(s, t) + '"')
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: 
s = "a"
t = "a"
print('"' + minWindow(s, t) + '"')
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: 
s = "a"
t = "aa"
print('"' + minWindow(s, t) + '"')
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
