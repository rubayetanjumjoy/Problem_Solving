def isHappy(n):
    visited = set()

    while n != 1:
        if n in visited:
            return False
        visited.add(n)

        digits = [int(d)*int(d) for d in str(n)]
        n = sum(digits)
        print(n)
        

    return True
print(isHappy(100))
