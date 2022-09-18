n,m = input().split()
n = int(n)
m = int(m)


for i in range(n//2):
    t = int((2*i)+1)
    print(('.|.'*t).center(m, '-'))

print('WELCOME'.center(m,'-'))

for i in reversed(range(n//2)):
    t = int((2*i)+1)
    print(('.|.'*t).center(m, '-'))