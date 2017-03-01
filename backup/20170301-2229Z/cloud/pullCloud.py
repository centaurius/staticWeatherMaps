try:
    from urllib.request import urlretrieve  # Python 3
except ImportError:
    from urllib import urlretrieve  # Python 2
import zipfile

x = 12

while (x <= 168):
    first = "http://assets.weather-forecast.com/maps/static/New-York.cloud."
    i = str(x)
    last = ".cc23.jpg"
    url = first + i + last
    filename = "NY-cloud-" + i + ".jpg"
    
    urlretrieve(url, filename)
    x = x + 12
    
    