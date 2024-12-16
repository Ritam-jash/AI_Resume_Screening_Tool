from app.utils.nlp_utils import analyze_job_description

sample_job_description = """
We are looking for a Software Developer skilled in Python, machine learning, and Git.
The ideal candidate should have experience in using Docker, and knowledge of Flask and Java is a plus.
"""

sample_resume_text = """
John Doe
Software Developer
johndoe@example.com

Objective:
Seeking a challenging role in software development where I can apply my skills in Python and machine learning.

Education:
- B.Tech in Computer Science, University XYZ (2022)

Experience:
- Software Engineer Intern at ABC Corp (June 2021 - August 2021)
- Worked on various Python projects and learned about machine learning algorithms.

Skills:
- Programming Languages: Python, Java, C++
- Tools: Git, Docker, PyCharm
- Frameworks: Flask, Django
"""

def test_analyze_job_description():
    result = analyze_job_description(sample_job_description, sample_resume_text)
    print("Matched Skills:", result["matched_skills"])
    print("All Resume Skills:", result["all_resume_skills"])

if __name__ == "__main__":
    test_analyze_job_description()
