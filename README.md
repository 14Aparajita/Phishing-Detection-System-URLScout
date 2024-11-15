# Phishing-Detection-System-URLScout
🌐 Phishing Detection System - URLScout
URLScout is an advanced Phishing Detection System designed to safeguard users from fraudulent websites that attempt to steal personal and sensitive information. Developed as a part of my B.Tech minor project (3rd year), this application leverages machine learning to identify and classify suspicious URLs with high accuracy.

🚀 Project Overview
Phishing attacks have become a significant cybersecurity concern, affecting millions of users worldwide. The URLScout project aims to address this issue by providing a real-time URL analysis tool. Users can simply paste a URL into the system, and it returns an immediate prediction of whether the link is potentially harmful.

The core of this system is a Multi-Layer Perceptron (MLP) model trained on a robust dataset containing over 450,000 URLs, classified as either legitimate or phishing. The model extracts and analyzes various features, such as:

URL Length: Longer URLs often indicate potential phishing attempts.
Hostname Length: Unusually long or complex hostnames are a red flag.
Entropy: Measures randomness; higher entropy may signal obfuscation tactics.
Digit Proportion: Phishing URLs often contain many digits.
Suspicious Keywords: Keywords like "login", "update", or "verify" can be signs of phishing.
✨ Features
Real-Time Prediction: Instantly analyzes URLs and provides a prediction score.
User-Friendly Interface: Simple and intuitive design for quick and easy usage.
Advanced Machine Learning: Utilizes a sophisticated MLP model for accurate predictions.
Protection Against Phishing: Helps users avoid phishing sites and protect their data.
💻 How It Works
Submit a URL: Enter the URL you want to check.
Feature Extraction: The system analyzes various characteristics of the URL.
Prediction: The MLP model evaluates the features and calculates the probability of the URL being malicious.
Result Display: Users receive a risk score indicating whether the URL is safe or suspicious.
🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript (Flask templates)
Backend: Python (Flask framework)
Machine Learning: TensorFlow/Keras (MLP model)
Data Processing: Pandas, NumPy
Deployment: Flask (Local server)
📊 Dataset
The model was trained on a comprehensive dataset of 450,000 URLs, which includes legitimate and phishing samples. Data preprocessing involved feature extraction and handling imbalanced data using techniques like SMOTE (Synthetic Minority Over-sampling Technique).

📈 Results
The MLP model achieved impressive accuracy in detecting phishing URLs, making it a reliable tool for enhancing online security. By analyzing URL patterns, structures, and other attributes, URLScout delivers real-time predictions with high precision.

🤝 Contributing
Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests. Let's work together to make the internet a safer place.

📧 Contact
For any questions or feedback, please contact me.

📝 License
