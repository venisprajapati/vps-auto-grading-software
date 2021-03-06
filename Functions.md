# Functions

## Input

### 1. omrs ( .jpg/.jpeg (prefer) or .png )

* OMR sheet paper A4 (preferable)
* Black & white image - 300 dpi or greater for scanning
* Print must be in actual size or fit to scale (refer to omr-sheet folder given in repo)
* Scanned omr sheet of 90 and 200 mcqs
* Id number is mandatory in omrs

### 2. students.xlsx (Sheet1)

| A | B |
| :-------------: | :-------------: |
| id | name |
| blank line | blank line |
| A001 | Abcd Stuv |
| J124 | Cdef Ghijk |

### 3. answers.xlsx (Sheet1)

| A | B |
| :-------------: | :-------------: |
| A | single choice |
| ACD | multiple choice |
| A/D/B | either A or D or B  |
| G | grace |
|  | blank = grace |

## Output

### 1. results.docx (exam-name_exam-date.docx)

* Header + Footer (important name, exam, current-date, link)
* Exam name, Exam date, total-marks
* Result Analysis Report by Marks
* Result Analysis Report by Section (optional functionality)
* Results for Individual Students
* Checked OMRs Of Individual Students

### 2. students.xlsx (exam-name_exam-date)

* User can add absent students further but they won't get actual rank, instead process whole exam again.

| A | B |
| :-------------: | :-------------: |
| exam-name | exam-date |
| id | obtained marks |
| A001 | 211 |
| J124 | 160 |

## Screen shots

### For Input

![functions-input](screen-shots/functions-1.png?raw=true)

### For Output

![functions-output](screen-shots/functions-2.png?raw=true)

*thank you*
