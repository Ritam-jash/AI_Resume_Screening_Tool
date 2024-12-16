import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to preprocess and normalize text
def preprocess_text(text):
    """Normalize and clean text for better processing."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
    return text


def extract_skills(text):
    skills_keywords = [
        "Python", "Java", "C++", "SQL", "JavaScript", "Git", "Docker", 
        "Machine Learning", "Flask", "Django", "MongoDB", "AngularJS", "React", "Kubernetes"
    ]
    pattern = re.compile(r'\b(?:' + '|'.join(re.escape(skill) for skill in skills_keywords) + r')\b', re.IGNORECASE)
    return pattern.findall(text)




# Extract education details from text
def extract_education(text):
    """
    Extract education-related information from the text.
    """
    education_keywords = ["B.Tech", "M.Tech", "Bachelor", "Master", "University", "College", "Degree"]
    extracted_education = []
    for sentence in text.splitlines():
        if any(keyword.lower() in sentence.lower() for keyword in education_keywords):
            extracted_education.append(sentence.strip())
    return extracted_education

# Extract experience details from text
def extract_experience(text):
    """
    Extract experience-related information from the text.
    """
    experience_keywords = ["experience", "intern", "worked at", "role", "position", "employed at"]
    extracted_experience = []
    for sentence in text.splitlines():
        if any(keyword.lower() in sentence.lower() for keyword in experience_keywords):
            extracted_experience.append(sentence.strip())
    return extracted_experience


def extract_resume_sections(text):
    skills = extract_skills(text)
    education = extract_education(text)
    experience = extract_experience(text)

    print("Extracted Skills:", skills)
    print("Extracted Education:", education)
    print("Extracted Experience:", experience)

    return {
        "skills": skills,
        "education": education,
        "experience": experience
    }




# Tokenize text into words for job description parsing
def tokenize_text(text):
    """
    Tokenizes the input text into words, removing stop words and punctuation.
    """
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    return tokens

# Extract keywords from job description
def extract_keywords_from_job_description(job_description, skills_list):
    """
    Extract keywords from the job description relevant to the given skills list.
    """
    job_tokens = tokenize_text(job_description)
    matched_keywords = [skill for skill in skills_list if skill.lower() in job_tokens]
    return matched_keywords

# Analyze job description to match resume skills
def analyze_job_description(job_description, resume_text):
    """
    Analyzes the job description and matches it against resume skills.
    """
    # Extract skills from resume
    resume_sections = extract_resume_sections(resume_text)
    resume_skills = resume_sections["skills"]

    # Match job description keywords with resume skills
    matched_skills = extract_keywords_from_job_description(job_description, resume_skills)

    return {
        "matched_skills": matched_skills,
        "all_resume_skills": resume_skills
    }
