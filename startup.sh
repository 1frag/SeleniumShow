#!/bin/bash
if [ -f "./chromedriver" ]; then
    echo "chromedriver already exist"
else
    echo "chromedriver does not exist. Try to download"
    curl -X GET https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip > sel.zip
    unzip sel.zip
    rm sel.zip
    if [ -f "./chromedriver" ]; then
        echo "chromedriver successfully installed. App starting..."
    else
        echo "instalation failed"
        exit 1
    fi
fi
python3 main.py
