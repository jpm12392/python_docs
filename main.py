# from docx import Document

# def read_docx(file_path):
#     doc = Document(file_path)
#     full_text = []
#     for para in doc.paragraphs:
#         full_text.append(para.text)
#     return '\n'.join(full_text)

# file_path = r'E:\python_project\python_docs\python_docs\todo.docx'
# text = read_docx(file_path)
# print(text)


# from docx import Document

# def search_points_in_docx(file_path, keyword):
#     doc = Document(file_path)
#     points = []
#     for para in doc.paragraphs:
#         if keyword in para.text:
#             points.append(para.text)
#     return points

# file_path = r'E:\python_project\python_docs\python_docs\todo.docx'
# keyword = 'React Project Setup'  # Modify this with the keyword you want to search for
# found_points = search_points_in_docx(file_path, keyword)
# if found_points:
#     print("Points found containing '{}':".format(keyword))
#     for point in found_points:
#         print(point)
# else:
#     print("No points containing '{}' found.".format(keyword))


from docx import Document

def extract_table_data(file_path):
    doc = Document(file_path)
    tables_data = []
    for table in doc.tables:
        table_data = []
        for row in table.rows:
            row_data = []
            for cell in row.cells:
                row_data.append(cell.text.strip())
            table_data.append(row_data)
        tables_data.append(table_data)
    return tables_data

def print_table_data(tables_data):
    for i, table_data in enumerate(tables_data):
        print(f"Table {i+1}:")
        for row in table_data:
            print("\t".join(row))
        print()

file_path = r'E:\python_project\python_docs\python_docs\todo_table.docx'
tables_data = extract_table_data(file_path)
print_table_data(tables_data)