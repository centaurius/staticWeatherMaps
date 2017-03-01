#!/bin/bash
git add .
git commit -a -m "static weather autoupdate `date +%F-%T`"
git push