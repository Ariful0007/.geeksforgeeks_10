
for _ in range(int(input())):
    n= int(input())
    sum=0
    for i in range(1,n+1):
        if n % i==0:
           if i%2==0:
               sum=sum+i

    print(sum)
    
if __name__ == '__main__':
    pass

