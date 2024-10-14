from flask import Flask, request, render_template, session
import subprocess
import requests
import os
import uuid

app = Flask(__name__)

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN") 

app.secret_key = os.getenv("SECRET_KEY") 

# if not os.path.exists('/tmp/user_files'):
#     os.makedirs('/tmp/user_files')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply', methods=['POST'])
def apply():
    name = request.form['name']
    email = request.form['email']
    experience = request.form['experience']
    skills = request.form['skills']

    user_dir = os.path.join('/tmp/user_files', name)
    session['name'] = name


    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    unique_id = str(uuid.uuid4())[:8]
    latex_filename = f'rejection_letter_{unique_id}.tex'
    pdf_filename = f'rejection_letter_{unique_id}.pdf'
    
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

    return send_email(email, name, os.path.join(user_dir, pdf_filename))

def send_email(recipient, name, pdf_path):
    response = requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        files=[("attachment", ("rejection_letter.pdf", open(pdf_path, "rb").read()))],
        data={"from": f"HR Department <mailgun@{MAILGUN_DOMAIN}>",
              "to": [recipient, f"YOU@{MAILGUN_DOMAIN}"],
              "subject": "Application Status Update",   
              "text": f"Dear {name},\n\nPlease find attached the status of your application.\n\nBest regards,\nHR Department"})
    
    if response.status_code == 200:
        return "Thank you for your application. Check your email, we will be in touch soon."
    else:
        return response.text
        #return "An error occurred while processing your application."

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)