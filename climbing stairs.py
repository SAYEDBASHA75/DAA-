'''You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

def steps(n):
    if n==1 or n==0:
        return 1
    first=1
    second=1
    for i in range(2, n+1):
        current=first+second
        first=second
        second=current
    return second
print(steps(4))
print(steps(3))

Output:
5
3
