================
Stock Reconciliation
================

This is a simple python program that takes text report of initial positions, transactions, and ending positions, and reconcile the changes.

Installation
------------
To install, simply clone this repo.
.. code-block:: bash
  $ git clone https://github.com/dayfine/stock-reconciliation.git


To Use
------------
.. code-block:: python
    $ python3 -m recon filename

In your CLI, use `python3 -m recon filename` command in the root directory. The filename can be either a relative or absolute path.

The program will read the given file, reconcile it, and output the result to both the terminal and an output file. The output file will be saved to the same directory where the input file is, and it will be named as the input file name followed by 'output'.


API
----------------
Class Report

Method: read_file
>

Method: reconcile
>


Tests
----------------
To test, make sure you have `pytest` installed. Then, simply run the command below:
.. code-block:: python
    $ python3 -m pytest

