# Resume Screening Tool

## Description

The **Resume Screening Tool** is a web-based application designed to help recruiters, HR professionals, and hiring managers automate and streamline the process of analyzing resumes. This tool compares resumes against a given job description, calculates a match score based on skills and experience, and ranks the resumes accordingly. It supports **bulk resume uploads** and enables **job description input** to generate detailed, accurate results.

## Features

- **Bulk Resume Upload**: Upload multiple resumes at once and have them processed simultaneously.
- **Job Description Input**: Paste job description to match with resumes.
- **Resume Parsing**: Extracts key sections such as skills, experience, and education from uploaded resumes.
- **Match Score Calculation**: Calculates a score based on how closely a resume matches the job description.
- **Ranking System**: Displays a ranked list of resumes based on the score.

## Requirements

Before you begin, make sure to have the following installed:

- Python 3.x
- pip (Python's package installer)
- MySQL (if you're using it for your database)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/resume-screening-tool.git
cd resume-screening-tool
```

### 2. Set up a virtual environment:

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment:

For **Windows**:

```bash
.\venv\Scripts\activate
```

For **macOS/Linux**:

```bash
source venv/bin/activate
```

### 4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 5. Set up the environment variables:

Create a `.env` file in the root directory of the project and add the following variables:

```bash
DB_USERNAME=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_NAME=resume_db
```

### 6. Set up the database (optional if you're using a database):

Ensure you have a MySQL database set up with the appropriate user and password details. You can use the `SQLAlchemy` configurations for MySQL in `__init__.py`.

### 7. Run the application:

To start the Flask app, use the following command:

```bash
flask run
```

The application will be available at: `http://127.0.0.1:5000`

---

## Project Structure

Here is an overview of the project structure:

```
/resume_screening_tool
├── app/
│   ├── __init__.py            # Initializes Flask app
│   ├── routes.py              # Handles API routes for uploading and analyzing resumes
│   ├── models.py              # Database models (e.g., User, Resume, JobDescription)
│   ├── utils/
│   │   ├── pdf_parser.py      # Parses PDF resumes, extracts text
│   │   ├── nlp_utils.py       # NLP functions for extracting and processing text data
│   │   └── ranker.py          # Logic for ranking resumes based on job description
│   ├── templates/
│   │   ├── base.html          # Main layout
│   │   ├── index.html         # Home page with navigation
│   │   ├── upload_resume.html # Form for uploading resumes
│   │   └── results.html       # Display analyzed results and ranking
├── uploads/                   # Folder to store uploaded resumes
├── static/
│   ├── css/
│   │   └── style.css          # Custom styles
│   └── favicon.ico            # Application icon
├── tests/
│   ├── test_pdf_parser.py     # Unit tests for PDF parsing
│   ├── test_nlp_utils.py      # Tests for NLP functions
│   ├── test_ranker.py         # Tests for resume ranking logic
│   └── test_job_description.py # Tests for job description parsing and matching
├── config.py                  # Configuration file (e.g., database URI)
├── requirements.txt           # Project dependencies
├── run.py                     # Entry point to run the Flask app
└── README.md                  # Project documentation

```

---

## How to Use

### 1. **Upload Resumes:**
   - Navigate to the **Upload Resume** page.
   - Click **Choose Files** to select multiple resumes (PDF format).
   - Paste the **Job Description** for the position you’re hiring for.
   - Click **Submit**.

### 2. **View Results:**
   - After the resumes are uploaded and processed, you will be redirected to the **Resume Screening Results** page.
   - Here, you will see the resumes listed along with their respective **match scores**.
   - The higher the score, the better the resume matches the job description.

---

## Application Flow

1. **Resume Upload**: Users can upload multiple resume files via the `upload_resume.html` form.
2. **Job Description Input**: Users paste the job description into a text area on the same page.
3. **Text Extraction**: The resumes are processed using **PDF parsing** (via `pdf_parser.py`) and **OCR** (if the resume contains images) to extract text.
4. **NLP Analysis**: The text from the resume is analyzed to extract key sections (skills, experience, education) using **spaCy** (via `nlp_utils.py`).
5. **Ranking**: The tool compares the extracted skills and experience against the job description, calculating a match score using the **ranking logic** (via `ranker.py`).
6. **Results Display**: The results are displayed on the **results.html** page, showing each resume's name and score.

---

## Additional Notes

### **Technologies Used:**

- **Flask**: For building the web application.
- **spaCy**: For Natural Language Processing (NLP) to extract skills, experience, and education.
- **PyPDF2** & **pdf2image**: For extracting text from PDF files (and OCR for image-based PDFs).
- **SQLAlchemy**: For interacting with the database.
- **HTML/CSS**: For the frontend design.
- **JavaScript (optional)**: For enhancing frontend interactions.

### **Improvements in Future**:
- Adding support for other file formats (Word, DOCX, etc.).
- Enhanced NLP capabilities to handle more diverse job descriptions and resumes.
- More detailed ranking factors such as years of experience, job titles, etc.

---

## Running Tests

To ensure everything is working as expected, you can run the provided unit tests for different components:

```bash
pytest
```

The tests are located in the `/tests` folder and cover:
- PDF text extraction (`test_pdf_parser.py`).
- NLP functionalities (`test_nlp_utils.py`).
- Ranking logic (`test_ranker.py`).

---

## Contribution

Feel free to fork the repository, submit pull requests, or create issues for improvements. I’m open to suggestions and improvements. 

---

## Contact

For any questions or issues, feel free to reach out to me via LinkedIn: [https://www.linkedin.com/in/ritam-jash/].

---

### Notes:
- You can update sections like contact info, technologies used, etc., based on your personal information.
- The steps mentioned in the **How to Use** section are intended to guide users on how to interact with the application.#
