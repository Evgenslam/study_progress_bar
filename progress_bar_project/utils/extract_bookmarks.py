import csv
import os

import fitz  # PyMuPDF


def extract_bookmarks(pdf_folder):
    root, _, files = next(os.walk(pdf_folder))

    for file in files:
        textbook = file.rstrip(".pdf")
        pdf_path = os.path.join(root, file)
        csv_path = os.path.join("../lesson_data/", f"{textbook}.csv")

        bookmarks = []
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

        # Iterate through bookmarks
        for bookmark in pdf_document.get_toc():
            print(bookmark)
            name = bookmark[1]
            bookmarks.append({"Textbook": textbook, "Name": name})

        # Create lesson_data folder if doesn't exist
        os.makedirs("../lesson_data", exist_ok=True)

        # Write bookmarks to CSV
        with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["Textbook", "Name"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(bookmarks)


extract_bookmarks("pdf_files/")
