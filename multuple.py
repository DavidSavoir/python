seq=((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))
	#seqresult=[]
	#print(seq[0][0])
	#for a, b, c, d, e in seq.iteritems():
	#	print((seq[0][0]*seq[0][1]) ,"=", seq[0][0]," x ",seq[0][1])

	#for i in seq.iteritems():	
	#	print((seq[i][i]*seq[0][i+1]), "=", seq[i][i]," x ",seq[i][i+1])
elements = "{0:>2} x {1:>2}"
	#for i in seq:
	#	seqresult.append[i] = seq[i]*seq[i]
fmt = "{0:>6}"
for (a, b) in seq:
	#c= a*b
	#for i in (a*b):
	print("{0:>4}".format(a*b), "{0:>0}".format("="), elements.format(a,b))

#for (a, b) in seq:
#    print(a*b,"=",a,"x",b)



""">>> fmt = "{0:>6} = {0:>#16b} = {0:#06x}"
>>> for i in 1, 23, 456, 7890:
...   print(fmt.format(i))
...
     1 =              0b1 = 0x0001
    23 =          0b10111 = 0x0017
   456 =      0b111001000 = 0x01c8
  7890 =  0b1111011010010 = 0x1ed2"""