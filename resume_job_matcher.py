from PyPDF2 import PdfReader
import spacy

# Load spaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

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

if __name__ == "__main__":
    # Input: Path to resume and job description text
    resume_path = r"C:\Users\Kartikeya Sharma\OneDrive\Desktop\Sample_resume.pdf"
    job_desc = """
    Job Title: Senior Python Developer
    ...
    """  # Full job description here

    # Process the resume
    resume_text = clean_and_extract_text(resume_path)
    resume_keywords = process_text_with_spacy(resume_text)
    print("Resume Keywords:")
    print(resume_keywords)

    # Process the job description
    job_keywords = process_text_with_spacy(job_desc)
    print("\nJob Description Keywords:")
    print(job_keywords)

    # Match resume to job description
    match_score, matched_keywords = match_resume_to_job(resume_keywords, job_keywords)
    print(f"\nMatch Score: {match_score:.2f}%")
    print("Matched Keywords:")
    print(matched_keywords)

    # Suggest improvements
    missing_keywords = suggest_improvements(resume_keywords, job_keywords)
    print("\nSuggestions to Improve Resume Match:")
    print(f"Consider adding these keywords to your resume: {missing_keywords}")
