from sympy import isprime
#

#list of primes
primes = [2]

#list of primes from two concatenated primes
primes_concat = {}

#list of remarkable primes
primes_remarkables = []

sum_remarkables = 10e100

#analize tuple
def analize_remarkables(t):
  
  if len(t)==5:
    print(t)
    sum_remarkables = sum(t)
    print(sum_remarkables)

#compare new prime with sum
def stop_prime(n):
  if n > sum_remarkables:
    return True

#search and add new remarkable couple
def is_remarkable_couple(n,m):
  nm = str(n) + str(m)
  mn = str(m) + str(n)
  if isprime(int(nm)) & isprime(int(mn)):
    return True
  else:
    return False

def add_double_remarkable(n):
  for p in primes:
    if is_remarkable_couple(n,p):
      primes_remarkables.append((n,p))

def add_multiple_remarkable(n):
  new_mult_rem = []
  for pr in primes_remarkables:
    #for each number in couple
    rem = True
    new_rem = []
    for i in pr:
      if is_remarkable_couple(n,i):
        new_rem.append(i)
      else:
        rem = False
        break
    if rem:     
      new_rem.append(n)
      tup = tuple(new_rem)
      new_mult_rem.append(tup)
      #analize tuple
      analize_remarkables(tup)
  for mr in new_mult_rem:
    primes_remarkables.append(mr)


n = 3
while True:
  if isprime(n):
    print(n)
    #search in remarkable couples if can create a new one with n
    add_multiple_remarkable(n)    
    #search and add new double remarkable couple
    add_double_remarkable(n)
    #append new prime
    primes.append(n)
    if stop_prime(n):
      print(n)
      break
  n +=1

print(sum_remarkables)


