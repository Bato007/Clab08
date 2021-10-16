import random

primesOverTen = [
            [1000000007, 1000000009, 1000000021, 1000000033, 1000000087, 1000000093, 1000000097,
             1000000103, 1000000123, 1000000181, 1000000207, 1000000223, 1000000241, 1000000271,
             1000000289, 1000000297, 1000000321, 1000000349, 1000000363, 1000000403, 1000000409],
            [100000035227, 100000034999, 100000034821, 100000034597, 100000034297, 100000034059,
             100000033877,100000033531, 100000033279, 100000032947, 100000032677, 100000032481,
             100000031897, 100000031713,100000031377, 100000031137, 100000035203, 100000034977,
             100000034581, 100000034023, 100000033849]
             ]

def primeGenerator(n, k):
  primes = []
  flag = 0
  lowerLimit = 10**(n-1)
  upperLimit = 10**(n)-1

  while len(primes) < k:
    numb = random.randint(lowerLimit, upperLimit)
    if numb == 2:
      primes.append(numb)
    if numb % 2 == 0:
      pass
    for i in range(k):
      a = random.randint(1, numb-1)
      if pow(a, numb-1) % numb != 1:
        pass
      else:
        flag += 1        

    if flag == k:
      primes.append(numb)
    flag = 0
  
  return primes

def power(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res

def main():
    prime = ''
    a = '\n-----------------------------'
    a += 'BIENVENIDO SUJETO!'
    a += '-----------------------------\n'
    a += '1) 6 DIGITOS\n'
    a += '2) 10 DIGITOS\n'
    a += '3) 12 DIGITOS\n'
    while True:
        print(a)
        option = input('ESCOJA EL TAMAÑO DEL NUMERO PRIMO: ')
        if option == '1':
            prime = primeGenerator(6, 1)[0]
            break
        elif option == '2':
            prime = random.choice(primesOverTen[0])
            break
        elif option == '3':
            prime = random.choice(primesOverTen[1])
            break
        else:
            print('\n----ERROR!!----\n')
        
    g = random.randint(2, prime-1)
    a = random.randint(2, prime-1)
    b = random.randint(2, prime-1)

    
    alice = power(g, a, prime)
    bob = power(g, b, prime)
    aliceBob = power(bob, a, prime)
    bobAlice = power(alice, b, prime)
    print('g: ',g,'\na: ',a,'\nb: ',b,'\nalice: ',alice,'\nbob: ',bob,'\naliceBob: ',aliceBob,'\nbobAlice: ',bobAlice)

    if aliceBob == bobAlice:
        print('La clave coincide!!')
    else:
        print('No coinciden las claves')
    


main()