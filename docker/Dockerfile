
FROM continuumio/miniconda3

RUN mkdir /proj
WORKDIR /proj

COPY conda-linux.yaml /tmp

RUN conda env create -f /tmp/conda-linux.yaml -n sez

RUN echo "conda activate sez" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# The code to run when container is started:
COPY  entrypoint.sh /proj
ENTRYPOINT ["./entrypoint.sh"]
CMD ["/opt/conda/envs/sez/bin/jupyter-lab", "--ip=0.0.0.0", "--port=8888", "--notebook-dir=/opt/notebooks", "--allow-root", "--no-browser"]