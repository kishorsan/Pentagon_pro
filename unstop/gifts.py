def find_youngest_member(n, m, gifts):
    """
    Write your logic here.
    Parameters:
        n (int): Number of family members
        m (int): Number of gifts exchanged
        gifts (list of tuples): List of tuples where each tuple contains two integers (a_i, b_i)
    Returns:
        int: The number that represents the youngest member of the family or -1 if no such member is found
    """
    lst = [0]*(n+1)
    for i in range(m):
        lst[gifts[i][1]] += 1
    ele = 0
    ind = -1
    if m == 0:
        return 1
    print(lst)
    for i in range(n+1):
        if ele < lst[i]:
            ind = i
            ele = lst[i]
    return ind

def main():
    data = list(map(int, input().split()))
    
    n = int(data[0])  # Number of family members
    m = int(data[1])  # Number of gifts exchanged
    
    gifts = []
    index = 2
    for _ in range(m):
        a_i = data[index]
        b_i = data[index + 1]
        gifts.append((a_i, b_i))
        index += 2
    
    # Call user logic function and print the output
    result = find_youngest_member(n, m, gifts)
    print(result)

if __name__ == "__main__":
    main()
