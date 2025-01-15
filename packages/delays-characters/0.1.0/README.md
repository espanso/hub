# Delays-characters

An Espanso trigger that uses the Python `pynput` library to inject text, *instead* of Espanso. This enables the addition of pauses (sleep), \<Tab> etc, and other key combinations not supported by Espanso. It can include use of Espanso {{variables}}. 

See https://pynput.readthedocs.io/en/latest/keyboard.html#controlling-the-keyboard for details of the keywords, and https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key for the key names.

If necessary, use `python -m pip install pynput` to add pynput to your Python installation. Tested here with Python 3.10 but may work from Python 2.7 or earlier.

Supports keywords "type", "tap", "press", "release", and "sleep".

The package includes a sample script which demonstrates a delay and the effect of simulating pressing the \<Shift> key. For different scripts, copy, and rename, the `package.yml` file into the `espanso/match/` directory. Edit the trigger value and Input list to suit your purpose.

NB. *The variable {{Trig}} **must** match the trigger in length at least, so that `parse_pynput.py` removes the trigger text cleanly.*

A possible future enhancement could be the addition of mouse control.
