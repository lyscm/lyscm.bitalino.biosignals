# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import bitalino  # pylint: disable=E0401
import requests  # pylint: disable=E0401

# %%

ENDPOINT_PORT = 8080
ENDPOINT_IP_ADDRESS = "localhost"
ENDPOINT_ADDRESS = "http://{}:{}//v1.0/gpio/led".format(
    ENDPOINT_IP_ADDRESS, ENDPOINT_PORT)


class Electromyography:

    def __init__(self, device, srate, nframes, threshold, channels):
        self.device = device
        self.srate = srate
        self.nframes = nframes
        self.threshold = threshold

        device.start(srate, channels)

    def aquire_signals(self):
        signal = self.device.read(self.nframes)
        return signal

    def set_led_status(self, pin, status):
        response = requests.post(
            "{}?pin={}&status={}".format(ENDPOINT_ADDRESS, pin, status))
        print(response)
    pass
