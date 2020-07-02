from plotdanforth2016sys.io import *
import matplotlib.pyplot as plt
import numpy as np

def plotlinesinzrange(root,linename,linerestwave,zrange=[-99,99],norm=True,waverangepad=3):
    wave,flux,cont=importfits(root)
    
    lines=importlines(root,zrange=zrange)

    lines = lines[np.where(np.array(lines['LINE_ID']) == linename)]
    waverange=[(1+np.min(lines['z_ABS']))*linerestwave,(1+np.max(lines['z_ABS']))*linerestwave]
    waverange[0]=waverange[0]-waverangepad
    waverange[1]=waverange[1]+waverangepad
    fig = plt.figure(figsize=(6,6))
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    if norm:
        fluxnorm=flux/cont
        axes.plot(wave,fluxnorm, 'xkcd:red')
        axes.set_ylabel('Normalized Flux (arbitrary units)')
        axes.set_ylim([-0.1,1.5])


    else:
        axes.plot(wave,flux, 'xkcd:red')
        axes.plot(wave,cont, 'xkcd:blue')
        axes.set_ylabel('Flux')
    axes.set_title('{} from z={} to z={}'.format(linename,zrange[0],zrange[1]))
    axes.vlines(linerestwave*(1+lines['z_ABS']),-999,999,colors='green')
    axes.set_xlabel('Observed wavelegnth ($\AA$)')
    axes.set_xlim(waverange)
    return fig