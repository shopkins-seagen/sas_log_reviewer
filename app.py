from flask import Flask, redirect, url_for, render_template, session, request, jsonify, flash, send_from_directory
from flask import Flask
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
        log = []
        raw = request.form.get('review')
        for n, l in enumerate(raw.splitlines()):
            log.append((n, l))
        reviewer = LogReview(log,'static/patterns.json')
        reviewer.review()
        session['findings']=reviewer.findings
        session['patterns']=reviewer.patterns
        return redirect(url_for('findings'))
    return render_template('review.html')

@app.route('/findings',methods=['GET'])
def findings():
    findings = session.get('findings')
    return render_template('findings.html',findings=findings)
@app.route('/info',methods=['GET'])
def info():
    patterns = LogReview.display_patterns('static/patterns.json')
    return render_template('info.html',patterns=patterns)

if __name__ == '__main__':
    app.run()
