#!/bin/sh

exec sudo -u puppeteer python3 /puppeteer/make-tests.py /scenarios/$1
