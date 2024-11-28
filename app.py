from flask import Flask, redirect, url_for, render_template, session, request, jsonify, flash, send_from_directory
from flask import Flask
from werkzeug.utils import secure_filename
import os
from model import LogReview


app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='static')
app.config["SECRET_KEY"]='pfe'
app.debug = True

@app.route('/',methods=['GET','POST'])
def review():
    if request.method == 'POST':
        f = request.files['file']
        fn = f'static/downloads/{secure_filename(f.filename)}'
        f.save(fn)
        logReview = LogReview(fn,'static/patterns.json')
        logReview.review()
        session['findings'] = logReview.findings
        return redirect(url_for('findings'))
    return render_template('review.html')

@app.route('/findings',methods=['GET'])
def findings():
    findings = session.get('findings')
    if len(findings)==0:
        findings.append({'type':'none','lineno':0, 'line':"No issues detected"})
    return render_template('findings.html',findings=findings)
@app.route('/info',methods=['GET'])
def info():
    patterns = LogReview.display_patterns('static/patterns.json')
    return render_template('info.html',patterns=patterns)

if __name__ == '__main__':
    app.run()
