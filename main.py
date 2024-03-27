import os
from docx import Document

# def read_docx(file_path):
#     doc = Document(file_path)
#     full_text = []
#     for para in doc.paragraphs:
#         full_text.append(para.text)
#     return '\n'.join(full_text)

# file_path = r'E:\python_project\python_docs\python_docs\todo.docx'
# text = read_docx(file_path)
# print(text)


# 888888888888888888888888888888888888

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

# =============================================================

# def extract_table_data(file_path):
#     doc = Document(file_path)
#     tables_data = []
#     for table in doc.tables:
#         table_data = []
#         for row in table.rows:
#             row_data = []
#             for cell in row.cells:
#                 row_data.append(cell.text.strip())
#             table_data.append(row_data)
#         tables_data.append(table_data)
#     return tables_data

# def print_table_data(tables_data):
#     for i, table_data in enumerate(tables_data):
#         print(f"Table {i+1}:")
#         for row in table_data:
#             print("\t".join(row))
#         print()


# file_path = r'E:\python_project\python_docs\python_docs\todo_table.docx'
# filename = os.path.basename(file_path)
# print("Filename:", filename)
# tables_data = extract_table_data(file_path)
# print_table_data(tables_data)
# ++++++++++++++++++++++++++++++++++++++++++++++++

# def extract_table_column_names(file_path, keyword):
#     doc = Document(file_path)
#     for para in doc.paragraphs:
#         if keyword in para.text:
#             column_names = []
#             for table in doc.tables:
#                 if len(table.rows) > 0:
#                     first_row = table.rows[0]
#                     for cell in first_row.cells:
#                         column_names.append(cell.text.strip())
#                     break
#             return column_names

# file_path = r'E:\python_project\python_docs\python_docs\todo_table.docx'
# filename = os.path.basename(file_path)
# print("Filename>>>>>>>>>>>>>>>:", filename)
# first_value = filename.split('_')[0]
# print('first_value>>>>', first_value)
# keyword = 'Applying K-means with no. clusters = 7'
# column_names = extract_table_column_names(file_path, keyword)
# print("Table Column Names:", column_names)

# from docx import Document

def read_docx_table(docx_file):
    doc = Document(docx_file)
    table = doc.tables[0]  # Assuming there is only one table in the document
    data = []
    for row in table.rows:
        row_data = []
        for cell in row.cells:
            row_data.append(cell.text)
        data.append(row_data)
    return data

if __name__ == "__main__":
    docx_file = r'E:\python_project\python_docs\python_docs\todo_table.docx' 
    table_data = read_docx_table(docx_file)
    for row in table_data:
        print(row)
