Setting Up Environments
-----------------------


Conda
=====

After you setup and install anaconda, you can create the environment. This installs a lot of packages, 
so it will take a while, but it prevents version conflicts later. 

For Mac OS X, and Maybe Windows, use the ``conda-env.yaml`` file:

    $ conda env create -f conda-env.yaml -n sez
    $ conda activate sez
    

For Linux, use the ``conda-linux.yaml`` file: 

    $ conda env create -f conda-linux.yaml -n sez
    $ conda activate sez
    


Strip Versions from Export
--------------------------

    $ conda env export | cut -f 1 -d '=' > conda-env-clean.yaml