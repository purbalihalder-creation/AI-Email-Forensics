import re


URGENCY_WORDS = [
    "urgent",
    "immediately",
    "act now",
    "within 24 hours",
    "suspended",
    "expire",
    "final warning"
]

CREDENTIAL_WORDS = [
    "password",
    "verify your account",
    "login",
    "username",
    "credential",
    "sign in"
]

FINANCIAL_WORDS = [
    "payment",
    "invoice",
    "bank account",
    "wire transfer",
    "gift card",
    "money"
]


def count_matches(text, words):

    text = text.lower()

    count = 0

    for word in words:

        if word.lower() in text:
            count += 1

    return count


def analyze_content(subject, body):

    text = subject + "\n" + body

    urgency = count_matches(text, URGENCY_WORDS)

    credentials = count_matches(text, CREDENTIAL_WORDS)

    financial = count_matches(text, FINANCIAL_WORDS)

    return {
        "urgency_indicators": urgency,
        "credential_indicators": credentials,
        "financial_indicators": financial
    }
def analyze_urls(urls):

    suspicious = []

    for url in urls:

        lower_url = url.lower()

        reasons = []

        if "@" in lower_url:
            reasons.append("Contains @ symbol")

        if len(url) > 100:
            reasons.append("Very long URL")

        if "login" in lower_url:
            reasons.append("Login-related URL")

        if "verify" in lower_url:
            reasons.append("Verification URL")

        if "password" in lower_url:
            reasons.append("Password-related URL")

        if reasons:

            suspicious.append({
                "url": url,
                "reasons": reasons
            })

    return suspicious

import joblib

model = joblib.load(
    "models/phishing_model.pkl"
)


def predict_email(text):

    prediction = model.predict([text])[0]

    probability = model.predict_proba(
        [text]
    )[0]

    phishing_probability = probability[1]

    if prediction == 1:

        label = "PHISHING"

    else:

        label = "LEGITIMATE"

    return {
        "label": label,
        "probability": float(
            phishing_probability
        )
    }