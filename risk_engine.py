def calculate_risk(
    content_analysis,
    url_analysis,
    header_analysis,
    suspicious_domain=False
):

    score = 0
    reasons = []

    urgency = content_analysis["urgency_indicators"]

    credentials = content_analysis["credential_indicators"]

    financial = content_analysis["financial_indicators"]

    if urgency >= 2:

        score += 20
        reasons.append(
            "Urgency/social engineering indicators"
        )

    if credentials >= 2:

        score += 20
        reasons.append(
            "Credential harvesting indicators"
        )

    if financial >= 1:

        score += 15
        reasons.append(
            "Financial fraud indicators"
        )

    if len(url_analysis) > 0:

        score += 15
        reasons.append(
            "Suspicious URL detected"
        )

    if header_analysis["spf"] == "fail":

        score += 10
        reasons.append("SPF failure")

    if header_analysis["dkim"] == "fail":

        score += 10
        reasons.append("DKIM failure")

    if header_analysis["dmarc"] == "fail":

        score += 10
        reasons.append("DMARC failure")

    if suspicious_domain:

        score += 20
        reasons.append(
            "Potential lookalike/suspicious domain"
        )

    score = min(score, 100)

    if score >= 80:

        classification = "CRITICAL"

    elif score >= 60:

        classification = "HIGH"

    elif score >= 30:

        classification = "MEDIUM"

    else:

        classification = "LOW"

    return {
        "score": score,
        "classification": classification,
        "reasons": reasons
    }