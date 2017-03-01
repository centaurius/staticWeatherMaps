try:
    from urllib.request import urlretrieve  # Python 3
except ImportError:
    from urllib import urlretrieve  # Python 2

x = 12

while (x <= 168):
    first = "http://assets.weather-forecast.com/maps/static/New-York.wind."
    i = str(x)
    last = ".cc23.jpg"
    url = first + i + last
    filename = "NY-wind-" + i + ".jpg"
    
    urlretrieve(url, filename)
    x = x + 12
    
url = "http://m0.fast-meteo.com/pa/fcmaps/images/scales/tempscale.imperial.gif"
urlretrieve(url, "windscale.jpg")