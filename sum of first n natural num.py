def recursive_sum(n):
    if (n<=1):
        return 1

    else:
        return n+recursive_sum(n-1)
num=-7

print(recursive_sum(num))
if num<0:
    print("postive only")