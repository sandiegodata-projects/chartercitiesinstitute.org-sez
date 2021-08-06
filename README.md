# chartercitiesinstitute.org-sez

Nighttime lights analysis for the Charter Cities Institute


## Setting up environment

To get started, you should set up a conda environment with the environment file in the
``requirements`` directory:

    $ cd requirements
    $ conda env create -f conda-env.yaml
    $ conda activate sez
    
You can also set a different name for the  new environment

    $ conda env create -f conda-env.yaml -n other_name
    $ conda activate other_name
    
Then you can run jupyter-lab and run some of the notebooks: 

    $ cd ../
    $ jupyter-lab
    
### Testing the Environment

You can test that the conda configurations work in Linux under Docker by running: 

    docker run -t -i --rm -v `pwd`:/pwd  continuumio/miniconda3 /bin/bash

From the root of the repository. Then, ``cd /pwd`` will allow you to run all of the
setup commands above, in a Linux environment. 


    $ cd requirements
    $ conda env create -f conda-linux.yaml
    $ conda activate sez

