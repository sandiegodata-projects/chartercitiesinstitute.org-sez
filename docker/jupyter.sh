#!/bin/bash


source /opt/conda/etc/profile.d/conda.sh 

conda activate base
/opt/conda/bin/jupyter-lab --ip=0.0.0.0 --port=8888 --notebook-dir=/opt/notebooks --allow-root --no-browser