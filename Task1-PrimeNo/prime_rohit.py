def prime(a):
    numb=[]
    prime=[]
    sum=0
    print('Please enter the {} Number.'.format(a))
    for i in range(0,a):
        #print('Enter {} number'.format(i+1))
        x=int(input(' '))
        numb.append(x)
    for j in range(0,len(numb)):
        
        if numb[j]%2==0:
            prime.append(numb[j])
            sum=sum+numb[j]
    print("Prime Number is :",prime)
    print("Sum of the Prime number is:",sum)

num=int(input("Please Lets us know,how Many number You want?"))
prime(num)
