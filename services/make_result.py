import os
from services.scan_omr_sheet import ScanOmrs
from services.read_answer import ReadAnswer


def Result(total_mcqs, positive_=1, negative_=0, section=False, section_1=0, section_2=0, section_3=0):

    omrs = ScanOmrs(total_mcqs)
    answers = ReadAnswer(total_mcqs)

    ans_sheet = './uploads/answers.xlsx'
    os.remove(os.path.join(ans_sheet))

    data = []

    ans_length = len(answers)
    if (total_mcqs <= ans_length):
        mcq_to_check = total_mcqs
    else:
        mcq_to_check = ans_length

    for omr in omrs:
        dictionary = {
            'id': omr['id']
        }

        correct_ = []
        not_attempted_ = []
        incorrect_ = []

        for i in range(1, (mcq_to_check + 1)):
            if (answers[i] == 'G'):
                correct_.append(i)
            elif (omr[i] == ''):
                not_attempted_.append(i)
            elif (answers[i] == omr[i]):
                correct_.append(i)
            elif (answers[i].__contains__('/')):
                ans_split_string = (omr[i]).split('/')
                if (omr[i] in ans_split_string):
                    correct_.append(i)
                else:
                    incorrect_.append(i)
            else:
                incorrect_.append(i)

        dictionary['correct'] = correct_
        dictionary['correct_count'] = len(correct_)
        dictionary['not_attempted'] = not_attempted_
        dictionary['not_attempted_count'] = len(not_attempted_)
        dictionary['incorrect'] = incorrect_
        dictionary['incorrect_count'] = len(incorrect_)

        if (section):

            if (section_1 != 0 and section_1 < mcq_to_check and section_1 >= 1):
                dictionary['section_1'] = True
                correct_1_ = 0
                incorrect_1_ = 0
                for i in range(1, section_1 + 1):
                    if (i in dictionary['correct']):
                        # correct_1_.append(i)
                        correct_1_ += 1
                    elif (i in dictionary['incorrect']):
                        # incorrect_1_.append(i)
                        incorrect_1_ += 1
                dictionary['section_1_correct'] = correct_1_
                dictionary['section_1_incorrect'] = incorrect_1_
                dictionary['section_1_marks'] = (
                    correct_1_*positive_) + (incorrect_1_*negative_)

            if (section_2 != 0 and section_2 <= mcq_to_check and section_2 > section_1):
                dictionary['section_2'] = True
                correct_2_ = 0
                incorrect_2_ = 0
                for i in range(section_1 + 1, section_2 + 1):
                    if (i in dictionary['correct']):
                        # correct_2_.append(i)
                        correct_2_ += 1
                    elif (i in dictionary['incorrect']):
                        # incorrect_2_.append(i)
                        incorrect_2_ += 1
                dictionary['section_2_correct'] = correct_2_
                dictionary['section_2_incorrect'] = incorrect_2_
                dictionary['section_2_marks'] = (
                    correct_2_*positive_) + (incorrect_2_*negative_)

            if (section_3 != 0 and section_3 <= mcq_to_check and section_3 > section_2):
                dictionary['section_3'] = True
                correct_3_ = 0
                incorrect_3_ = 0
                for i in range(section_2 + 1, section_3 + 1):
                    if (i in dictionary['correct']):
                        # correct_3_.append(i)
                        correct_3_ += 1
                    elif (i in dictionary['incorrect']):
                        # incorrect_3_.append(i)
                        incorrect_3_ += 1
                dictionary['section_3_correct'] = correct_3_
                dictionary['section_3_incorrect'] = incorrect_3_
                dictionary['section_3_marks'] = (
                    correct_3_*positive_) + (incorrect_3_*negative_)

            positive_marks = dictionary['correct_count'] * positive_
            negative_marks = dictionary['incorrect_count'] * negative_

            dictionary['obtained_total_marks'] = positive_marks + \
                negative_marks

        else:

            positive_marks = dictionary['correct_count'] * positive_
            negative_marks = dictionary['incorrect_count'] * negative_

            dictionary['obtained_total_marks'] = positive_marks + \
                negative_marks

        data.append(dictionary)

    final_data = sorted(
        data, key=lambda marks: marks['obtained_total_marks'], reverse=True)

    for rank, data_0_ in enumerate(final_data, start=1):
        data_0_['rank'] = rank

    return final_data, omrs
