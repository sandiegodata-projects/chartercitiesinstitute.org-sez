# chartercitiesinstitute.org-sez

Nighttime lights analysis for the Charter Cities Institute


## Setting up environment

The Python environment for this project is managed with conda, using one of the 
environment files in the requirements directory that is specific you your operating system. 

For instance, to install these files on a Mac: 

    conda env create -f conda-environment/build/conda-Darwin.yaml -n sez
    
Or, you can create the environment in Anaconda navagator. In the "Environments" click the "import" button 
import a file for your environment. 


You can also run Jupyter in the conda environment under Docker by running the Makefile:

   make build # Build the docker image
   make jupyter
   
 Then open your browser on http://127.0.0.1:9888/lab

### Troubleshooting Environment Issues

If you have problems with installing the conda environment, or Notebooks don't run correctly, 
try installing the minimal conda env file; 

    conda env create -f conda-minimal.yaml -n sez
    
    
