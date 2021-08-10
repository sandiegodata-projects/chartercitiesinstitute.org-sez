#!/bin/bash 
# Install the conda packages and pip packages, resolve all versions, 
# and export an environment file, using a disposable conda environment. 


# exit when any command fails
set -e

conda env remove -n _sez_build || echo

conda env create  -f conda-minimal.yaml -n _sez_build

conda activate _sez_build

pip install -r requirements.txt

conda env export  | egrep -v '^prefix' | sed 's/_sez_build/sez/' > conda-env.yaml

conda env remove -n _sez_build