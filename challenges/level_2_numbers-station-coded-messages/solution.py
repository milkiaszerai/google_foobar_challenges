def solution(l, t):
    ''' 
    A function that verifies if there is at least one consecutive sequence of positive integers within the 
    list l(i.e. a contiguous sub-list) that can be summed up to the given target positive integer t (the key).  
    
    Args:
        l (list) -> a non-empty list of positive integers
        t (int)-> target positive integer 
        
    Returns:
        l_ (list) -> a lexicographically smallest list containing the smallest start and end indexes where a sequence is found 
        array [-1, -1] -> if there is no such sequence
    '''
    
    l_ = [-1, -1]
    
    for idx, i in enumerate(l):
        list = l[idx:len(l)]  # iteratively stores consecutive elements
        sub_list = []
        found = False
        for ix, j in enumerate(list):
            sub_list.append(j)
            if sum(sub_list) == t:
                found = True
                l_[0], l_[1] = idx, (idx + ix)
                print("sub_list:  {} \nindexes: {} ".format(sub_list, l_))
                break
        if found:
            break
    return l_
    
if __name__ == "__main__":
    solution([4, 3, 10, 2, 8],  12)

