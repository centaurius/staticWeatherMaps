#!/bin/bash

cd /home/ubuntu/workspace/staticweatherPull/cloud
rm *.jpg

cd /home/ubuntu/workspace/staticweatherPull/precipitation
rm *.jpg

cd /home/ubuntu/workspace/staticweatherPull/temperature
rm *.jpg

cd /home/ubuntu/workspace/staticweatherPull/wind
rm *.jpg

cd /home/ubuntu/workspace/staticweatherPull
sudo mv cloud.zip /zips
sudo mv precipitation.zip /zips
sudo mv wind.zip /zips
sudo mv temp.zip /zips
