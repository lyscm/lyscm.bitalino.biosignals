# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import bitalino  # pylint: disable=E0401
import time
import BITalino
import numpy  # pylint: disable=E0401
import requests  # pylint: disable=E0401

# %%
# Set variables
srate = 1000
channels = [0]
nframes = 100
threshold = 5


# %%
# Mac OS
# macAddress = "/dev/tty.BITalino-XX-XX-DevB"
# Windows/Container/Raspberry
macAddress = "98:D3:41:FD:4F:19"
device = bitalino.BITalino(macAddress)


# %%
emg = BITalino.Electromyography(
    device, srate=srate, channels=channels, nframes=nframes, threshold=threshold)


def main():

    pin = 23

    try:
        while True:
            signal = emg.aquire_signals()

            if numpy.mean(signal[:, 1]) < 1:
                break

            emg_data = signal[:, -1]

            envelope = numpy.mean(abs(numpy.diff(emg_data)))

            print("Envelope: {}".format(envelope))

            try:
                if envelope > threshold:
                    emg.set_led_status(pin=pin, status="on")
                else:
                    emg.set_led_status(pin=pin, status="off")
            except requests.exceptions.RequestException as e:
                time.sleep(1)
                print(e)
    finally:
        print("STOP")
        device.stop()
        device.close()


if __name__ == "__main__":
    main()


# %%
