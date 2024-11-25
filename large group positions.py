'''In a string S of lowercase letters, these letters form consecutive groups of the same character. For example, a string like s = "abbxxxxzyy" has the
groups "a", "bb", "xxxx", "z", and "yy". A group is identified by an interval [start, end], where start and end denote the start and end indices 
(inclusive) of the group. In the above example, "xxxx" has the interval [3,6]. A group is considered large if it has 3 or more characters. Return the 
intervals of every large group sorted in increasing order by start index.'''

def largeGroupPositions(s):
    intervals=[]
    start=0
    for i in range(1,len(s)):
        if s[i]!=s[start]:
            if i-start>=3:
                intervals.append([start,i-1])
            start=i
    if len(s)-start>=3:
        intervals.append([start,len(s)-1])
    return intervals
print(largeGroupPositions("abbxxxxzzy"))
print(largeGroupPositions("abc"))

Output: [[3,6]]
[]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
