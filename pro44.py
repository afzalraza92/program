"""Sum of 2 elements of array whose sum is equal to a given value x.
If there exist 2 pair such that their sum is equal to the value x print yes else print no."""
x = [5,3,1,9,2,6,10,18,4,3]
y = 10
sum=0
low = 0
high = len(x)-1
x.sort()
print(x)
for i in range(len(x)):
    sum = x[low] + x[high]
    if(sum == y):
        print("yes")
        break
    elif(sum>y):
        high=high-1
    else:
        low=low+1

if(low>=high):
    print("no")


