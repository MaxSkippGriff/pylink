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

trials = 10
for i in range(trials):
    # Log a message in the EDF data file
    tk.sendMessage(f'Trial: {i}')

    # Eye tracker starts recording
    tk.startRecording(1,1,1,1)

    # Record eye data every 2000ms
    pylink.msecDelay(2000)

    # Eye tracker stops recording
    tk.stopRecording()

# Close and download EDF file
tk.closeDataFile()

# Close eye tracker link and close calibration window
tk.receiveDataFile('test.edf', 'test.edf')
# 
tk.close()
pylink.closeGraphics()