
FROM continuumio/miniconda3

RUN mkdir /proj
WORKDIR /proj

COPY conda-environment/build/conda-linux.yaml /proj

RUN conda init --all
#RUN conda env create -f /tmp/conda-linux-env.yaml -n sez
RUN conda env update -n base --file  /proj/conda-linux.yaml 

RUN echo "conda activate base" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# The code to run when container is started:

COPY  docker/jupyter.sh /proj

CMD ["/proj/jupyter.sh"]