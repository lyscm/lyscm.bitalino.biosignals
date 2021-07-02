# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import bitalino  # pylint: disable=E0401
import numpy as np  #pylint: disable=E0401
import time
import random
import matplotlib.pyplot as plt  #pylint: disable=E0401
from threading import Thread
from statsmodels.nonparametric.smoothers_lowess import lowess  # pylint:disable=E0401
import peakutils.peak  #pylint: disable=E0401
import math
import sensors


# %%
# Set variables
num_buzz_trig = 20
threshold = 0
trialData = []
trial = True


# %%
# Mac OS
# macAddress = "/dev/tty.BITalino-XX-XX-DevB"
# Windows/Container/Raspberry
macAddress = "20:17:09:18:58:60"
device = bitalino.BITalino(macAddress)


# %%
signals = sensors.Biosignals(
    device, trialData, num_buzz_trig, threshold, trial)

def main():
    if(signals.calibrateSensor()):
        print("Calibration successful")
        #thread one deals with continuous data acquision
        t1 = Thread(target=signals.dataAcquisition)
        #thread two controls the experiment and triggers the buzzer
        t2 = Thread(target=signals.triggerBuzzer)
        t1.setDaemon(True)
        t2.setDaemon(True)
        t1.start()
        t2.start()
        #rejoin threads to execute drawCharts sequentially
        t1.join()
        t2.join()
        if(signals.validateResults()):
            signals.drawCharts()
        else:
            print("Trial unsucessfull, you may have missed to react to the buzzer")
    else:
        print("Calibration unsuccessfull, please analyze data")


if __name__ == "__main__":
    main()



# %%
