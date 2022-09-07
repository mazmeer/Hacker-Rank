n,m = input().split()
n = int(n)
m = int(m)

#printing first half
for i in range(n//2):
    t = int((2*i)+1)
    print(('.|.'*t).center(m, '-'))
#printing middle line
print('WELCOME'.center(m,'-'))
#printing last half
'''for i in reversed(range(n//2)):
    t = int((2*i)+1)
    print(('.|.'*t).center(m, '-'))'''