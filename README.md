# pcg32
A Python implementation of the PCG32 algorithm by Melissa O'Reilly

Professor O'Neill has a great paper on the subject: `http://www.pcg-random.org/pdf/hmc-cs-2014-0905.pdf` 
I'm not kidding. This paper is readable and somewhat humorous; I wish I could say the same about my own
papers. And there is a *great* quote in the paper that appears on my website's quote list
`http://georgeflanagin.com/quotes.php#oneill`:

*From a very practical perspective, the longer the code, the more likely it is to contain an implementation error.*

Now if the speed of generating a zillion or so random integers is the main issue, the Python 3 might not
be your choice in spite of how fast `numpy` runs. However, if you are studying either Python or 
random numbers, then immediate access to the algorithm in a language that you know might be the key.

The single file contains everything you need, and the one function is a generator allowing you
to invoke it with `next()`. There is a short program at the bottom that exercises the generator
and prints the results, giving you some ideas. In your own code it will probably look like this

```python
import pcg32

# create an instance using random initialization
my_generator = pcg32()

# create something repeatable by supplying values
my_generator = pcg32(initial_state, an_increment)

# If you need a generator expression around the generator, using a generator for the number
# you need. This saves storage space, and does not run the code all at once.

one_million_ints = (next(my_generator) for i in range(0, 1000000))

# If you need a list.
one_thousand_ints = [ next(my_generator) for i in range(0, 1000) ]
```
