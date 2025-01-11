**Resume and Job Description Matcher**
A Flask-powered web application that evaluates the compatibility between a resume and a job description. This tool leverages NLP techniques to extract, process, and compare keywords, providing a match score and actionable suggestions to optimize resumes for specific job descriptions.

**Features**
Resume Analysis: Extracts and cleans text from uploaded PDF resumes.
Keyword Matching: Identifies common keywords between resumes and job descriptions.
Match Scoring: Calculates a compatibility score based on keyword overlap.
Improvement Suggestions: Highlights missing keywords to enhance resume relevance.
Web Interface: User-friendly interface for uploading resumes and entering job descriptions.

**Technologies Used**
Backend: Python (Flask, spaCy, PyPDF2)
Frontend: HTML (templates provided by Flask)
NLP: spaCy for keyword extraction and lemmatization
Utilities: PyPDF2 for PDF text extraction

**Installation**
1. Clone the Repository
   ```
   git clone https://github.com/yourusername/resume-job-matcher.git
   cd resume-job-matcher
   ```

2. Set Up Virtual Environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate 
   ```

3. Install Dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run the Application
   ```
   python app.py
   ```

5. Access the Application Open your web browser and navigate to http://127.0.0.1:5000/

**Usage**
Upload a Resume: Use the interface to upload your resume in PDF format.
Enter Job Description: Paste the job description text into the provided field.
View Results: The app calculates a match score, displays common keywords, and suggests missing ones to improve the resume.

**Project Structure**
```
├── app.py                     # Flask application entry point
├── resume_job_matcher.py      # Core functions for text processing and matching
├── templates/
│   ├── index.html             # Main page for uploading resumes and entering job descriptions
│   ├── result.html            # Page displaying match results and suggestions
├── uploads/                   # Directory for storing uploaded resumes
└── requirements.txt           # List of Python dependencies
```

**Screenshots:**
![Screenshot 2025-01-11 200159](https://github.com/user-attachments/assets/bab5d259-5a10-41f4-bc04-fc5b0a3b59b1)

![Screenshot 2025-01-11 200222](https://github.com/user-attachments/assets/d46a9f82-5e6b-4da4-839b-192e34c6c7aa)

![Screenshot 2025-01-11 200242](https://github.com/user-attachments/assets/c6fba0e9-6c81-4c04-8ce6-d73ed8a7d173)

**Contributing**
Feel free to submit issues or pull requests to improve the project.

**License**
This project is licensed under the MIT License.
