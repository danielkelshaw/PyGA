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

## **History:**
The optimisation history is written to a ```History``` data structure
to allow the user to further investigate the optimisation procedure 
upon completion. This is a powerful tool, letting the user define custom
history classes which can record whichever data the user desires.

Tracking the history of the optimisation process allows for plotting
of the results, an example demonstration is seen in the
```plot_fitness_history``` function - this can be further customised
through the designation of a ```PlotDesigner``` object which provides
formatting instructions for the graphing tools.

## **Customisation:**
Though the base ```SOGA``` will work for many, there maybe aspects that
one may want to change, such as the selection / recombination methods.
A common interface has been designed for these, this ensures that the
user can alter the functionality at will and researchers can implement
additional functionality with ease.

Attributes of the ```SOGA``` instance can be modified to implement
alternative methods, this is demonstrated below:

```python
# using 'uniform crossover' as the crossover method
from pyga.utils.crossovers import UniformCrossover
optimiser.crossover = UniformCrossover(p_swap=0.25)
```
```python
# using 'fitness-proportionate selection' as the selection method
from pyga.utils.selections import FitnessProportionateSelection
optimiser.selection = FitnessProportionateSelection()
```

It is also possible to define alternative termination criteria through
implementation of a ```TerminationManager``` class, a couple of examples
are demonstrated below:

```python
# using elapsed time as the termination criteria
from pyga.utils.termination_manager import TimeTerminationManager
optimiser.termination_manager = TimeTerminationManager(t_budget=10_000)
```

```python
# using error as the termination criteria
from pyga.utils.termination_manager import ErrorTerminationManager
optimiser.termination_manager = ErrorTerminationManager(
    optimiser, target=0.0, threshold=1e-3
)
```

###### Author: Daniel Kelshaw