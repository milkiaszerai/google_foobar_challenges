def solution(n):
    ''' 
    Write a function called solution(n) which takes a positive integer as a string and 
    returns the minimum number of operations needed to transform the number of pellets to 1. 
    
    Args: 
        n (str): string of postive integer
    Returns:
        res (int): minimum number of operations needed to transform the number of pellets to 1

    Examples:
        solution(4) returns 2: 4 -> 2 -> 1
        solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
    '''
    n = int(n)
    res = 0

    while(n!=1):
        if(n%2==0):
            n=n/2
        elif((n==3) or ((n+1)&n) > ((n-1)&(n-2))):
            n-=1
        else:
            n+=1
        res+=1
    return res
