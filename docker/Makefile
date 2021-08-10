
NS = sandiegodata.org
VERSION = latest

ENV = 
REPO = sez
NAME = sez
INSTANCE = default
DOCKER ?= docker
VOLUMES = -v $(shell pwd)/..:/opt/notebooks 
PORTS = -p 9888:9888 --expose 9888

.PHONY: build push shell run start stop restart reload rm rmf release

# Build the sez image using the conda-linux environment, coppied from ../requirements
build:
	cp ../requirements/conda-linux.yaml . 
	$(DOCKER) build -t $(NS)/$(REPO):$(VERSION) .


# build the conda-linux.yaml file from conda-minimal.yaml and requirements.txt, and write it
# back into ../requirements
build-env:
	cp ../requirements/conda-minimal.yaml .
	cp ../requirements/requirements.txt . 
	
	$(DOCKER) build -t  $(NS)_env/$(REPO):$(VERSION) -f Dockerfile.build-env .
	
	$(DOCKER) run --rm -ti --name $(NAME)_jupyter  $(CAP)  $(PORTS) $(VOLUMES) $(ENV) $(NS)_env/$(REPO):$(VERSION) /opt/notebooks/docker/build.sh

# Open a bash shell in the sez image
shell:
	$(DOCKER) run --rm -ti --name $(NAME)_shell  $(CAP) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) /bin/bash


# Open a bash shekll for debugging the process to build the conda environment
shell-build:
	$(DOCKER) run --rm -ti --name $(NAME)_shell  $(CAP) $(PORTS) $(VOLUMES) $(ENV) $(NS)_env/$(REPO):$(VERSION) /bin/bash


# Run a Jupyter-lab instance
jupyter:
	$(DOCKER) run --rm -ti --name $(NAME)_jupyter  $(CAP)  $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) /opt/notebooks/docker/jupyter.sh
	

rmf:
	$(DOCKER) rm -f $(NAME)

rm:
	$(DOCKER) rm $(NAME)

