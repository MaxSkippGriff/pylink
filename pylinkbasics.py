import pylink

# Connect to eye tracker
tk = pylink.Eyelink('100.1.1.1')

# Open edf file - this is where we will save the 
# eye tracking data on the host PC
tk.openDataFile('test.edf')

# This sets our tracking parameters
tk.sendCommand('sample_rate 1000')

# This opens a calibration window
pylink.openGraphics()

# Calibrate the tracker before running five trials
tk.doTrackerSetup()

trials = 5
for i in range(trials):
    # Log a message in the EDF data file
    tk.sendMessage(f'Trial: {i}')