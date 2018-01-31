#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  
#  patiencebar - Terminal progress bar compatible with multi-threading
#  Copyright (C) 2016  Guillaume Schworer
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  
#  For any information, bug report, idea, donation, hug, beer, please contact
#    guillaume.schworer@obspm.fr
#
###############################################################################



import time
import numpy as np
import patiencebar as PB
from multiprocessing import Pool


# single-thread

n_calc = 34

pb = PB.Patiencebar(valmax=n_calc, barsize=50, title="Test bar")

for i in range(n_calc):
    time.sleep(np.random.random()*0.2)
    pb.update()


################################################################################
# multi-thread

def worker(params):
    pbm, num = params
    time.sleep(num*4)
    num = num**2
    pbm.update()
    return num


def worker2(params):
    i, pbm, num = params
    time.sleep(num*4)
    num = num**2
    pbm.update("Just got %ith element done: %f" % (i, num))
    return num


threads = 5
n_calc = 10
vector = np.random.random(n_calc)


pbm = PB.Patiencebarmulti(valmax=n_calc, barsize=30, title="Heavy calculation of the square of a vector")

pool = Pool(processes=threads)
result = pool.map_async(worker, ((pbm, item) for item in vector))
pool.close()
pool.join()
vector2 = np.asarray(result.get())


pbm.reset(bar=False)  # keep all other parameters already defined at init as they are

pool = Pool(processes=threads)
result = pool.map_async(worker2, ((i, pbm, item) for i, item in enumerate(vector)))
pool.close()
pool.join()
vector2b = np.asarray(result.get())
