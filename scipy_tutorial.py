import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#


'''
Subpackage	Description
cluster	Clustering algorithms
constants	Physical and mathematical constants
fftpack	Fast Fourier Transform routines
integrate	Integration and ordinary differential equation solvers
interpolate	Interpolation and smoothing splines
io	Input and Output
linalg	Linear algebra
ndimage	N-dimensional image processing
odr	Orthogonal distance regression
optimize	Optimization and root-finding routines
signal	Signal processing
sparse	Sparse matrices and associated routines
spatial	Spatial data structures and algorithms
special	Special functions
stats	Statistical distributions and functions
weave	C/C++ integration
'''
# subpackages need to be imported separately
from scipy import linalg, optimize

# common functions
# it's better to import the entire package and use the functions from the package than just import the functions/modules

# Index Tricks
# np.mgrid , np.ogrid , np.r_ , and np.c_ for quickly constructing arrays
a = np.concatenate(([3], [0]*5, np.arange(-1, 1.002, 2/9.0)))
# can be written:
a = np.r_[3, [0]*5, -1:1:10j] #<------ what is this?????
# 10j is the step size in the slicing syntax.
# r_ stands for row-concatenation
# two objects bewteen commas are 2 dimensional arrays, they are stacked by rows (and must habe commensurate columns)

# mgrid
# in the simplest case, this function can be used to construct 1d ranges as a convenient substitute for arange.
# it also allows the use of complex-numbers in the step-size to indicate the number of points to place between the (inclusive) end-points.
# The real purpose of this function is to produce N, N-d arrays which provide coordinate arrays for an N-dimensional volume. <------ what is this????
# example:
print np.mgrid[0:5, 0:5]

print np.mgrid[0:5:4j, 0:5:4j]


# Vectorize function
def addsubtract(a, b):
    if a > b:
        return a - b
    else:
        return a + b
vec_addsubtract = np.Vectorize(addsubtract)

vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7])
# result will return a array!
