Setting Up Environments
-----------------------


Conda
=====

After you setup and install anaconda, you can create the environment. This installs a lot of packages, 
so it will take a while, but it prevents version conflicts later. 

For Mac OS X, and Maybe Windows, use the ``conda-mac.yaml`` file:

    $ conda env create -f conda-mac.yaml -n sez
    $ conda activate sez
    

For Linux, use the ``conda-linux.yaml`` file: 

    $ conda env create -f conda-linux.yaml -n sez
    $ conda activate sez
    

The ``conda-minimal.yaml`` and ``requirements.txt`` files are for building version-pinned yaml files for
specific platforms. See ``build.sh`` for an example. 


Strip Versions from Export
--------------------------

Remove all of the version from an environment file. 

    $ conda env export | cut -f 1 -d '=' > conda-env-clean.yaml