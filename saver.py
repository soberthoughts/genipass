import csv
import os
from datetime import datetime
import pyperclip  # For copying to clipboard

DATA_FILE = "passwords.csv"


def save_to_database(password):
    """Save the password to a CSV file with a timestamp."""
    # Check if the file exists
    file_exists = os.path.isfile(DATA_FILE)

    # Open the CSV file in append mode
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header if file doesn't exist
        if not file_exists:
            writer.writerow(["Password", "Copied On"])

        # Avoid duplicate passwords by checking file content
        with open(DATA_FILE, mode="r") as read_file:
            existing_passwords = [row[0] for row in csv.reader(read_file)]
            if password in existing_passwords:
                print("Password already exists in the database.")
                return

        # Write the new password with a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([password, timestamp])
        print("Password saved to database!")
