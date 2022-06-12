import os

def capitalize_file(file_path):
    file_name = os.path.join(file_path, 'mf1.txt')
    new_text = ""
    with open(file_name, 'r+', encoding='utf-8') as data:
        for line in data:
            new_text += line.capitalize()
        data.seek(0)
        data.write(new_text)
        