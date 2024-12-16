import unittest
from app.utils.ranker import calculate_match_score, rank_resumes

class TestRanker(unittest.TestCase):

    def setUp(self):
        self.sample_resume_text = """
        John Doe
        Software Developer
        johndoe@example.com
        Objective:
        Seeking a challenging role in software development where I can apply my skills in Python and
        machine learning.
        Education:
        - B.Tech in Computer Science, University XYZ (2022)
        Experience:
        - Software Engineer Intern at ABC Corp (June 2021 - August 2021)
        - Worked on Python and machine learning projects.
        Skills:
        - Python, Git, Docker, Flask
        """
        self.sample_job_description = """
        We are looking for a software developer with expertise in Python, Git, Docker, and Flask.
        Experience with machine learning is a plus.
        """

    def test_calculate_match_score(self):
        score = calculate_match_score(self.sample_resume_text, self.sample_job_description)
        self.assertGreater(score, 0, "Match score should be greater than 0")

    def test_rank_resumes(self):
        resumes = [self.sample_resume_text]
        job_desc = self.sample_job_description
        ranked_resumes = rank_resumes(resumes, job_desc)
        self.assertEqual(ranked_resumes[0][0], self.sample_resume_text)

if __name__ == "__main__":
    unittest.main()
