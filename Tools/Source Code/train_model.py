import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import time
import os  # For creating directories

# Start measuring time
start_time = time.time()

print("🔄 Loading dataset...")
df = pd.read_csv("malicious_phish.csv", nrows=5000)  # Read only the first 5000 rows
print("✅ Dataset loaded.")

# Prepare features and labels
X = df['url']
y = df['type']

print("🔄 Vectorizing URLs...")
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)
print("✅ Vectorization done.")

print("🔄 Training model (this may take time)...")
model = RandomForestClassifier()
model.fit(X_vectorized, y)
print("✅ Model trained!")

# Ensure the 'model' directory exists
os.makedirs('model', exist_ok=True)

print("💾 Saving model and vectorizer...")
joblib.dump(model, "model/url_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")
print("✅ Model and vectorizer saved successfully.")

# Time elapsed
end_time = time.time()
elapsed_time = end_time - start_time
print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")
