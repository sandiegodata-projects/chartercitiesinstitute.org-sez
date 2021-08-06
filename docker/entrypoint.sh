#!/bin/bash --login
# The --login ensures the bash configuration is loaded,
# enabling Conda.

#set -euo pipefail
#set -eu
conda activate sez
exec /opt/conda/envs/sez/bin/jupyter-lab --ip=0.0.0.0 --port=8888 --notebook-dir=/opt/notebooks --allow-root --no-browser