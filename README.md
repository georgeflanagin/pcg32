# pcg32
A Python implementation of the PCG32 algorithm by Melissa O'Reilly

Professor O'Reilly has a great paper on the subject: `http://www.pcg-random.org/pdf/hmc-cs-2014-0905.pdf` 

Now if the speed of generating a zillion or so random integers is the main issue, the Python 3 might not
be your choice in spite of how fast numpy runs. However, if you are studying either Python or 
random numbers, then immediate access to the algorithm in a language that you know might be the key.

The single file contains everything you need, and the one function is a generator allowing you
to invoke it with `next()`. There is a short program at the bottom that exercises the generator
and prints the results, giving you some ideas. In your own code it will probably look like this

```

import pcg32

my_generator = pcg32(state, inc)
one_million_ints = (next(my_generator) for i in range(0, 1000000))
```
