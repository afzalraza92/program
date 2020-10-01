x = "A clever fox jumps over the lazy       dog"
print(x)
c=0
for i in range(0,len(x)):
    if(x[i]=='A' or x[i]=='a'):
        x = x.replace(x[i],'1')
        c=c+1

    if(x[i]=='E' or x[i]=='e'):
        x = x.replace(x[i],'2')
        c=c+1

    if(x[i]=='I' or x[i]=='i'):
        x = x.replace(x[i],'3')
        c=c+1

    if(x[i]=='O' or x[i]=='o'):
        x = x.replace(x[i],'4')
        c=c+1

    if(x[i]=='U' or x[i]=='u'):
        x = x.replace(x[i],'5')
        c=c+1

print(x)
print(c*2)