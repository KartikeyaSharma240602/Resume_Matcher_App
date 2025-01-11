from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import spacy
import os

# Initialize Flask app and spaCy model
app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def clean_and_extract_text(file_path):
    """
    Extracts and cleans text from a PDF file.
    """
    reader = PdfReader(file_path)
    text = " ".join(page.extract_text() for page in reader.pages)
    return " ".join(text.split())  # Remove extra spaces/newlines

def process_text_with_spacy(text):
    """
    Processes text with spaCy to extract meaningful keywords (lemmatized, lowercase).
    """
    doc = nlp(text)
    keywords = [
        token.lemma_.lower()  # Use lemmatized and lowercase words
        for token in doc
        if token.is_alpha and not token.is_stop
    ]
    return set(keywords)

def match_resume_to_job(resume_keywords, job_keywords):
    """
    Matches resume keywords to job keywords and calculates a match score.
    """
    common_keywords = resume_keywords.intersection(job_keywords)
    match_score = (len(common_keywords) / len(job_keywords)) * 100 if job_keywords else 0
    return match_score, common_keywords

def suggest_improvements(resume_keywords, job_keywords):
    """
    Suggests missing keywords from the job description that are not in the resume.
    """
    missing_keywords = job_keywords - resume_keywords
    return missing_keywords

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    # Handle file upload
    if 'resume' not in request.files:
        return "No file uploaded", 400
    file = request.files['resume']
    if file.filename == '':
        return "No file selected", 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Extract and clean resume text
    resume_text = clean_and_extract_text(file_path)
    resume_keywords = process_text_with_spacy(resume_text)

    # Get and process job description
    job_desc = request.form['job_desc']
    job_keywords = process_text_with_spacy(job_desc)

    # Calculate match score
    match_score, matched_keywords = match_resume_to_job(resume_keywords, job_keywords)

    # Suggest improvements
    missing_keywords = suggest_improvements(resume_keywords, job_keywords)

    return render_template(
        'result.html',
        match_score=match_score,
        matched_keywords=matched_keywords,
        missing_keywords=missing_keywords
    )

if __name__ == '__main__':
    app.run(debug=True)
