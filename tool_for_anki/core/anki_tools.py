"""
Anki笔记工具函数

包含处理Anki笔记的函数，如移除ID、规范化空行等。
"""
import re
from pathlib import Path


def remove_anki_id(file_path, pattern):
    """
    移除 Anki ID，返回新文件路径

    Args:
        file_path: 文件路径
        pattern: 匹配Anki ID的正则表达式

    Returns:
        文件路径或None(处理失败时)
    """
    try:
        # 使用Path处理文件路径
        path = Path(file_path)
        # print(path)
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        # 使用正则表达式替换 Anki ID
        new_content = re.sub(pattern, "", content)

        # # 生成新文件路径
        # new_path = path.with_stem(f"{path.stem}_no_id")
        # with open(new_path, 'w', encoding='utf-8') as file:
        #     file.write(new_content)

        # return new_path

        # 直接覆盖原文件
        with open(path, "w", encoding="utf-8") as file:
            file.write(new_content)
        return path

    except Exception as e:
        print(f"处理文件{file_path}时出错: {e}")
        return None


def normalize_empty_lines(file_path):
    """
    将文件中的空行规范化为两个空行

    Args:
        file_path: 文件路径

    Returns:
        文件路径或None(处理失败时)
    """
    # 读取文件内容
    try:
        path = Path(file_path)
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        normalized_lines = []
        empty_line_count = 0

        for line in lines:
            line = line.rstrip("\n")
            if line == "":
                empty_line_count += 1
            else:
                if empty_line_count == 1:
                    normalized_lines.extend(["", ""])
                elif empty_line_count >= 2:
                    normalized_lines.extend(["", ""])

                empty_line_count = 0
                normalized_lines.append(line)

        # new_path = path.with_stem(f"{path.stem}_normalized")
        # with open(new_path, 'w', encoding='utf-8') as file:
        #     file.write('\n'.join(normalized_lines))

        # return new_path

        # 直接覆盖原文件
        with open(path, "w", encoding="utf-8") as file:
            file.write("\n".join(normalized_lines))
        return path

    except Exception as e:
        print(f"处理文件{file_path}时出错: {e}")
        return None


def remove_anki_id_and_normalize(path_file):
    """
    移除 Anki ID 并规范化空行

    Args:
        path_file: 文件路径

    Returns:
        文件路径或None(处理失败时)
    """
    pattern = r"<!--ID: \d+-->\n"
    new_file_path = remove_anki_id(path_file, pattern)
    if new_file_path:
        return normalize_empty_lines(new_file_path)
    return None
