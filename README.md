# pylink

PsychoPy is a Python based stimulus presentation solution. 

It comes with native support for EyeLink eye trackers, and contains a fully featured wrapper for the EyeLink C API via the PyLink library. In order to use PyLink with PsychoPy the EyeLink Developers Kit must be installed on the same computer as PsychoPy. 

Once the EyeLink Developers Kit is installed you should have full access to all of the available API functions.

1. Configure your Display PC's network connection to communicate with the EyeLink Host PC.

2. Download and install the latest version of the EyeLink Developers Kit

3. Download and install the latest version of PsychoPy

4. Replace the PyLink library included in PsychoPy with the latest version. The PyLink library included in PsychoPy may be slightly older than the ones included in the EyeLink Developers Kit.  To be sure that you have the most up to date version, please replace the pylink folder that comes with PsychoPy with the appropriate version from the EyeLink Developers Kit.

* Windows (64-bit): Copy the pylink folder from C:\Program Files (x86)\SR Research\EyeLink\SampleExperiments\Python\64\3.6\ and paste it to:

    C:\Program Files\PsychoPy3\Lib\site-packages\

* MacOS: Copy the pylink folder from /Applications/EyeLink/SampleExperiments/Python/3.6/ and paste it to:

    /Applications/PsychoPy.app/Contents/Resources/lib/python3.6/

* Ubuntu: To move the correct pylink folder to PsychoPy enter the following code in terminal:

Enter the following:

    sudo cp -r /usr/share/EyeLink/SampleExperiments/Python/64/3.8/pylink /usr/lib/python3/dist-packages/

To check if PyLink is properly installed in PsychoPy, enter the following code in the PsychoPy Coder shell. If no error message comes up, you are all set.

    import pylink