try:
    from urllib.request import urlretrieve  # Python 3
except ImportError:
    from urllib import urlretrieve  # Python 2

x = 12

while (x <= 168):
    first = "http://assets.weather-forecast.com/maps/static/New-York.prec."
    i = str(x)
    last = ".cc23.jpg"
    url = first + i + last
    filename = "NY-precip-" + i + ".jpg"
    
    urlretrieve(url, filename)
    x = x + 12

url = "http://m0.fast-meteo.com/pa/fcmaps/images/scales/rainandsnowscale.imperial.gif"
urlretrieve(url, "scale.jpg")
