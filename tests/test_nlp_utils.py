import unittest
from app.utils.nlp_utils import extract_resume_sections, extract_keywords_from_job_description, analyze_job_description

class TestNLPUtils(unittest.TestCase):

    def setUp(self):
        # Sample resume text for testing
        self.sample_resume_text = """
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
        
        # Sample job description for testing
        self.sample_job_description = """
        We are looking for a Software Developer skilled in Python, machine learning, and Git.
        The ideal candidate should have experience in using Docker, and knowledge of Flask and Java is a plus.
        """

    def test_extract_resume_sections(self):
    # Check if skills, education, and experience are extracted correctly
        sections = extract_resume_sections(self.sample_resume_text)
        self.assertIn("skills", sections)
        self.assertIn("education", sections)
        self.assertIn("experience", sections)
        self.assertIn("Python", sections["skills"])

        # Check for the substring in the education section
        education_texts = " ".join(sections["education"])  # Join list into one string
        self.assertIn("B.Tech in Computer Science", education_texts)  # Substring check

        exprience_text = " ".join(sections["experience"])
        self.assertIn("Software Engineer Intern at ABC Corp", exprience_text)


    def test_extract_keywords_from_job_description(self):
        # Check if keywords from job description match resume skills
        skills_list = extract_resume_sections(self.sample_resume_text)["skills"]
        matched_keywords = extract_keywords_from_job_description(self.sample_job_description, skills_list)

        # Perform substring checks within the matched keywords
        matched_keywords_text = " ".join(matched_keywords)  # Combine list into single string for substring checking
        self.assertIn("Python", matched_keywords_text)
        self.assertIn("Git", matched_keywords_text)
        self.assertIn("Docker", matched_keywords_text)


    def test_analyze_job_description(self):
        # Check the overall analysis result
        result = analyze_job_description(self.sample_job_description, self.sample_resume_text)

        # Check for required keys in the result dictionary
        self.assertIn("matched_skills", result)
        self.assertIn("all_resume_skills", result)

        # Ensure there are matched skills in the output
        self.assertGreater(len(result["matched_skills"]), 0)  # Some matches should exist

        # Use substring checks for skills to handle format differences
        matched_skills_text = " ".join(result["matched_skills"])
        all_resume_skills_text = " ".join(result["all_resume_skills"])

        self.assertIn("Python", matched_skills_text)
        self.assertIn("Java", all_resume_skills_text)


if __name__ == "__main__":
    unittest.main()
