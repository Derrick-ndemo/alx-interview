"""
Function that returns a list of lists 
of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers 
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    result = []

    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            prev_row = result[i-1]
            new_row = [1]
            
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j-1] + prev_row[j])
            
            new_row.append(1)
            result.append(new_row)

    return result
