from astropy.io import ascii,fits
from pathlib import Path
import numpy as np
def datapath(root):
    testfilename='hlsp_igm_hst_cos_'+root+'_g130m-g160m_v3_igm-systems.txt'
    if (Path(__file__).parents[1] / 'igm' / root / testfilename).is_file():
        datapath = Path(__file__).parents[1] / 'igm' / root
        return datapath
    else:
        raise Exception("Data files not found.")


def importsystems(root):

    """Returns the system information found in
	datapath(root) as an astropy table object."""	
    
    names=['Z_SYS','DELTAV_SYS','WAVELENGTH','LINE_ID','z_ABS','SIGLEVEL' ,
           'S/N','EQW  ','EQW_ERR','BVALUE','BVALUE_ERR' ,'LOGN lower limit',
           'LOGN','LOGN_ERR','FLAG_FIT' ,'LCOD','NUM_SYS_LINES','NUM_METAL_LINES']
    systemsfile='hlsp_igm_hst_cos_'+root+'_g130m-g160m_v3_igm-systems.txt'
    systems=ascii.read(datapath(root) / systemsfile,names=names)
    
    return systems

def importlines(root,zrange=[-9999,9999],waverange=[0,np.inf],linename=None):

    """Returns the line information found in
	datapath(root) as an astropy table object."""	
    
    names=['WAVELENGTH','LINE_ID','z_ABS','SIGLEVEL' ,'S/N','EQW','EQW_ERR',
           'BVALUE','BVALUE_ERR' ,'LOGN lower limit' ,'LOGN' ,'LOGN_ERR',
           'FLAG_FIT' ,'LCOD','FLAG_ISM','FLAG_AGN']
    linesfile='hlsp_igm_hst_cos_'+root+'_g130m-g160m_v3_linelist.txt'
    lines=ascii.read(datapath(root) / linesfile,names=names)
    if linename is not None:
        lines=lines[np.where(np.array(lines['LINE_ID']) == linename)]
    lines=lines[np.where(lines['z_ABS']>zrange[0])]
    lines=lines[np.where(lines['z_ABS']<zrange[1])]
    lines=lines[np.where(lines['WAVELENGTH']>waverange[0])]
    lines=lines[np.where(lines['WAVELENGTH']<waverange[1])]
    #lines.add_row([0,'',np.mean(zrange),0,0,0,0,0,0,0,0,0,0,0,0,0]) #hack, fix please
    #lines.add_index('z_ABS')
    #lines=lines.loc['z_ABS',zrange[0]:zrange[1]]

    return lines

def importfits(root):

    """Returns the l."""	
    
    fitsfile='hlsp_igm_hst_cos_'+root+'_g130m-g160m_v3_spec.fits'
    datafile = fits.open(datapath(root) / fitsfile)
    data=datafile[1].data
    datafile.close
    wave=data['WAVE']
    flux=data['FLUX']
    cont=data['CONT']
    return wave,flux,cont