def solution(s):
    ''' 
    Program that counts how many salutes are exchanged during a typical walk along a hallway which is represented by a string. For example: "--->-><-><-->-" 
    
    Args: 
        s: string of unkown length
    Returns:
        n(int): number of salutes
    '''
    len_ = len(s)
    n = 0 
    
    for ix, i in enumerate(s):
        if i == '-':
            n+=0
        elif i == '>':
            for j in range(len_ - (ix+1)):
                if s[ix+j+1] == '-':
                    n+=0
                elif s[ix+j+1] == '>':
                    n+=0
                elif s[ix+j+1] == '<':
                    n+=1
        elif i == '<':
            for j in range(ix):
                if s[j] == '-':
                    n+=0
                elif s[j] == '<':
                    n+=0
                elif s[j] == '>':
                    n+=1
    print("Number of salutes: {}".format(n))
    return n 


if __name__ == "__main__":
    solution("--->-><-><-->-")
