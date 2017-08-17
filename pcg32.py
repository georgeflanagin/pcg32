#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Credits
__author__ =        'George Flanagin'
__version__ =       '1.0'
__maintainer__ =    'George Flanagin'
__email__ =         'me+pcg@georgeflanagin.com'
__status__ =        'production'
__license__ =       'GPL3, no warranty.'


"""
A Python 3 version of the PCG generator based on Melissa O'Neill's
extremely minimal C version.


typedef struct { uint64_t state;  uint64_t inc; } pcg32_random_t;

uint32_t pcg32_random_r(pcg32_random_t* rng)
{
    uint64_t oldstate = rng->state;
    // Advance internal state
    rng->state = oldstate * 6364136223846793005ULL + (rng->inc|1);
    // Calculate output function (XSH RR), uses old state for max ILP
    uint32_t xorshifted = ((oldstate >> 18u) ^ oldstate) >> 27u;
    uint32_t rot = oldstate >> 59u;
    return (xorshifted >> rot) | (xorshifted << ((-rot) & 31));
}
"""

import os
import random
import sys


try:
    import numpy as np
except ImportError as e:
    sys.stderr.write('You need to install numpy.\n')

def pcg32(param1:np.uint64=None, param2:np.uint64=None) -> np.uint32:
    """
    All we ever do is call this over and over, so let's make it
    a generator instead of a class.

    param1 -- initial state of the engine.
    param2 -- the increment.

    yields -- an int, of which 32 bits are suitable scrambled.
    """

    np.seterr(all='ignore') # remove overflow messages.

    if param1 is None: param1 = random.random() * 9223372036854775807
    if param2 is None: param2 = random.random() * 9223372036854775807

    engine = np.array([param1, param2], dtype='uint64')
    multiplier = np.uint64(6364136223846793005)
    big_1 = np.uint32(1)
    big_18 = np.uint32(18)
    big_27 = np.uint32(27)
    big_59 = np.uint32(59)
    big_31 = np.uint32(31)

    while True:
        old_state = engine[0]
        inc = engine[1]
        engine[0] = old_state * multiplier + (inc | big_1)
        xorshifted = np.uint32(((old_state >> big_18) ^ old_state) >> big_27)
        rot = np.uint32(old_state >> big_59)
        yield np.uint32((xorshifted >> rot) | (xorshifted << ((-rot) & big_31)))


if __name__=='__main__':
    param1 = np.uint64(random.random() * 9223372036854775807)    
    param2 = np.uint64(random.random() * 9223372036854775807)    
    x = pcg32(param1, param2)    
    print('Using \nInit state = ' + str(param1) + '\nIncrement  = ' + str(param2) + '\nhere is some randomness.\n')
    print([ next(x) for i in range(0, 100) ])
