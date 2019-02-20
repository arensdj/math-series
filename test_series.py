""" 
  This is a test program for the series_module program 
"""
from series_module import fibonacci
from series_module import lucas
from series_module import sum_series

def test_fib_series():
  """
    This is a test function to test fibonnaci function 
      
    Attributes: 
      n: A numeric value  
  """
  n = 6
  actual = fibonacci(n)
  expected = 8
  assert expected == actual


def test_lucas_series():
  """
    This is a test function to test lucas function 
      
  Attributes: 
      n: A numeric value  
  """
  n = 5
  actual = lucas(n)
  expected = 7
  assert expected == actual


def test_sum_series_fib():
  """
    This is a test function to test sum_series function 
      
  Attributes: 
      n: A numeric value  
  """
  n = 6
  actual = sum_series(n)
  expected = 8
  assert expected == actual  


def test_sum_series_lucas():
  """
    This is a test function to test sum_series function 
      
  Attributes: 
      n: A numeric value  
  """
  n = 5
  arg1 = 2
  arg2 = 1
  actual = sum_series(n, arg1, arg2)
  expected = 7
  assert expected == actual  
