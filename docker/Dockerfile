
FROM continuumio/miniconda3

RUN mkdir /proj
WORKDIR /proj

COPY conda-linux.yaml /proj

RUN conda init --all

RUN conda env create -n sez --file  /proj/conda-linux.yaml 

RUN echo "conda activate sez" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

COPY conda-minimal.yaml /proj
COPY requirements.txt /proj
COPY entrypoint.sh /proj
COPY jupyter.sh /proj
COPY build.sh /proj

#ENTRYPOINT ["/proj/entrypoint.sh"]
CMD ["/proj/jupyter.sh"]