#!/bin/bash



source /opt/conda/etc/profile.d/conda.sh 

conda activate sez
/opt/conda/envs/sez/bin/jupyter-lab --ip=0.0.0.0 --port=9888 --notebook-dir=/opt/notebooks --allow-root --no-browser --NotebookApp.token='' --NotebookApp.password=''