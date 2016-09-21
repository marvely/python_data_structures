#import numpy
#import pylab
from numpy import *
############ Numpy's array class is called: ndarray ###############
a = arange(15).reshape(3,5)
print a
print "Shape:", a.shape
print "Dimensions:", a.ndim
print "Data type in the array:", a.dtype.name
print "Size in bytes of each element of the array:", a.itemsize
print "Total num of elements in the array:", a.size
print "Array class:", type(a)

################ Ways to create arrays: #########################
b = array([6, 7, 8])

c = array([2, 3, 4])

d = array([(1.5, 2, 3), (4, 5, 6)]) # transform sequences of sequences into 2-D arrays!!!!!!
print d
e = array([[1, 2], [3, 4]], dtype = complex) #<------- Complex floating-point number??? what is that?????
print e

f = zeros((3, 4)) #<-------- create an array of 3*4 with zero has place-holder in the array
print f

g = ones((2, 3, 4), dtype = int16)
print g

h = empty((2, 3))
print h

################### Create sequences of numbers ###################
i = arange(10, 30, 5) #<-------- the third number is the interval. also can be float.
print i

j = arange(0, 2, 0.5)
print j

k = linspace(0, 2, 9) #<--------- the third number is how many elements we want in the array
print k

# also: array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, rand, randn, fromfunction, fromfile

################### Basic Operations ########################

l = c - b
print l

m = b**2
print m

n = b < 80
print n

# Note: unlike in matrix languages, the product operator * operates elementwise in NumPy arrays.
# The matrix product can be performed using the dot() or creating matrix objects <---------- later in the tutorial

A = array([[1, 1], [0, 1]])
B = array([[2, 0], [3, 4]])

print "* operator on arrays:", A*B #<------------------ elementwise product
print "dot function on arrays:", dot(A, B) #<---------- matrix product

# some operations, such as += and *=, act in place to modify an existing array rather than create a new one.

# if operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one!

# operations of all the elements in an array is implemented as methods of the ndarray class.

a.sum()
a.min()
a.max()

# by specify the axis parameter you can apply an operation along the specified axis of an array:

b.sum(axis = 0) #<--------- sum of each col
b.sum(axis = 1) #<--------- sum of each row

b.cumsum(axis = 1) #<------ cumulative sum along each row!!!!!





# build a vector of 10000 normal deviates with variance = 0.5^2 and mean = 2
'''
mu, sigma = 2, 0.5

v = numpy.random.normal(mu, sigma, 10000)

pylab.hist(v, bin = 50, normed = 1)
pylab.show()
# cannot plot here.... plot at home

# compute the histogram with numpy and then plot it
(n, bins) = numpy.histogram(v, bins = 50, normed = True)
pylab.plot(.5*(bins[1:] + bins[:-1]), n)
pylab.show()
'''
