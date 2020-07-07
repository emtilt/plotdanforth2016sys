from plotdanforth2016sys.io import *
import matplotlib.pyplot as plt
import numpy as np

def plotlinesinzrange(root,linename='OVI 1032',linerestwave=1031.93,zrange=[-99,99],norm=True,waverangepad=3,linemark=True,otherlines=True):
    wave,flux,cont=importfits(root)
    fluxrange=[-0.1,1.5]

    wantedlines=importlines(root,zrange=zrange,linename=linename)

    fig = plt.figure(figsize=(6,6))
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    
    if len(wantedlines) > 0:
        waverange=[(1+np.min(wantedlines['z_ABS']))*linerestwave,(1+np.max(wantedlines['z_ABS']))*linerestwave]    
        waverange[0]=waverange[0]-waverangepad
        waverange[1]=waverange[1]+waverangepad
        axes.vlines(linerestwave*(1+wantedlines['z_ABS']),-999,999,colors='green',label=linename)
        for i in range(0,len(wantedlines)):
            offset=0.03+0.03*(i % 3)
            axes.text(wantedlines['WAVELENGTH'][i],fluxrange[1]-offset*(fluxrange[1]-fluxrange[0]),wantedlines['LINE_ID'][i],color='green')
    else:
        waverange=[(1+zrange[0])*linerestwave,(1+zrange[1])*linerestwave]
        

    if norm:
        fluxnorm=flux/cont
        axes.plot(wave,fluxnorm, 'xkcd:red')
        axes.set_ylabel('Normalized Flux (arbitrary units)')
        axes.set_ylim(fluxrange)
    else:
        axes.plot(wave,flux, 'xkcd:red')
        axes.plot(wave,cont, 'xkcd:blue')
        axes.set_ylabel('Flux')
        
    axes.set_title('{} from z={} to z={} in the {} sightline'.format(linename,zrange[0],zrange[1],root))
    axes.set_xlabel('Observed wavelegnth ($\AA$)')
    axes.set_xlim(waverange)
    
    if otherlines:
        unwantedlines=importlines(root,waverange=waverange,linename=None)
        unwantedlines=unwantedlines[np.where(np.array(unwantedlines['LINE_ID']) != linename)]

        axes.vlines(unwantedlines['WAVELENGTH'],-999,999,colors='xkcd:light gray')
        for i in range(0,len(unwantedlines)):
            offset=0.01+0.03*(i % 3)
            axes.text(unwantedlines['WAVELENGTH'][i],fluxrange[0]+offset*(fluxrange[1]-fluxrange[0]),unwantedlines['LINE_ID'][i],color='xkcd:gray')
    #axes.legend()
    return fig