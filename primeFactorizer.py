
#to find factor of any number
def factorsOf(num):
    factors=[]
    for i in range(num):
        if num%(i+1)==0:
            factors.append(i+1)      
    return factors
 
#returns true if the given number is prime   
def isPrime(num):
    f=factorsOf(num)
    if len(f)==2 or num==0:
        if num==1 or num==0:
            
            return False
        else:
            return True
 
#returns prime factors of given number                       
def primeFactorsOf(num):                    
            primeFacs=[]  
            fac=factorsOf(num)
            for i in fac:
                if isPrime(i)==True:
                    primeFacs.append(i) 
            return primeFacs        

def repeatCountOfPrimeFacsOf(num):
            p=primeFactorsOf(num)
            repeatCountOfPrimeFacs=[]
            count=0
            m=num
            res=[]
            for i in p:
                while m%i==0:
                    
                    
                    m=m/i
                    count=count+1
                repeatCountOfPrimeFacs.append(count)   
                count=0    
            for g in range(len(p)):
                    res.append(str(p[g])+"^"+
                    str(repeatCountOfPrimeFacs[g]))
                    
            return res       
