# Functions

## Input

### omrs ( .jpg/.jpeg (prefer) or .png )

* scanned omr sheet of 90 and 190 mcqs (id number is mandatory in omrs)

### students.xlsx (Sheet1)

| A | B |
| :-------------: | :-------------: |
| id | name |
| blank line | blank line |
| A001 | Abcd Stuv |
| J124 | Cdef Ghijk |

### answers.xlsx (Sheet1)

| A | B |
| :-------------: | :-------------: |
| A | single choice |
| ACD | multiple choice |
| A/D/B | either A or D or B  |
| G | grace |
|  | blank = grace |

## Output

### results.docx (exam-name_exam-date.docx)

* Header + Footer (important name, exam, current-date, link)
* Exam name, Exam date, total-marks
* Result Analysis Report by Marks
* Result Analysis Report by Section (optional functionality)
* Results for Individual Students
* Checked OMRs Of Individual Students

### students.xlsx (exam-name_exam-date)

* you can add absent students further but they won't get actual rank, instead process whole exam again.

| A | B |
| :-------------: | :-------------: |
| exam-name | exam-date |
| id | obtained marks |
| A001 | 211 |
| J124 | 160 |

*thank you*
