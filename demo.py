from docx import Document

def print_heading_text(docx_file, heading_text):
    doc = Document(docx_file)
    for paragraph in doc.paragraphs:
        if paragraph.style.name.startswith("Heading") and heading_text in paragraph.text:
            print(paragraph.text)
            break
    else:
        print("Heading not found.")

# Usage example
print_heading_text("your_document.docx", "Your Heading")