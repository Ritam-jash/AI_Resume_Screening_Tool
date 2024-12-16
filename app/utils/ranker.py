from .nlp_utils import extract_keywords_from_job_description, extract_resume_sections, preprocess_text


def calculate_match_score(resume_text, job_description_text, skill_weight=0.7, experience_weight=0.3):
    resume_text = preprocess_text(resume_text)
    job_description_text = preprocess_text(job_description_text)

    resume_sections = extract_resume_sections(resume_text)
    skills_in_resume = resume_sections["skills"]
    experience_in_resume = resume_sections["experience"]

    job_keywords = extract_keywords_from_job_description(job_description_text, skills_in_resume)

    print("Processed Resume Text:", resume_text[:500])  # First 500 characters for debugging
    print("Job Keywords:", job_keywords)
    print("Skills in Resume:", skills_in_resume)

    skill_matches = [skill for skill in skills_in_resume if skill.lower() in job_keywords]
    skill_score = len(skill_matches) * skill_weight
    experience_score = len(experience_in_resume) * experience_weight

    print("Skill Matches:", skill_matches)
    print("Skill Score:", skill_score, "Experience Score:", experience_score)

    return skill_score + experience_score


def rank_resumes(resume_texts, job_description_texts):
    """
    Compare multiple resumes against job description(s) and rank them.

    Args:
        resume_texts (list): List of extracted text from the uploaded resumes.
        job_description_texts (list): List of job descriptions to compare against.

    Returns:
        list: Rankings with names and scores.
    """
    rankings = []

    for resume_text in resume_texts:  # Iterate through all resume texts
        scores = []
        for job_description in job_description_texts:
            # Calculate match score for each job description
            score = calculate_match_score(resume_text, job_description)
            scores.append(score)

        # Add the average score if multiple job descriptions are used
        average_score = sum(scores) / len(job_description_texts)
        rankings.append({"score": average_score})

    return rankings
