""" 
  This is a test function to test fibonnaci program 
"""
from series_module import fibonacci

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

