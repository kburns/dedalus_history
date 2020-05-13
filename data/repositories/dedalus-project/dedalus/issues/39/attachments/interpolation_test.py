import dedalus.public as de
import numpy as np

import logging
logger = logging.getLogger(__name__)
root = logging.root

nr = 64
ntheta =64
nz = 64

R1 = 7.
R2 = 8.
Lz = 3.

r = de.Chebyshev('r',nr, interval=[R1, R2])
## If fourier in all 3 directions, this works.
#r = de.Fourier('r',nr, interval=[R1, R2])
theta = de.Fourier('theta', ntheta)
z = de.Fourier('z', nz, interval=[0, Lz])

domain = de.Domain([z, theta, r], grid_dtype='float')
data = domain.new_field()

zg, tg, rg = domain.grids()
data['g'] = np.sin(np.pi*rg - R1) * np.cos(2*np.pi/Lz *zg)

## Workaround: if we force transposes to be created first, everything is OK.
#data['c']
#data['g']

logger.info("beginning interpolation...")
q = data.interpolate(r = 7.5, theta = 0., z = 1.5)
logger.info("finshed interpolation...")

logger.info('interpolated value is {:18.6e}'.format(q['g'][0,0,0]))
