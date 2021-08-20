# Venis Prajapati's Auto grading software

<p align="right">
    Date of first Availablity: 21 August, 2021
</p>

## Purpose
- Open-source web-browser based general purpose software to make bubble-omr sheet checking, the grading ask easy and efficient, that runs on localhost using python (virtual environment).

## Technical Info
- languages: Python 3.9.6, Batchfile, HTML, CSS
- libraries used: 
    - flask
    - opencv
    - numpy
    - openpyxl
    - python-docx
    - os, glob
    - werkzeug
    - waitress
    - webbrowser, threading

## Concept
- Convert scanned images of OMR sheet to specific width(i.e. w=624) with aspect ratio maintain, then use GaussianBlur; make it grayscale using cvtColor with COLOR_BGR2GRAY and apply some threshold to convert the pixels above threshold value to Black.

- There is some specific grid like desing to Scan specific box (i.e. around the bubble) in OMR Sheet so that function will count the number of Black pixels in specific area (or bubble), if count of black pixels is above specific value then it is filled or marked otherwise not filled or marked by the user (or student).
