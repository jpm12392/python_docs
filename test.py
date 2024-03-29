from docx import Document

def extract_table_data(docx_file):
    doc = Document(docx_file)
    
    table_data = []
    
    for table in doc.tables:
        table_dict = {}
        heading_row = None
        
        for i, row in enumerate(table.rows):
            if i == 0:  # First row usually contains headings
                heading_row = [cell.text.strip() for cell in row.cells]
            else:
                row_data = [cell.text.strip() for cell in row.cells]
                # Only include rows where all cells have data
                if all(row_data):
                    table_dict[tuple(heading_row)] = row_data
        
        if table_dict:
            table_data.append(table_dict)
    
    return table_data

# Example usage
docx_file = r'E:\python_project\python_docs\python_docs\demo.docx'
table_data = extract_table_data(docx_file)

# Printing the extracted data
for table_dict in table_data:
    for heading, records in table_dict.items():
        print("Heading:", heading)
        for record in records:
            print("Record:", record)
