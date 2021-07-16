# template-collection

A template repo for creating new collections of [Metapack](http://metatab.org) data packages.

*Don't fork this repo*. Instead, use the green "Use this Template" button in Github. 


## Managing the Collection


### Adding an Existing Data Package

Collections are composed of this top level directory and source packages that
are included a git submodules. So, to add a few packages:

  
    git submodule add https://github.com/metatab-packages/sandiegocounty.gov-covid19.git
    git submodule add https://github.com/metatab-packages/census.gov-boundaries-2018.git
    
Then, when checking out the collection, be sure to update all of the submodules too: 

    git clone --recurse-submodules <collection_url>
    
### Adding new data packages. 
    
To add a new package, cd to the staging directory, create the package, then check it in to github. Then use the instructions above to add it to the main directory as a submodule. 

    cd staging
    mp new -o exmaple.com -d datapackage
    cd exmaple.com-datapackage
    < Edit metadata; At least set description and title>
    mp github init
    cd ../
    git submodule add https://github.com/metatab-packages/exmaple.com-datapackage.git
    
The `mp github init` call will set up a new repo on Github for the package. It requires getting an pplication token from Github and adding it to the metatab configuration file. See ``mp github init``
    
    
### Building  packages. 

The top lvel directory defines `invoke` tasks. To use invoke you will need to `pip install invoke`. Then run `invoke -l` to like the available tasks. THe most important are: 

* `invoke build`: Run `mp build` in each package
* `invoke make`: Run `mp make` in each package, which will build the package, upload it to s3 and publish it to Wordpress, with the proper configuration. 