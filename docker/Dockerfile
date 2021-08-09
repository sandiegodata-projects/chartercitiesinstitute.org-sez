
FROM continuumio/miniconda3

RUN mkdir /proj
WORKDIR /proj

COPY conda-linux-env.yaml /proj
COPY conda-linux-clean.yaml /proj

RUN conda init --all
#RUN conda env create -f /tmp/conda-linux-env.yaml -n sez
RUN conda env update -n base --file  /proj/conda-linux-clean.yaml 

RUN echo "conda activate base" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# The code to run when container is started:
COPY  entrypoint.sh /proj
COPY  jupyter.sh /proj
#ENTRYPOINT ["/proj/entrypoint.sh"]
CMD ["/proj/jupyter.sh"]