try:
    from reportlab.lib.pagesizes import A4  # type: ignore
    from reportlab.platypus import (  # type: ignore
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table
    )
    from reportlab.lib.styles import getSampleStyleSheet  # type: ignore
except ImportError as e:
    raise ImportError("reportlab is not installed. Install it with: pip install reportlab") from e


def generate_report(
    filename,
    email_data,
    risk,
    ips,
    urls,
    geolocation
):

    output = (
        "reports/"
        + filename
        + "_forensic_report.pdf"
    )

    document = SimpleDocTemplate(
        output,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Email Forensic Investigation Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"<b>Subject:</b> "
            f"{email_data['subject']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Sender:</b> "
            f"{email_data['from']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Risk Score:</b> "
            f"{risk['score']}/100",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Classification:</b> "
            f"{risk['classification']}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "<b>Detected Indicators</b>",
            styles["Heading2"]
        )
    )

    for reason in risk["reasons"]:

        elements.append(
            Paragraph(
                "• " + reason,
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "<b>Observed IP Addresses</b>",
            styles["Heading2"]
        )
    )

    for ip in ips:

        elements.append(
            Paragraph(
                ip,
                styles["Normal"]
            )
        )

    elements.append(
        Paragraph(
            "<b>URLs</b>",
            styles["Heading2"]
        )
    )

    for url in urls:

        elements.append(
            Paragraph(
                url,
                styles["Normal"]
            )
        )

    document.build(elements)

    return output