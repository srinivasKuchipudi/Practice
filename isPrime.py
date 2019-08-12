def isPrime(n):
    i=2
    if i == n:
        print('Prime')
    while i<n:
        #print(i)
        if n%i == 0:
            print(i)
            print('Not a Prime Number')
            break
        i+=1
        if i == n:
            print('Prime Number')
            s=0
            j=n
            while j >10:
                s+=j%10
                q=j//10
                if q > 10:
                    j=q                    
                else:
                    j=q
                    s+=q
                    if s == 10:
                        print('Sum of digits is 10')
                    else:
                        print('Sum of digits is not 10')