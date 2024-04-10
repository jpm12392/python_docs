from docx import Document

def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

file_path = 'path_to_your_file.docx'
content = read_docx(file_path)
print(content)