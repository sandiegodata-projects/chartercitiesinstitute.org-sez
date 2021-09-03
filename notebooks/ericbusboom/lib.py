import rasterio

# Load a year of rasters, masked and cropped to a geometry
# See the rasterio documentation for more examples: 
# https://rasterio.readthedocs.io/en/latest/topics/masking-by-shapefile.html
def load_ntl(pkg, year, shapes=None):
    
    ref = pkg.reference(f'ntl{year}').resolved_url.get_resource().get_target()
    
    with rasterio.open(str(ref.fspath)) as src:
        
        if shapes is not None:
            img, transform = rasterio.mask.mask(src, shapes, crop=True)
        else:
            img =  src.read()
            transform = None
            
        meta = src.meta
      
        
        return img, meta, transform