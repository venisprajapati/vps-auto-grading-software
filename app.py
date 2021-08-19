import os
import webbrowser
from waitress import serve
from threading import Timer
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, send_file, request
from services.final_result_ import MakeFinalResults


students_file_name_ = 'students.xlsx'

app = Flask(__name__)
UPLOAD_FOLDER_1 = './uploads'
app.config['UPLOAD_FOLDER_1'] = UPLOAD_FOLDER_1

UPLOAD_FOLDER_2 = './uploads/omrs'
app.config['UPLOAD_FOLDER_2'] = UPLOAD_FOLDER_2

RESULT_FOLDER = './result'
app.config['RESULT_FOLDER'] = RESULT_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        directory = './result'
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))

        file_students = request.files['students']
        if file_students:

            global students_file_name_
            students_file_name_ = secure_filename(file_students.filename)
            file_students.save(os.path.join(
                app.config['RESULT_FOLDER'], "students.xlsx"))

        file_answers = request.files['answers']
        if file_answers:
            file_answers.save(os.path.join(
                app.config['UPLOAD_FOLDER_1'], "answers.xlsx"))

        files_omr = request.files.getlist('omr-sheets')
        if files_omr:
            for file in files_omr:
                filename = secure_filename(file.filename)
                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER_2'], filename))

        if (request.form.getlist('section') == ['on']):

            s_1 = int(request.form['section-1']
                      ) if (request.form['section-1']) else 0
            s_2 = int(request.form['section-2']
                      ) if (request.form['section-2']) else 0
            s_3 = int(request.form['section-3']
                      ) if (request.form['section-3']) else 0
            MakeFinalResults(exam_name=request.form['examName'].strip(), exam_date=request.form['examDate'], total_mcqs=request.form['total-mcq'],
                             positive_marks=request.form['positive-marks'], negative_marks=request.form['negative-marks'], section=True, section_1=s_1, section_2=s_2, section_3=s_3)

        else:
            MakeFinalResults(exam_name=request.form['examName'].strip(), exam_date=request.form['examDate'], total_mcqs=request.form['total-mcq'],
                             positive_marks=request.form['positive-marks'], negative_marks=request.form['negative-marks'])

        return redirect('/result')

    elif request.method == "GET":
        return render_template('index.html')

    else:
        return "Error 404: Page Not Found"


@app.route('/result', methods=['GET', 'POST'])
def result():

    if request.method == 'POST':

        if request.form['submit_result'] == 'Download Results .docx':

            result_directory_ = './result'
            for file in os.listdir(result_directory_):
                if file.endswith('.docx'):
                    result_doc_ = file
            result = os.path.join(
                app.root_path, app.config['RESULT_FOLDER'], result_doc_)
            return send_file(result, mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document', download_name=result_doc_, as_attachment=True)

        if request.form['submit_result'] == 'Download Students .xlsx':

            result = os.path.join(
                app.root_path, app.config['RESULT_FOLDER'], 'students.xlsx')
            return send_file(result, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', download_name=students_file_name_, as_attachment=True)

    elif request.method == "GET":
        return render_template('result.html')

    else:
        return "Error 404: Page Not Found"


@app.route('/info', methods=['GET'])
def info():
    
    return render_template('info.html')


def open_web_browser():
    webbrowser.open_new('http://127.0.0.1:2102/')


# main function :- program execution will starts from here
if __name__ == '__main__':

    # Timer(1, open_web_browser).start()
    # serve(app, host="127.0.0.1", port=2102)

    app.run(port=2102, debug=True)
