def add(x, y):
      return(x + y)

def factorial(x):
      s = 1
      for i in range(x):
            s = s * (i+1)
      return(s)
      
def sin(x, N):
      s = 0
      for n in range(N+1):
            s = s + (((-1)**n) * x**(2*n+1)) / factorial(2*n + 1)
      return(s)
      
def divide(x, y):
      return(x / y)
      
def power(x, y):
      return(x**y)
      
def dubble_power(x, y):
      b = x
      for i in range(y-1):
            b = power(x,b)
      return(b)