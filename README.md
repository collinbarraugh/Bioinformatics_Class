
# Bioinformatics_Class

This is a workspace for CSCI578A Bioinformatics at Mines.

## Description

Every student in this class is required to choose one algorithm covered in the course from the below list and implement it using one programming language, such as C, C++, Java, Python, and so on. Your deliverables should include the following content:

A project report to include:

- a description on your selected algorithm and your understanding on the algorithm;
- a description on your implementation of the algorithm including what programming language (name and version) and what OS platform of your development environment, as well as the procedures/commands to compile your codes and those to run the executables;
- a description on how you want to verify your algorithm, such as how you design test cases; an analysis on your experimental results on your test cases.
- A zip package to include your source codes that implement your selected algorithm. You can include the executables in the package, but the grader will only use it for reference purpose. To evaluate your submission, the grader will compile your source codes to create executables.

Your deliverables are due at 11:59:59PM on Wednesday 12/15/2021. Early submission is highly recommended.

Algorithm list:

- The Basic Local Alignment Search Tool (BLAST)
- The UPGMA algorithm to build a phylogentic tree.
- The de Bruijn graph algorithm to assembly DNA sequences.
- Deep neural network to study a biological problem, such as protein function prediction, DNA sequence representation, etc.

## Installation

  To install the dependencies in the .yml file:

  `conda env create`

  `conda activate bioinformatics_class`
  
  `python setup.py develop`

  Or install with pip:

  `pip install --editable=git+https://github.com/collinbarraugh/Bioinformatics_Class.git`

  If you edit the .yml file with new packages to install, just use:

  `conda env update`

## Testing

  Verify your installation is correct by running:

  `pytest -s -v tests/test.py`


