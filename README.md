# Parallel Bubble Sort Algorithm using MPI for Python

This project illustrates the implementation of parallel bubble sort using MPI for python. This project has been done as an exercise to apply parallelism in the `High Performance Computing` course in postgraduate studies at Cairo University.

This project depends on [mpi4py](https://mpi4py.readthedocs.io/en/stable/)

## What is MPI?
MPI, [mpi-using](https://mpi4py.readthedocs.io/en/stable/intro.html#mpi-using) the Message Passing Interface, is a standardized and portable message-passing system designed to function on a wide variety of parallel computers. The standard defines the syntax and semantics of library routines and allows users to write portable programs in the main scientific programming languages (Fortran, C, or C++)

## MPI4PY Installation
https://mpi4py.readthedocs.io/en/stable/install.html

## Run
1. Install mpi4py on your machine and test it functioning by running this part of code
```
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print (“hello world from process “, rank)
```

2. Clone this project

3. Run `bubble_parallel.py` file with this command `mpiexec.exe -n [number_of_processes] python parallel_bs.py` with different number of processes

4. You can check the execution time based on your machine specs
