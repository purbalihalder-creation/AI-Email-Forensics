import sqlite3


def create_database():

    connection = sqlite3.connect(
        "forensics.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            filename TEXT,

            sender TEXT,

            subject TEXT,

            risk_score INTEGER,

            classification TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    connection.close()


def save_case(
    filename,
    sender,
    subject,
    risk_score,
    classification
):

    connection = sqlite3.connect(
        "forensics.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO cases
        (filename, sender, subject,
         risk_score, classification)

        VALUES (?, ?, ?, ?, ?)
    """, (
        filename,
        sender,
        subject,
        risk_score,
        classification
    ))

    connection.commit()

    connection.close()