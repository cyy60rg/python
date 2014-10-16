#!/usr/bin/python
def prime(n):
  f=0
  m=n/2
  #p=(int)m
  print str(m) +" "+ str(int(m))
  for i in range(1,int(m+1)):
    print str(i) + "\n"
  if(n%i==0):
   f+=1

 if f == 1 :
  return 1;
 else:
  return 0;
def main():
 n=input("Enter the number\n")
 f=prime(n)
 if f==1 :
  print "No: "+ str(n) +" is prime "+ str(f) + "\n"
 else:
  print "No: "+ str(n) +" is not prime. "+ str(f) +" \n"
main()
~                                                                                   
~               
