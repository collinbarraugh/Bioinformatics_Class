# Bioinformatics_Class
This is a workspace for CSCI578A Bioinformatics at Mines.

## Install

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

  `pytest -s -v tests/`

## Files

