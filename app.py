import os
import tempfile

import streamlit as st
import pandas as pd

from email_parser import parse_email
from header_analyzer import analyze_headers

from ioc_extractor import (
    extract_ips,
    extract_urls,
    extract_domains
)

from threat_detector import (
    analyze_content,
    analyze_urls,
    predict_email
)

from geoip import geolocate_ip

from risk_engine import calculate_risk

from graph_analysis import create_email_graph
from graph_visualizer import graph_to_plotly

from database import (
    create_database,
    save_case
)

from report_generator import (
    generate_report
)


st.set_page_config(
    page_title="AI Email Forensics",
    page_icon="🛡️",
    layout="wide"
)


create_database()


st.title(
    "🛡️ AI-Powered Email Threat Detection"
)

st.subheader(
    "GeoLocation & Forensic Intelligence Platform"
)


uploaded_file = st.file_uploader(
    "Upload suspicious .eml file",
    type=["eml"]
)


if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".eml"
    ) as temp:

        temp.write(
            uploaded_file.getvalue()
        )

        temp_path = temp.name


    email_data = parse_email(
        temp_path
    )


    # Header analysis

    header_data = analyze_headers(
        email_data
    )


    # IOC extraction

    ips = extract_ips(
        email_data["headers"]
    )

    urls = extract_urls(
        email_data["body"]
    )

    domains = extract_domains(
        urls
    )


    # Content analysis

    content_analysis = analyze_content(
        email_data["subject"],
        email_data["body"]
    )


    # URL analysis

    url_analysis = analyze_urls(
        urls
    )


    # ML

    combined_text = (
        email_data["subject"]
        + "\n"
        + email_data["body"]
    )

    ml_result = predict_email(
        combined_text
    )


    # Risk calculation

    suspicious_domain = False

    if domains:

        sender_domain = (
            email_data["from"]
            .split("@")[-1]
            .replace(">", "")
        )

        for domain in domains:

            if domain.lower() != sender_domain.lower():

                suspicious_domain = True


    risk = calculate_risk(
        content_analysis,
        url_analysis,
        header_data,
        suspicious_domain
    )


    # Display basic information

    st.header("📧 Email Information")


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            "**From:**",
            email_data["from"]
        )

        st.write(
            "**To:**",
            email_data["to"]
        )

        st.write(
            "**Reply-To:**",
            email_data["reply_to"]
        )


    with col2:

        st.write(
            "**Subject:**",
            email_data["subject"]
        )

        st.write(
            "**Return-Path:**",
            email_data["return_path"]
        )


    st.divider()


    # Threat score

    st.header("🚨 Threat Assessment")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Risk Score",
            f"{risk['score']}/100"
        )


    with col2:

        st.metric(
            "Classification",
            risk["classification"]
        )


    with col3:

        st.metric(
            "AI Prediction",
            ml_result["label"]
        )


    st.write(
        "AI phishing probability:",
        f"{ml_result['probability'] * 100:.2f}%"
    )


    # Authentication

    st.header(
        "🔐 Email Authentication"
    )


    auth_df = pd.DataFrame({

        "Mechanism": [
            "SPF",
            "DKIM",
            "DMARC"
        ],

        "Result": [
            header_data["spf"],
            header_data["dkim"],
            header_data["dmarc"]
        ]
    })


    st.dataframe(
        auth_df,
        use_container_width=True
    )


    # IOCs

    st.header(
        "🔎 Indicators of Compromise"
    )


    st.write("### IP Addresses")

    if ips:

        st.dataframe(
            pd.DataFrame({
                "IP": ips
            }),
            use_container_width=True
        )

    else:

        st.info(
            "No IP addresses extracted."
        )


    st.write("### URLs")

    if urls:

        st.dataframe(
            pd.DataFrame({
                "URL": urls
            }),
            use_container_width=True
        )

    else:

        st.info(
            "No URLs extracted."
        )


    # Geolocation

    st.header(
        "🌍 IP Geolocation"
    )


    geo_results = []


    for ip in ips:

        result = geolocate_ip(ip)

        geo_results.append(result)


    if geo_results:

        geo_df = pd.DataFrame(
            geo_results
        )

        st.dataframe(
            geo_df,
            use_container_width=True
        )


    # Threat reasons

    st.header(
        "⚠️ Detection Reasons"
    )


    for reason in risk["reasons"]:

        st.warning(reason)


    # Graph

    st.header(
        "🕸️ Infrastructure Relationship Graph"
    )


    graph = create_email_graph(
        email_data["from"],
        domains,
        ips,
        urls
    )


    figure = graph_to_plotly(
        graph
    )


    st.plotly_chart(
        figure,
        use_container_width=True
    )


    # Save case

    save_case(
        uploaded_file.name,
        email_data["from"],
        email_data["subject"],
        risk["score"],
        risk["classification"]
    )


    # Report

    st.header(
        "📄 Forensic Report"
    )


    if st.button(
        "Generate Forensic Report"
    ):

        os.makedirs(
            "reports",
            exist_ok=True
        )

        report = generate_report(
            uploaded_file.name,
            email_data,
            risk,
            ips,
            urls,
            geo_results
        )

        st.success(
            "Forensic report generated."
        )

        with open(
            report,
            "rb"
        ) as file:

            st.download_button(
                "Download Report",
                file,
                file_name=os.path.basename(
                    report
                ),
                mime="application/pdf"
            )