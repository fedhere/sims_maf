import numpy as np
import healpy as hp
from .baseMetric import BaseMetric
try:
    # Try cKDTree first, as it's supposed to be faster.
    from scipy.spatial import cKDTree as kdtree
    #current stack scipy has a bad version of cKDTree.  
    if not hasattr(kdtree,'query_ball_point'): 
        from scipy.spatial import KDTree as kdtree
except:
    # But older scipy may not have cKDTree.
    from scipy.spatial import KDTree as kdtree


class LinkedMetric(BaseMetric):
    """Calculate how many other healpixels a given observation is linked to.  This is a fairly crude measure of how well the observations are linked for self-calibration pruposes.  An even better metric would look at the chip level since that's how large calibration patches will be. """

    def __init__(self, metricName='linked', plotParams=None, raCol='fieldRA', decCol='fieldDec', nside=128, fovRad=1.8):
        """nside = healpixel nside
           fovRad = radius of the field of view in degrees"""
        cols = [raCol, decCol]
        self.needRADec = True #flag so binMetric will pass ra,dec of point
        super(ParallaxMetric, self).__init__(cols, metricName=metricName)
        self.raCol = raCol
        self.decCol = decCol

        #build a kdtree for healpixel look-up

    def run(self, dataSlice, ra,dec):

        # Cut down to the unique set of ra,dec combinations

        pixlist=[]
        # For each ra,dec pointing, find the healpixels they overlap and append to the list
        
        pixlist = list(set(pixlist))
        return len(pixlist)
    
