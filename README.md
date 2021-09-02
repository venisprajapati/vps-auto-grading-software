
# Venis Prajapati's Auto grading software


<p align="right">
    Date of first Availablity: 21 August, 2021
</p>


## Purpose

- Open-source web-browser based general purpose software to make bubble-omr sheet checking and grading task Easy and Efficient, that runs on localhost using python (virtual environment).


## Technical Info

- Requirements: python 3.9 support, web browser
- languages: Python 3.9.6, Batchfile, HTML, CSS
- libraries used: 
    - Flask
    - opencv
    - numpy
    - openpyxl
    - python-docx
    - os, glob, date
    - werkzeug
    - waitress
    - webbrowser, threading


## Concept

- Convert scanned images of OMR sheet to specific width(i.e. w=624) with aspect ratio maintain, then use GaussianBlur; make it grayscale using cvtColor with COLOR_BGR2GRAY and apply some threshold to convert the pixels above threshold value to Black.

- There is some specific grid like desing to Scan specific box (i.e. around the bubble) in OMR Sheet so that function will count the number of Black pixels in specific area (or bubble), if count of black pixels is above specific value then it is filled or marked otherwise not filled or marked by the user (or student).

- 90 MCQs Bubble OMR Sheet with grid to count black pixels in specific square of grid.

    ![grid-omr](https://github.com/venisprajapati/vps-auto-grading-software/blob/main/screen-shots/grid_.png?raw=true)

- Returned objects from scan function used to make results with answers given by users and scanned by openpyxl functions, then results are added to students excel file; then omr resonses and results are used to make a document that contains all details, ranking, analysis by marks, analysis by sections, results in details for individual students and also a response ticked by students in OMR Sheet.

- Hence, OMR Sheet is checked and you have results in your hand, LOL ;)


## Installation

### Windows

- Download or Clone Project from <a href="https://github.com/venisprajapati/vps-auto-grading-software">GitHub</a>
- Unzip :/ the Project
- Install python <a href="https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe">Python 3.9.6</a>
- Run <b>install.bat</b> to install all dependencies in the project
- Run <b>vps-ags.bat</b> to start the software
- Server runs with output like: <b>Venis Prajapati's Auto grading Software Started At PORT: <a href="http://127.0.0.1:2102/">http://127.0.0.1:2102/</a> </b>

### Linux and Mac

- Download or Clone Project from <a href="https://github.com/venisprajapati/vps-auto-grading-software">GitHub</a>
- Unzip :/ the Project
- Install Python 3.9.6
- Create virtual environment and activate venv
- Run following command to install required packages & libraries
    ```
    pip3 install -r requirements.txt
    ```
- To run project run this command
    ```
    python3 app.py
    ```
- Server runs with output like: <b>Venis Prajapati's Auto grading Software Started At PORT: <a href="http://127.0.0.1:2102/">http://127.0.0.1:2102/</a> </b>


## Usage

Follow below important links:

- <a href="https://github.com/venisprajapati/vps-auto-grading-software">Github</a>
- <a href="https://medium.com/@venisprajapati2102/about-vps-auto-grading-software-5b611ffe6c74">Medium Blog</a>
- <a href="https://github.com/venisprajapati/vps-auto-grading-software/blob/main/User-guide.pdf">User Guide</a>
- <a href="https://github.com/venisprajapati/vps-auto-grading-software/issues">Issues</a>


## Developer Contact and Donate

### Contact info:
Venis Prajapati
* Email: projects.venisprajapati@gmail.com
* Github: <a href="github.com/venisprajapati">github.com/venisprajapati</a>
* LinkedIn: <a href="linkedin.com/in/venis-prajapati-a12b1019b">linkedin.com/in/venis-prajapati-a12b1019b</a>
* Medium: <a href="medium.com/@venisprajapati2102">medium.com/@venisprajapati2102</a>

### Donate

* Buy me a coffee: <a href="buymeacoffee.com/venisprajapati">buymeacoffee.com/venisprajapati</a>


## Screen Shots

1) Home Screen
    ![home-page](https://github.com/venisprajapati/vps-auto-grading-software/blob/main/screen-shots/vps-ags_main_page.png?raw=true)

2) Result Screen
    ![result-page](https://github.com/venisprajapati/vps-auto-grading-software/blob/main/screen-shots/vps-ags_result_page.png?raw=true)

3) About Screen
    ![info-page](https://github.com/venisprajapati/vps-auto-grading-software/blob/main/screen-shots/vps-ags_info_page.png?raw=true)

*Thank you, Have a nice day ;)*
