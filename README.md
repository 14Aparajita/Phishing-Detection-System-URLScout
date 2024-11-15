# 🌐 Phishing-Detection-System-URLScout


# 🌐 Phishing Detection System - URLScout

**URLScout** is an advanced **Phishing Detection System** that helps users identify fraudulent websites attempting to steal personal information. This project was developed as part of my B.Tech minor project in the 3rd year of Computer Science. Using machine learning, URLScout analyzes URLs in real-time to determine if they are potentially malicious.

---

## 🚀 Project Overview

Phishing attacks are a major cybersecurity threat affecting millions of users globally. **URLScout** aims to mitigate this risk by providing a user-friendly tool to assess URLs before visiting them.

The system employs a **Multi-Layer Perceptron (MLP)** model trained on a dataset of **450,000 URLs**, which are categorized as legitimate or phishing. Key features extracted include:

- **URL Length**: Helps detect overly long or suspicious URLs.
- **Hostname Length**: Identifies suspiciously long hostnames.
- **Entropy**: Measures randomness, flagging obfuscated URLs.
- **Digit Proportion**: High digit counts can indicate phishing attempts.
- **Suspicious Keywords**: Identifies keywords like "login" or "update" that are common in phishing.

---

## ✨ Features

- **Real-Time Prediction**: Instant analysis of submitted URLs.
- **User-Friendly Interface**: Clean and simple design for easy navigation.
- **Sophisticated ML Model**: Uses an advanced MLP for accurate predictions.
- **Enhanced Security**: Helps users avoid phishing attacks and protect their data.

---

## 💻 Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Flask templates)
- **Backend**: Python (Flask framework)
- **Machine Learning**: TensorFlow/Keras (MLP model)
- **Data Processing**: Pandas, NumPy
- **Deployment**: Flask (Local server)

---

## 📊 Dataset

The model was trained on a dataset containing **450,000 URLs**, both legitimate and phishing. Feature extraction and data preprocessing were key steps, and imbalanced data was handled using **SMOTE** (Synthetic Minority Over-sampling Technique).

---

## 📈 How It Works

1. **Submit a URL**: Users enter the URL they want to check.
2. **Feature Extraction**: The system analyzes various URL attributes.
3. **Prediction**: The MLP model evaluates the features to classify the URL.
4. **Result Display**: The system provides a risk score indicating if the URL is safe or potentially harmful.

---

## 🛠️ Installation

To set up and run this project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/username/URLScout.git

# Navigate to the project directory
cd URLScout

# Install the required dependencies
pip install -r requirements.txt

# Run the Flask app
flask run
```

Access the application at **http://127.0.0.1:5000** in your browser.

---

## 📈 Results

The MLP model demonstrates high accuracy in detecting phishing URLs, making it a reliable tool for online security. The real-time analysis helps users make informed decisions before clicking on unknown links.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Submit a pull request.

---

## 📧 Contact

If you have any questions or feedback, please reach out:

- **Email**: aparajitavaish@gmail.com
- **GitHub**: [AparajitaVaish](https://github.com/14Aparajita)

---


---
