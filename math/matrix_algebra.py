# Matrix Algebra

import numpy as np

A = np.matrix('1,2,3;2,7,4')
B = np.matrix('1,-1;0,1')
C = np.matrix('5, -1;9,1;6,0')
D = np.matrix('3,-2,-1;1,2,3')
u = np.matrix('6,2,-3,5')
v = np.matrix('3,5,-1,4')
w = np.matrix('1;8;0;5')


print (A.shape)
print (B.shape)
print (C.shape)
print (D.shape)
print (u.shape)
print (w.shape)

#(2, 3)
#(2, 2)
#(3, 2)
#(2, 3)
#(1, 4)
#(4, 1)

#2.1
print "2.1) %r" %(u+v)
#2.1) matrix([[ 9,  7, -4,  9]])

#2.2
print "2.2) %r" %(u-v)
#2.2) matrix([[ 3, -3, -2,  1]])

#2.3
print "2.3) %r" %(6*u)
#2.3) matrix([[ 36,  12, -18,  30]])

#2.4
udotv= np.multiply(u,v)
print "2.4) %r" %(np.sum(udotv))
#2.4) 51

#2.5
from numpy import linalg as LA
print "2.5) %r" %(LA.norm(u))
#2.5) 8.6023252670426267

#3.1
print "3.1) %r" %(A+C)
#not defined

#3.2
print "3.2) %r" %(A-C.transpose())
#3.2) matrix([[-4, -7, -3],
#        [ 3,  6,  4]])

#3.3
print "3.3) %r" %(C.transpose()+3*D)
#3.3) matrix([[14,  3,  3],
#        [ 2,  7,  9]])

#3.4
print "3.4) %r" %(np.dot(B,A))
#3.4) matrix([[-1, -5, -1],
#        [ 2,  7,  4]])

#3.5
print "3.5) %r"  %(np.dot(B,A.transpose()))
#not defined

#3.6
print "3.6) %r" %(np.dot(B,C))
#not defined

#3.7
print "3.7) %r" %(np.dot(C,B))
#3.7) matrix([[ 5, -6],
#        [ 9, -8],
#        [ 6, -6]])

#3.8
print "3.8) %r" %(np.power(B,4))
#3.8) matrix([[1, 1],
#        [0, 1]])

#3.9
print "3.9) %r" %(np.dot(A,A.transpose()))
#3.9) matrix([[14, 28],
#        [28, 69]])

#3.10
print "3.10) %r" %(np.dot(D.transpose(),D))
#3.10) matrix([[10, -4,  0],
#        [-4,  8,  8],
#        [ 0,  8, 10]])
