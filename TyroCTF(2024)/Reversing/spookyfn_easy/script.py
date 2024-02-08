def spooky_fn(x):
    if x <= 1:
        return 0  
    return 1 + spooky_fn(x >> 42)

n = int(input())

k = spooky_fn(n)

if k is not spooky_fn(n):
    print(open("flag.txt").read().strip())
else:
    print("Boo!")

