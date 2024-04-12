from docx import Document

def read_heading_content(docx_path, target_heading):
    doc = Document(docx_path)
    found_heading = False
    content = []

    for paragraph in doc.paragraphs:
        if paragraph.style.name.startswith('Heading') and paragraph.text == target_heading:
            found_heading = True
            continue
        
        if found_heading:
            if paragraph.style.name.startswith('Heading'):
                break
            content.append(paragraph.text)
    
    return '\n'.join(content)

# Example usage
docx_file = "your_document.docx"
target_heading = "Your Target Heading"
heading_content = read_heading_content(docx_file, target_heading)
print(heading_content)
