from docx import Document

def find_heading(document, heading_text):
    for paragraph in document.paragraphs:
        if paragraph.style.name.startswith('Heading'):
            if paragraph.text == heading_text:
                return paragraph

    return None

def main():
    docx_file = r'E:\python_project\python_docs\python_docs\demo.docx'
    heading_text_to_find = 'HELO'  # Replace with the heading text you want to find

    doc = Document(docx_file)
    heading_paragraph = find_heading(doc, heading_text_to_find)

    if heading_paragraph:
        print("Heading found:")
    else:
        print("Heading not found.")

if __name__ == "__main__":
    main()