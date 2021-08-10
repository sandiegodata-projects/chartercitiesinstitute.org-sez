# chartercitiesinstitute.org-sez

Nighttime lights analysis for the Charter Cities Institute


## Setting up environment

To get started, you should set up a conda environment with the environment file in the
``requirements`` directory, using the ``conda-linux.yaml`` or ``conda-mac.yaml`` files:

    $ cd requirements
    $ conda env create -f conda-env.yaml
    $ conda activate sez
    
You can also set a different name for the new environment

    $ conda env create -f conda-env.yaml -n other_name
    $ conda activate other_name
    

Then you can run jupyter-lab and run some of the notebooks: 

    $ cd ../
    $ jupyter-lab
    

You can also run Jupyter in the conda environment under Docker by running the Makefile in the 
``docker`` directory: 

   cd docker
   make build # Build the docker image
   make jupyter

