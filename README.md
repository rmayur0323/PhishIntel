# 🔐 PhishIntel
The Phishing Website Detector is a lightweight, Python-based cybersecurity tool developed to identify and flag potentially dangerous phishing websites. It uses supervised machine learning models trained on real-world URL data to classify web addresses as either legitimate or phishing attempts. The project demonstrates the practical application of AI in cybersecurity and is designed to be educational, accessible, and extendable for research or real-world deployment.

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

**🚀 Installation**
🐍 Using Python:
```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
pip install -r requirements.txt
python app.py

