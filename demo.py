from docx import Document

def print_paragraph_by_heading(docx_file, target_heading):
    document = Document(docx_file)
    for paragraph in document.paragraphs:
        if paragraph.style.name == "Heading 1" and paragraph.text == target_heading:
            # Print the heading
            print(paragraph.text)
            
            # Print the following paragraph
            next_paragraph = paragraph
            while True:
                next_paragraph = next_paragraph._element.getnext()
                if next_paragraph is None or next_paragraph.tag.endswith('p'):
                    break
                print(next_paragraph.text)

# Example usage
docx_file = "your_document.docx"
target_heading = "Your Heading"
print_paragraph_by_heading(docx_file, target_heading)
