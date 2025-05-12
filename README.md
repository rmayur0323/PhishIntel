# 🔐 PhishIntel
**PhishIntel** is an AI-based Phishinng Website Detector cybersecurity tool designed to help users **identify whether a given URL or file is legitimate or a phishing attempt.** It leverages machine learning algorithms **to analyze structural and behavioral characteristics of URLs and files** to make real-time classification decisions. The project demonstrates the practical application of AI in cybersecurity and is designed to be educational, accessible, and extendable for research or real-world deployment.

**🧠 Key Features**

**🌐 URL-Based Phishing Detection**

*Analyzes URLs to detect suspicious characteristics (e.g., use of IPs, @, hyphens, abnormal length).

*Real-time classification as "Phishing" or "Legitimate".

*Uses interpretable features for transparency and trust.

**📊 ML Model Integration**

*Trained on over 11,000 labeled samples (from UCI/Kaggle).

*Supports Logistic Regression, Decision Tree, and Random Forest classifiers.

*Accuracy up to 96% with detailed precision/recall metrics.

**🖥️ Web-Based Interface**

*Simple input form for users to paste a URL.

*Displays result and highlights the features that triggered detection.

*Built for clarity, speed, and user-friendly experience.

**🛠️ Tech Stack**

| Tech          | Usage                                  |
|---------------|----------------------------------------|
| Python        | Core programming language             |
| Flask         | Backend server and API routes         |
| HTML/CSS      | Frontend form and output rendering     |
| Scikit-learn  | Model training and prediction          |
| Pickle        | Model serialization (`model.pkl`)      |

**👨‍💻 Project Structure**
csharp

Copy

Edit

phishing-detector/

├── app.py            # Flask app controller

├── model.pkl            # Trained ML model

├── url_extractor.py     # URL feature extraction script

├── templates/

│   └── index.html       # Web form interface

├── static/

│   └── style.css        # Basic CSS styling

├── requirements.txt     # Python dependencies

└── README.md            # Project documentation

**👩‍💻 Authors**

Mayur Koregaonkar

Anjali Yadav

**Team:-** Phishing Frenzy

**This project was developed as part of an academic research initiative focused on AI in cybersecurity.**

**📜 License**

This project is licensed under the MIT License.

See the LICENSE file for more details.


**🚀 Installation**
🐍 Using Python:
```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
pip install -r requirements.txt
python app.py



