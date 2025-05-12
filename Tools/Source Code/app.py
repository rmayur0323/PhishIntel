from flask import Flask, render_template, request
import os
import PyPDF2
import google.generativeai as genai

app = Flask(__name__)

# Configure Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBIgf4L0lNEuqZE8bhDT9T492YPy8hXUao"  # Replace with your actual key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

ALLOWED_EXTENSIONS = {'pdf', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

def detect_scam_text(text):
    prompt = f"""
    You are an expert in scam detection. Analyze the following content and classify it as either:
    - Scam/Fake (with reason) 
    - Real/Legitimate

    Text:
    {text}

    Only return the classification and a brief explanation. No null or empty output.
    """
    response = model.generate_content(prompt)
    return response.text.strip() if response else "Detection failed."

def detect_url_category(url):
    prompt = f"""
    Analyze the following URL and classify it as one of:
    - Secure and Safe
    - Scam url
    - malware
    - defacement

    URL: {url}

    Return only one word (lowercase) as classification.
    """
    response = model.generate_content(prompt)
    return response.text.strip() if response else "Detection failed."

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict_url():
    url = request.form.get('url', '').strip()
    if not url.startswith(('http://', 'https://')):
        return render_template("index.html", input_url=url, predicted_class="Invalid URL format.")
    classification = detect_url_category(url)
    return render_template("index.html", input_url=url, predicted_class=f"🔍 URL classification: {classification}")

@app.route('/scam/', methods=['POST'])
def scam_detection():
    if 'file' not in request.files:
        return render_template("index.html", message="No file uploaded.")
    
    file = request.files['file']
    if not file or file.filename == '':
        return render_template("index.html", message="No selected file.")

    if not allowed_file(file.filename):
        return render_template("index.html", message="Invalid file format. Use PDF or TXT.")
    
    content = ''
    if file.filename.endswith('.pdf'):
        content = extract_text_from_pdf(file)
    elif file.filename.endswith('.txt'):
        content = file.read().decode('utf-8')

    if not content.strip():
        return render_template("index.html", message="File is empty or text not readable.")
    
    result = detect_scam_text(content)
    return render_template("index.html", message=result)

if __name__ == '__main__':
    app.run(debug=True)

