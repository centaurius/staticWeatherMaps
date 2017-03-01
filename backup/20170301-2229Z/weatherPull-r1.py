try:
    from urllib.request import urlretrieve  # Python 3
except ImportError:
    from urllib import urlretrieve  # Python 2
import os, sys
import shutil
import subprocess

x = 1
while (x <= 1):
    os.getcwd()
        
    os.chdir('/home/ubuntu/workspace/staticweatherPull')
    os.chdir('cloud')
    execfile('pullCloud.py')
    os.chdir('/home/ubuntu/workspace/staticweatherPull')
    shutil.make_archive("cloud", 'zip', "cloud")
    
    os.chdir('precipitation')
    execfile('pullPrecip.py')
    os.chdir('/home/ubuntu/workspace/staticweatherPull')
    shutil.make_archive("precipitation", 'zip', "precipitation")
    
    os.chdir('temperature')
    execfile('pullTemp.py')
    os.chdir('/home/ubuntu/workspace/staticweatherPull')
    shutil.make_archive("temp", 'zip', "temperature")
    
    os.chdir('wind')
    execfile('pullWind.py')
    os.chdir('/home/ubuntu/workspace/staticweatherPull')
    shutil.make_archive("wind", 'zip', "wind")
    
    break

os.chdir("/home/ubuntu/workspace/staticweatherPull")
bashCommand = "sh clean.sh"
output = subprocess.check_output(['bash', '-c', bashCommand])


