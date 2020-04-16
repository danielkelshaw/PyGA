# PyGA

[![Build Status](https://travis-ci.org/danielkelshaw/PyGA.svg?branch=master)](https://travis-ci.org/danielkelshaw/PyGA)

PyGA is an extensible toolkit for Genetic Algorithms (GA) in Python.

The library aims to provide a high-level declarative interface which
ensures that GAs can be implemented and customised with ease. PyGA 
features an extensible framework which allows researchers to provide 
custom implementations which interface with existing functionality.

- **License:** MIT
- **Python Versions:** 3.6+

## **Features:**
- [x] High-level module for Genetic Algorithms.
- [x] Extensible API for implementing new functionality.

## **Basic Usage:**

PyGA aims to provide a high-level interface for Genetic Algorithms - the
code below demonstrates just how easy running an optimisation procedure
can be.

```python
import pyga
from pyga.utils.functions import single_objective as fx


bounds = {
    'x0': [-1e6, 1e6],
    'x1': [-1e6, 1e6],
    'x2': [-1e6, 1e6]
}

optimiser = pyga.SOGA(bounds, n_individuals=30, n_iterations=100)
optimiser.optimise(fx.sphere)
```

## **Customisation:**
Though the base ```SOGA``` will work for many, there maybe aspects that
one may want to change, such as the selection / recombination methods.
A common interface has been designed for these, this ensures that the
user can alter the functionality at will and researchers can implement
additional functionality with ease.

Attributes of the ```SOGA``` instance can be modified to implement
alternative methods, this is demonstrated below:

```python
from pyga.utils.crossovers import UniformCrossover
from pyga.utils.selections import FitnessProportionateSelection

optimiser.crossover = UniformCrossover(p_swap=0.25)
optimiser.selection = FitnessProportionateSelection()
```
