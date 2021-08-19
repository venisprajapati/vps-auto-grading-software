from openpyxl.reader.excel import load_workbook


def ReadAnswer(total_mcqs):
    wb = load_workbook('./uploads/answers.xlsx')

    sheet_ = wb['Sheet1']

    dictionary = {}

    ans_length = len(sheet_['A'])

    if (total_mcqs <= ans_length):

        for i in range(1, total_mcqs + 1):
            dictionary[i] = ((sheet_[f'A{i}'].value).strip()) if (
                sheet_[f'A{i}'].value) is not None else 'G'

    else:

        for i in range(1, ans_length + 1):
            dictionary[i] = ((sheet_[f'A{i}'].value).strip()) if (
                sheet_[f'A{i}'].value) is not None else 'G'

    wb.close()

    return dictionary
