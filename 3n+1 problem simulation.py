# 3n+1 simulation
n = int(input("Enter an integer (negative or positive):" ))
max_n = 0
count = 0
if n > 0:
		while n != 1:
        max_n = max(max_n, n)  
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count = count + 1
    print('your calculation has run for', count, 'times before going into a loop, the largest n is', max_n)
else:
    while n not in [-1, -5, -17]:
        max_n = min(max_n, n)  
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count = count + 1
    print('your calculation has run for', count, 'times before going into a loop, and the smallest n is', max_n)
