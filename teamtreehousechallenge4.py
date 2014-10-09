__author__ = 'david.savoir'

	def sillycase (x):
  first = round(len(x)/2)
5	  y = list(x)
6	  first_half = y[:(first)]
7	  last_half = y[(first):]
8	  upperlasthalf = [x.upper() for x in last_half]
9	  first_half.extend(upperlasthalf)
10	  print (first_half)
11	  return first_half

sillycase("treehouse")


