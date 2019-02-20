""" 
  This is a test function to test fibonnaci program 
"""
from series_module import fibonacci
from series_module import lucas

def test_fib_series():
  """
    This is a test function to test fibonnaci program 
      
    Attributes: 
      n: A numeric value  
  """
  n = 6
  actual = fibonacci(n)
  expected = 8
  assert expected == actual

def test_lucas_series():
  """
    This is a test function to test fibonnaci program 
      
  Attributes: 
      n: A numeric value  
  """
  n = 5
  actual = lucas(n)
  expected = 7
  assert expected == actual

