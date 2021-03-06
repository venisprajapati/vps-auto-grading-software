from services.make_result import Result
from services.make_excel_result import MakeExcelResult
from services.make_result_documents import ResultDocument


# This file contains code of Making final result files that is exam_date.docx and adding new workbook to students.xlsx file./

def MakeFinalResults(exam_name, exam_date, total_mcqs, positive_marks, negative_marks, section=False, section_1_name='', section_2_name='', section_3_name='', section_1=0, section_2=0, section_3=0):

    e_n = str(exam_name)
    e_d = str(exam_date)

    t_m = int(total_mcqs)
    p_m = int(positive_marks)
    n_m = float(negative_marks) if str(
        negative_marks).__contains__('.') else int(negative_marks)
    # print(n_m)

    t_marks = t_m*p_m

    sec_1_n = str(section_1_name)
    sec_2_n = str(section_2_name)
    sec_3_n = str(section_3_name)

    s_1 = section_1
    s_2 = section_2
    s_3 = section_3

    if (section):
        result, omrs = Result(t_m, positive_=p_m, negative_=n_m, section=True,
                              section_1=s_1, section_2=s_2, section_3=s_3)

    else:
        result, omrs = Result(t_m, positive_=p_m, negative_=n_m)

    students = MakeExcelResult(results=result, name=e_n, date=e_d)

    ResultDocument(exam_name_=e_n, exam_date_=e_d, section_=section,
                   results=result, omr_s_=omrs, students=students, total_marks=t_marks, section_1_n=sec_1_n, section_2_n=sec_2_n, section_3_n=sec_3_n)
