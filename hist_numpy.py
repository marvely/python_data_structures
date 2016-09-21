import numpy
import pylab

# build a vector of 10000 normal deviates with variance = 0.5^2 and mean = 2

mu, sigma = 2, 0.5

v = numpy.random.normal(mu, sigma, 10000)

pylab.hist(v, bins = 50, normed = 1)
pylab.show()
# cannot plot here.... plot at home

# compute the histogram with numpy and then plot it
(n, bins) = numpy.histogram(v, bins = 50, normed = True)
pylab.plot(.5*(bins[1:] + bins[:-1]), n)
pylab.show()
