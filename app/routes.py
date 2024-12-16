from flask import Blueprint, flash, render_template, request, redirect, url_for, send_from_directory
from . import db
from .utils.pdf_parser import extract_text_from_pdf
from .utils.ranker import rank_resumes
import os

# Define the Blueprint
main = Blueprint('main', __name__)

# Route for the home page
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('resumes')  # Get all uploaded files
        job_description = request.form.get('job_description', '')

        if not job_description.strip():
            flash('Please provide a job description.', 'error')
            return redirect(url_for('main.upload'))

        resume_scores = []

        os.makedirs('uploads', exist_ok=True)

        for uploaded_file in uploaded_files:
            if uploaded_file:
                save_path = os.path.join('uploads', uploaded_file.filename)
                uploaded_file.save(save_path)

                resume_text = extract_text_from_pdf(save_path)
                print(f"Resume Text ({uploaded_file.filename}): {resume_text[:500]}")  # Log first 500 characters

                score = rank_resumes([resume_text], [job_description])
                resume_scores.append({"name": uploaded_file.filename, "score": score[0]["score"]})

        return render_template('results.html', rankings=resume_scores)

    return render_template('upload_resume.html')


@main.route('/results')
def results():
    # Path to the latest uploaded resume
    upload_dir = 'uploads'
    uploaded_files = os.listdir(upload_dir)
    if not uploaded_files:
        return render_template('results.html', rankings=[], error="No files found in uploads directory.")
    
    latest_resume = os.path.join(upload_dir, uploaded_files[-1])  # Assume last uploaded file is the one we process

    # Read the job description from the saved file
    job_description_path = os.path.join(upload_dir, 'job_description.txt')
    if not os.path.exists(job_description_path):
        return render_template('results.html', rankings=[], error="Job description not found.")

    with open(job_description_path, 'r') as jd_file:
        job_description_text = jd_file.read()

    try:
        # Extract text from the uploaded resume
        resume_text = extract_text_from_pdf(latest_resume)  # Use existing function

        # Pass both the resume text and job description text to the ranking function
        rankings = rank_resumes(resume_text, [job_description_text])
    except Exception as e:
        return render_template('results.html', rankings=[], error=f"Error processing resume: {e}")

    return render_template('results.html', rankings=rankings)



@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(main.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


