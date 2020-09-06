import calculator
import pytest
import math

def test_add_exercise_1():
      assert calculator.add(1, 2) == 3
      
def test_add_exercise_2():
      test = calculator.add(0.1, 0.2)
      Cansw = 0.3
      tol = 10**(-5)
      assert  abs(test - Cansw) < tol*max(abs(test),abs(Cansw))

def test_add_exercise_3():
      assert(calculator.add("Hello ", "World")) == "Hello World"


def test_factorial_exercise_4():
      assert(calculator.factorial(25)) == math.factorial(25)
      
def test_sin_exercise_4():   
      test = calculator.sin(30,100)
      Cansw = math.sin(30)
      tol = 10**(-3)
      assert abs(test - Cansw) < tol*max(abs(test),abs(Cansw))
      
def test_divide_exercise_4():
      test = calculator.divide(3,2)
      Cansw = 1.5
      tol = 10**(-6)
      assert abs(test - Cansw) < tol*max(abs(test),abs(Cansw))
      
def test_power_exercise_4():
      test = calculator.power(3,3)
      Cansw = 27
      tol = 10**(-6)
      assert abs(test - Cansw) < tol*max(abs(test),abs(Cansw))
      
def test_dubble_power_exercise_4():
      test = calculator.dubble_power(3,3)
      Cansw = 7625597484987
      tol = 10**(-6)
      assert abs(test - Cansw) < tol*max(abs(test),abs(Cansw))

def test_add_exercise_5():
      with pytest.raises(TypeError):
            calculator.add("Hello",2)

def test_divide_exercise_5():
      with pytest.raises(ZeroDivisionError):
            calculator.divide(2,0)

@pytest.mark.parametrize(
            "x, y", [[(3,5),8],[(0.3,2),2.3],[(5.21,-7.3),-2.09],[("Hello ", "World"),"Hello World"]]
            )
def test_add_exercise_6(x, y):
      assert calculator.add(x[0],x[1]) == y
      
@pytest.mark.parametrize(
            "x", [[2],[-1],[0]]
            )
def test_factorial_6(x):
      assert calculator.factorial(x[0])
            
@pytest.mark.parametrize(
            "x, y", [[3,math.sin(3)],[-2,math.sin(-2)],[0.05,math.sin(0.05)],[0,math.sin(0)]]
            )
def test_sin_exercise_6(x, y):
      N = 10^3
      test = calculator.sin(x,N)
      tol = 10**(-4)
      assert abs(test - y) <= tol*max(abs(test),abs(y))
      
@pytest.mark.parametrize(
            "x, y", [[(10,5),2],[(0.3,2),0.15],[(5,0.5),10],[(-1,2),-0.5],[(4,-2),-2]]
            )
def test_divide_6(x, y):
      test = calculator.divide(x[0],x[1])
      tol = 10**(-6)
      assert abs(test - y) <= tol*max(abs(test),abs(y))
      
@pytest.mark.parametrize(
            "x, y", [[(2,5),32],[(0.3,2),0.09],[(4,1.5),8],[(-5,-2),0.04]]
            )
def test_power_6(x,y):
      test = calculator.power(x[0],x[1])
      tol = 10**(-5)
      assert abs(test - y) <= tol*max(abs(test),abs(y))
      
@pytest.mark.parametrize(
            "x, y", [[(1,10),1],[(2,4),65536],[(0.5,3),0.612547326536],[(-3,2),-0.03703703703]]
            )
def test_dubble_power_6(x,y):
      test = calculator.dubble_power(x[0],x[1])
      tol = 10**(-5)
      assert abs(test - y) <= tol*max(abs(test),abs(y))