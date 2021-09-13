import rasterio
from joblib import Parallel, delayed
from tqdm.notebook import tqdm
import numpy as np 
import pandas as pd

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
    
def mp_ntl_mask(ntl_p, df, col='geometry'):
    """Run a multi-process masking operation to return numpy arrays extracted from the 
    NTL datasets in the ntl_p packages according to each of the geometries in the df GeoDataFrame, using the 
    geometry column col """
    tasks = [  (year, r.unique_id, r[col]) for idx,r in df.iterrows() for year in list(range(1992, 2018+1))]
    print(len(tasks))

    # Run the extraction tasks in parallel
    # First, define the function we will run in parallel
    def _f(year, sez_id, geo):
        try:
            return (year, sez_id, load_ntl(ntl_p, year, [geo])[0])
        except Exception as e:
            return (year, sez_id, e)

    # Second, run the tasks
    patches = Parallel(prefer='threads')(delayed(_f)(*t) for t in tqdm(tasks, desc=col))

    exc = [(year, sez_id,  e) for year, sez_id,  e in patches if isinstance(e, Exception)]

    return patches, exc, tasks


def make_rings(df, r1, r2=None):
    """Return geometries for rings around the points ( or other geometry ) in df. If not specified, 
    r2 is selected so the area of the ring is equal to the area of the circle described by r1, 
    r2 = sqrt(2)*r1"""

    if r2 is None:
        r2 = np.sqrt(2)*r1
    
    buf_r1 = df.to_crs(3395).buffer(r1)
    buf_r2 = df.to_crs(3395).buffer(r2)

    # Check that relative difference is close to zero --> areas are equal
    # rel_diff = ((sez_buf_r1.area - sez_buf_r2.difference(sez_buf_r1).area)/sez_buf_r1.area).round(8)
    # assert rel_diff.sum() == 0

    return buf_r2.difference(buf_r1).to_crs(4326)

def build_ring_sums(ntl_p, sez_df, radius=10_000):
    
    sez_rings = make_rings(sez_df, radius)

    sez_df = sez_df.join(sez_rings.to_frame('ring'))

    patches, exc, tasks = mp_ntl_mask(ntl_p, sez_df.to_crs(4326), 'ring')

    rows = [ (e[0],e[1], np.nansum(e[2])) for e in patches]

    return sez_df, patches, pd.DataFrame(rows, columns=['year','sez_id','pix_sum'])


def split_series(df, col=None):
    
    col = col or 'mean_light'
    
    bf = df[df.year<=df.op_year].sort_values('year').reset_index(drop=True)
    af = df[df.year>=df.op_year].sort_values('year').reset_index(drop=True)

    bf[col] = bf[col].fillna(method='bfill').fillna(method='ffill')
    af[col] = af[col].fillna(method='bfill').fillna(method='ffill')
    
    return bf, af


def exp_line_fit(x,y=None, col='mean_light'):
    
    from numpy.linalg import LinAlgError 
    
    if y is None:
        df = x
        x = df['year']
        y = df[col]
    else:
        df = None
    
    y = np.log(y)
    
    try:
        fit = np.polyfit(x,y,1)
    
    except LinAlgError:
        # Didn't converge
        return [np.nan,np.nan]
    except TypeError:
        # Maybe that x or y is empty
        return [np.nan,np.nan]
    except ValueError:
        # Something Else, maybe that x or y is empty
        return [np.nan,np.nan]
    
        
    beta, alpha = np.exp(fit)
    
    return beta-1, alpha



def compute_yoy(df, col=None):
    
    bf, af = split_series(df, col)
    
    def _f(t):
        ml = t.mean_light
        return (ml.iloc[-1]-ml.iloc[0])/len(ml)
        
    return pd.Series([_f(bf), _f(af)])

def compute_slopes(df, col=None):

    bf, af = split_series(df, col)
    

    return pd.Series([exp_line_fit(bf)[0], exp_line_fit(af)[0]])
