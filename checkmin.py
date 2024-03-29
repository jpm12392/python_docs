from docx import Document

def read_docx_table(docx_file):
    doc = Document(docx_file)
    table = doc.tables[0]  # Assuming there is only one table in the document
    data = []
    for row in table.rows:
        row_data = []
        for cell in row.cells:
            if len(cell.text) < 3:
                minlen = f"{cell.text}  required is min 3 lenght"
                row_data.append(minlen)
            else:
                row_data.append(cell.text)
            
        data.append(row_data)
    return data

if __name__ == "__main__":
    docx_file = r'E:\python_project\python_docs\python_docs\demo.docx'
    table_data = read_docx_table(docx_file)
    for row in table_data[1:]:
        print(row)