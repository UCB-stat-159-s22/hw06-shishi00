import ligotools.utils as utils
from os.path import exists
from ligotools import readligo as rl
import numpy as np
import matplotlib.mlab as mlab

def test_whiten():
    """Test to see if the first 3 results match"""
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
    time = time_H1
    dt = time[1] - time[0]
    fs, NFFT = 4096, 4*fs
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    psd_H1 = interp1d(freqs, Pxx_H1)
    strain_H1_whiten == utils.whiten(strain_H1,psd_H1,dt)
    assert strain_H1_whiten[:3] == np.array(648.16749914, -307.14005653,  734.98585191)

def test_write_wavfile():
    """Test if write_wavfile can create a test file"""
    new_file = utils.write_wavfile('audio/' + "test.wav",int(4096), np.ones(1000))
    assert exists('audio/test.wav')
    
def test_reqshift():
    """Test if reqshift can produce accurate results"""
    assert sum(utils.reqshift(np.ones(1000), 400, 4096)) == -1.1324274851176597e-14
    
def test_plot(): 
    """Test if a plot exists"""
    assert utils.plot(
    

        


