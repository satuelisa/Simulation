# http://code.activestate.com/recipes/576556-generating-random-numbers-with-arbitrary-distribut/ converted to Python 3

import pylab
import numpy

class GeneralRandom:

  def __init__(self, x = pylab.arange(-1.0, 1.0, .01), p = None, Nrl = 1000):
    self.set_pdf(x, p, Nrl)

  def set_pdf(self, x, p, Nrl = 1000):
    self.x = x
    self.pdf = p/p.sum()
    self.cdf = self.pdf.cumsum()
    self.inversecdfbins = Nrl
    self.Nrl = Nrl
    y = pylab.arange(Nrl)/float(Nrl)
    delta = 1.0/Nrl
    self.inversecdf = pylab.zeros(Nrl)
    self.inversecdf[0] = self.x[0]
    cdf_idx = 0
    for n in range(1,self.inversecdfbins):
      while self.cdf[cdf_idx] < y[n] and cdf_idx < Nrl:
        cdf_idx += 1
      self.inversecdf[n] = self.x[cdf_idx-1] + (self.x[cdf_idx] - self.x[cdf_idx-1]) * (y[n] - self.cdf[cdf_idx-1])/(self.cdf[cdf_idx] - self.cdf[cdf_idx-1])
      if cdf_idx >= Nrl:
        break
    self.delta_inversecdf = pylab.concatenate((pylab.diff(self.inversecdf), [0]))

  def random(self, N = 1000):
    idx_f = numpy.random.uniform(size = N, high = self.Nrl-1)
    idx = pylab.array([idx_f],'i')
    y = self.inversecdf[idx] + (idx_f - idx)*self.delta_inversecdf[idx]
    return y
