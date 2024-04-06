import csv
import fitz  # PyMuPDF

from variables import textbooks_data


def extract_bookmarks(pdf_path, csv_path, textbook):
    bookmarks = []
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through bookmarks
    for bookmark in pdf_document.get_toc():
        print(bookmark)
        name = bookmark[1]
        bookmarks.append({'Textbook': textbook, 'Name': name})

    # Write bookmarks to CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Textbook', 'Name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(bookmarks)


for t in textbooks_data:
    extract_bookmarks(t["pdf_path"], t["csv_path"], t["textbook"])
