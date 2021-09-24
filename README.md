
# Venis Prajapati's Auto grading software


<p align="right">
    Date of first Availablity: 21 August, 2021
</p>


## Purpose

- Open-source web-browser based general purpose software to make bubble-omr sheet checking and grading task Easy and Efficient, that runs on localhost using python (virtual environment).


## Technical Info

- Requirements: python 3.9 support, Web browser
- languages: Python == 3.9.6, Batchfile, HTML, CSS
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

- Scanned images will be processed to find biggest contour in img, then after applying some <b>Threshold</b> algorithm will crop scanned image using <b>Perspective Transform</b>.

- Converted scanned images of OMR sheet to specific width and height with maintain aspect ratio aintain, then use <b>GaussianBlur</b>; make it grayscale using <b>cvtColor</b> with <b>COLOR_BGR2GRAY</b> and apply some threshold to convert the pixels above threshold value to Black.

- There is some specific grid like desing to Scan specific box (i.e. around the bubble) in OMR Sheet so then functions will count the <b>number of Black pixels</b> in specific area (or bubble), if count of black pixels is above specific value then it is filled or marked otherwise not filled or marked by the user (or student).

- 190 MCQs Bubble OMR Sheet with perspective-transformed image and mcq area highlighted to check count black pixels in specific square in virtual grid.

    ![contour-and-mcq-area](https://github.com/venisprajapati/vps-auto-grading-software/blob/main/screen-shots/contour-and-mcq-area.png?raw=true)

- Returned objects from scan function used to make results with answers given by users and scanned by openpyxl functions, then results are added to students excel file; then omr resonses and results are used to make a document that contains all details, ranking, analysis by marks, analysis by sections, results in details for individual students and also a response ticked by students in OMR Sheet.

- Hence, OMR Sheet is checked and you get result and student-report-cards.


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
- Also create 2 folders in project directory <b>uploads</b> and <b>uploads/omrs</b>.
- To run project run this command
    ```
    python3 app.py
    ```
- Server runs with output like: <b>Venis Prajapati's Auto grading Software Started At PORT: <a href="http://127.0.0.1:2102/">http://127.0.0.1:2102/</a> </b>


## Test

- For testing, put scanned images in <b>test</b> directory, then run following command
    ```
    python test.py
    ```
- This will show detected contour, perspective transform, draw rectangles in mcq area as shown in above image in Concept section.
- In line no.-14, you can change to respective omr size i.e. 190, 120.., .
    ```
    total_mcqs = 90
    ```
- It will also print python dictionary, containing information of all scanned OMRs for test.


## Usage

Follow below important links:

- <a href="https://github.com/venisprajapati/vps-auto-grading-software/blob/main/User-guide.pdf">User Guide</a>
- <a href="https://medium.com/@venisprajapati2102/about-vps-auto-grading-software-5b611ffe6c74">Medium Blog</a>
- <a href="https://github.com/venisprajapati/vps-auto-grading-software/issues">Issues</a>
- <a href="https://github.com/venisprajapati/vps-auto-grading-software">Github</a>


## Developer

### Developer contact info:
Venis Prajapati
* Email: projects.venisprajapati@gmail.com
* Github: <a href="https://github.com/venisprajapati">github.com/venisprajapati</a>
* LinkedIn: <a href="https://linkedin.com/in/venis-prajapati-a12b1019b">linkedin.com/in/venis-prajapati-a12b1019b</a>
* Medium: <a href="https://medium.com/@venisprajapati2102">medium.com/@venisprajapati2102</a>


## License

Copyright (c) 2021 Venis Prajapati.

Licensed under the [MIT](LICENSE) license.


## Screen Shots

1) Home Screen
    ![home-page](https://github.com/venisprajapati/vps-auto-grading-software/blob/main/screen-shots/vps-ags_main_page.png?raw=true)

2) Result Screen
    ![result-page](https://github.com/venisprajapati/vps-auto-grading-software/blob/main/screen-shots/vps-ags_result_page.png?raw=true)

3) About Screen
    ![info-page](https://github.com/venisprajapati/vps-auto-grading-software/blob/main/screen-shots/vps-ags_info_page.png?raw=true)

*thank you*