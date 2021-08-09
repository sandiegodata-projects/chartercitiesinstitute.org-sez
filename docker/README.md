
Build with:

    make build

Run with: 

    docker run -t -i --rm -v `pwd`:/pwd  sez /bin/bash
    
or, to run jupyter lab:

    docker run -ti --rm -p 8888:8888 -v `pwd`:/opt/notebooks sez
    
or just: 

    ./jupyter.sh