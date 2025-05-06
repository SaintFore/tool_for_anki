import re

def remove_anki_id(file_name, pattern):
    """
    移除 Anki ID
    """
    # 读取文件内容
    file_path = file_name + '.md'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式替换 Anki ID
    new_content = re.sub(pattern, '', content)

    new_file_name = file_name + '_no_id'
    new_file_path = new_file_name + '.md'
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


pattern = r'<!--ID: \d+-->\n'
file_name = 'test'

remove_anki_id(file_name, pattern)
