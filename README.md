# Fake Profile Detector

## Overview
The Fake Profile Detector is a minimal web application built using Python and Flask. It allows users to upload a profile bio and an image to analyze whether the profile is likely to be fake or real. The application utilizes a pre-trained text classification model to evaluate the bio and performs basic validation on the uploaded image.

## Project Structure
```
fake-profile-detector/
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd fake-profile-detector
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**
   ```bash
   python app.py
   ```

2. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Upload Profile Information**
   - Enter the profile bio in the text area.
   - Upload an image file.
   - Click the submit button to analyze the profile.

4. **View Results**
   The application will display whether the profile is classified as "FAKE" or "REAL" based on the analysis of the bio text.

## Dependencies
- Flask==2.0.3
- transformers==4.11.3
- Pillow

## License
This project is licensed under the MIT License.