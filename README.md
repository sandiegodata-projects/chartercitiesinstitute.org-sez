# chartercitiesinstitute.org-sez

Nighttime lights analysis for the Charter Cities Institute


## Setting up environment

The conda environment files are created using the Makefile in the ``conda-environment``
submodule; See the README there for how to update the file

To install these files on a Mac: 

    conda env create -f conda-environment/build/conda-Darwin.yaml -n sez
    
For Linux

    conda env create -f conda-environment/build/conda-linux.yaml -n sez

For other environments you will need to create an environment file

You can also run Jupyter in the conda environment under Docker by running the Makefile in the 
``docker`` directory: 

   cd docker
   make build # Build the docker image
   make jupyter
   
 Then open your browser on http://127.0.0.1:9888/lab

