# math-series
# This program consists of three functions which produce numbers from the 
# fibonacci series and the lucas series.  The function named sum_series can 
# compute either series depending on the arguments to the function.  

## Challenge
# Code a function that can compute either fibonacci and lucas series which is
# determined by the arguments to the function.

## Approach & Efficiency
# The approach I took was to code the fibonacci series and lucas in separate
# functions.  Both are have similar algorithm but differs in the first two 
# values in the series in the array.  Invoking the sum_series function with no
# optional arguments will produce fibonacci numbers.  Invoking the sum_series
# with optional arguments 2 and 1 will produce lucas numbers.  Once this is
# determined, the first two values for the series can be produced.  The 
# remaining numbers in both series have the same algorithm.

