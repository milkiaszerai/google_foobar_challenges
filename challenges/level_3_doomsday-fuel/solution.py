from fractions import Fraction

# Replace trials by probabilties of occurrences
def replace_probability(m):        
    for row in range(len(m)):
        total = 0
        for item in range(len(m[row])):
            total += m[row][item]
        if total != 0:
            for item in range(len(m[row])):
                m[row][item] /= float(total)
    return m

# R - non-terminal -> terminal
# Q - non-terminal -> non-terminal
def RQ(m, terminal_state, non_terminal_state):
    R = []
    Q = []
    for i in non_terminal_state:
        temp_t = []
        temp_n = []
        for j in terminal_state:
            temp_t.append(m[i][j])
        for j in non_terminal_state:
            temp_n.append(m[i][j])
        R.append(temp_t)
        Q.append(temp_n)
    return R, Q

# Get Identity Matrix - Q
def subtract_Q_from_identity(Q):
    """
    If Q = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
    I - Q:
    [[1,0,0]            [[0,-2,-3]
     [0,1,0]   - Q =     [-4,-4,-6]
     [0,0,1]]            [-7,-8,-8]]
    """

    n = len(Q)
    for row in range(len(Q)):
        for item in range(len(Q[row])):
            if row == item:
                Q[row][item] = 1 - Q[row][item]
            else:
                Q[row][item] = -Q[row][item]
    return Q

# Get minor matrix
def get_minor_matrix(Q,i,j):
    """
    Q = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
    Minor matrix corresponding to 0,0 is
    [
        [5,6],
        [8,9],
    ]
    """

    minor_matrix = []
    for row in Q[:i] + Q[i+1:]:
        temp = []
        for item in row[:j] + row[j+1:]:
            temp.append(item)
        minor_matrix.append(temp)
    return minor_matrix

# Get determinant of a square matrix
def get_determinant(Q):
    if len(Q) == 1:
        return Q[0][0]
    if len(Q) == 2:
        return Q[0][0]*Q[1][1] - Q[0][1]*Q[1][0]
    
    determinant = 0
    for first_row_item in range(len(Q[0])):
        minor_matrix = get_minor_matrix(Q, 0, first_row_item)
        determinant += (((-1)**first_row_item)*Q[0][first_row_item] * get_determinant(minor_matrix))

    return determinant

# Get transpose of a square matrix
def get_transpose_square_matrix(Q):
    for i in range(len(Q)):
        for j in range(i, len(Q), 1):
            Q[i][j], Q[j][i] = Q[j][i], Q[i][j]
    return Q


def get_inverse(Q):
    Q1 = []
    for row in range(len(Q)):
        temp = []
        for column in range(len(Q[row])):
            minor_matrix = get_minor_matrix(Q, row, column)
            determinant = get_determinant(minor_matrix)
            temp.append(((-1)**(row+column))*determinant)
        Q1.append(temp)
    main_determinant = get_determinant(Q)
    Q1 = get_transpose_square_matrix(Q1)
    for i in range(len(Q)):
        for j in range(len(Q[i])):
            Q1[i][j] /= float(main_determinant)
    return Q1

def multiply_matrix(A, B):
    result = []
    dimension = len(A)
    for row in range(len(A)):
        temp = []
        for column in range(len(B[0])):
            product = 0
            for selector in range(dimension):
                product += (A[row][selector]*B[selector][column])
            temp.append(product)
        result.append(temp)
    return result

def gcd(a ,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)   

def sanitize(M):
    needed = M[0]
    to_fraction = [Fraction(i).limit_denominator() for i in needed]
    lcm = 1
    for i in to_fraction:
        if i.denominator != 1:
            lcm = i.denominator
    for i in to_fraction:
        if i.denominator != 1:
            lcm = lcm*i.denominator/gcd(lcm, i.denominator)
    to_fraction = [(i*lcm).numerator for i in to_fraction]
    to_fraction.append(lcm)
    return to_fraction

def solution(m):
    n = len(m)
    if n==1:
        if len(m[0]) == 1 and m[0][0] == 0:
            return [1, 1]
    terminal_state = []
    non_terminal_state = []

    # Get terminal and non-terminal states
    for row in range(len(m)):
        count = 0
        for item in range(len(m[row])):
            if m[row][item] == 0:
                count += 1
        if count == n:
            terminal_state.append(row)
        else:
            non_terminal_state.append(row)
    # Replace trials by probabilties
    probabilities = replace_probability(m)
    # Get R and Q matrix
    R, Q = RQ(probabilities, terminal_state, non_terminal_state)
    IQ = subtract_Q_from_identity(Q)
    # Get Fundamental Matrix (F)
    IQ1 = get_inverse(IQ)
    product_IQ1_R = multiply_matrix(IQ1, R)
    return sanitize(product_IQ1_R)

# Case where state 0 itself is a terminal state
assert(solution(
    [
        [0],
    ]
)) == [1, 1]

assert(solution(
    [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)) == [7, 6, 8, 21]

assert(solution(
    [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
)) == [0, 3, 2, 9, 14]
