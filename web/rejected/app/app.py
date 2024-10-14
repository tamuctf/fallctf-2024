from flask import Flask, request, render_template
import subprocess
import requests
import os
import uuid
import shutil

app = Flask(__name__)

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN") 
app.secret_key = uuid.uuid4().hex


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/apply', methods=['POST'])
def apply():
    name = request.form['name']
    email = request.form['email']
    experience = request.form['experience']
    skills = request.form['skills']

    rid = uuid.uuid4().hex
    user_dir = os.path.join('/tmp/user_files', rid)

    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    did = uuid.uuid4().hex
    latex_filename = f'rejection_letter_{did}.tex'
    pdf_filename = f'rejection_letter_{did}.pdf'
    
    # Create LaTeX content
    latex_content = f"""
    \\documentclass{{letter}}
    \\usepackage{{hyperref}}
    \\signature{{HR Department}}
    \\address{{TAMU Cybersecurity Center\\\\College Station, TX}}
    \\begin{{document}}

    \\begin{{letter}}{{{name}\\\\{email}}}
    \\opening{{Dear {name},}}

    We regret to inform you that your application for the position of TAMUCTF Developer has been unsuccessful.

    While we appreciate your {experience} years of experience and skills in {skills}, we have decided to move forward with other candidates whose qualifications more closely match our current needs.

    We wish you the best in your future endeavors.
    \\closing{{Sincerely,}}
    \\end{{letter}}

    \\end{{document}}
    """
    
    with open(os.path.join(user_dir, latex_filename), 'w') as f:
        f.write(latex_content)
    
    # Compile LaTeX to PDF
    subprocess.run(['pdflatex', '-output-directory', user_dir, os.path.join(user_dir, latex_filename)])

    try:
        r = send_email(email, name, os.path.join(user_dir, pdf_filename))
        shutil.rmtree(user_dir)
    except:
        shutil.rmtree(user_dir)
        return "An error occurred while processing your application."

    if r.status_code == 200:
        return "Thank you for your application. Check your email, we will be in touch soon."
    else:
        return r.text


def send_email(recipient, name, pdf_path):
    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        files=[("attachment", ("rejection_letter.pdf", open(pdf_path, "rb").read()))],
        data={"from": f"HR Department <mailgun@{MAILGUN_DOMAIN}>",
              "to": [recipient, f"YOU@{MAILGUN_DOMAIN}"],
              "subject": "Application Status Update",   
              "text": f"Dear {name},\n\nPlease find attached the status of your application.\n\nBest regards,\nHR Department"})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)
