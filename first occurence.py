'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.'''
haystack="sadbutsad"
needle="sad"
for i in range(len(haystack)- len(needle)+1):
    if haystack[i:i + len(needle)]==needle:
        print(i)
        break
    else:
        print(-1)
        break

Output:0
