import numpy as np
from dedalus.core.field import Operand
from dedalus.core.operators import Operator, FutureField, Interpolate
from dedalus.tools.array import reshape_vector, axslice

import dedalus.public as de
from diagonal import SinCosDiagonal

class OpTest(Operator, FutureField):
    """SinCos  interpolation-on-diagonal operator.

    Parameters
    ----------
    arg : field object
        Field argument
    basis0, basis1 : basis identifiers
        Bases for diagonal interpolation

    Notes
    -----
    The return data is structured such that, for g = Diag(f), and x1,x2 in [a,b],
        g(x1, x2) = f(x1+x2-a, x1+x2-a)
    s.t. interpolation of g at x1=a or x2=a yields the diagonalization of f,
    i.e. f(x, x), arranged as a one-dimensional function of x2 or x1, respectively.

    """

    def __init__(self, arg, basis0, basis1, **kw):
        arg = Operand.cast(arg)
        super().__init__(arg, **kw)
        pass
        
    def meta_constant(self, axis):
        # Preserve constancy
        pass

    def check_conditions(self):
        # Shearing layout
        pass

    def operate(self, out):
        pass

test = 'fourier' # works
#test = 'sin' # fails
 
xi = de.Fourier('xi', 128)
if test == 'fourier':
    y0 = de.Fourier('y0', 128)
    y1 = de.Fourier('y1', 128)
else:
    y0 = de.SinCos('y0', 128)
    y1 = de.SinCos('y1', 128)

domain = de.Domain([xi, y0,y1],grid_dtype='float')
#domain = de.Domain([y0,y1],grid_dtype='float')

f = domain.new_field()

scd = OpTest(f,'y0','y1')

scd.meta
