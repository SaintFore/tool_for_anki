"""
文件操作函数

包含添加标签等文件操作功能。
"""
import sys
from pathlib import Path
# 添加项目根目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tool_for_anki.core.anki_tools import normalize_empty_lines



def change_brackets(file_path):
    """
    替换文件中的中括号，防止Obsidian识别为链接

    Args:
        file_path: 文件路径

    Returns:
        文件路径或None(处理失败时)
        处理后的行列表
    """
    try:
        path = Path(file_path)

        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        handled_lines = []
        for line in lines:
            if line.strip() == "":
                handled_lines.append("\n")
            else:
                line = line.replace("[", "【").replace("]", "】")
                handled_lines.append(line)
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(handled_lines))
        return path, handled_lines
    except Exception as e:
        print(f"处理文件{file_path}时出错: {e}")
        return None


def add_tag(file_path, tag):
    """
    添加标签到文件中

    Args:
        file_path: 文件路径
        tag: 要添加的标签

    Returns:
        文件路径或None(处理失败时)
    """

    
    # print(path)
    try:
        path = normalize_empty_lines(file_path)
        path,lines = change_brackets(path)

        sign = 0
        handle = []

        for line in lines:
            if line.strip() == "":
                sign += 1
                handle.append(line)
            elif sign == 2 and line.strip() != "":
                if '#' not in line:
                    line = line.strip() + f" #{tag}\n"
                sign = 0
                handle.append(line)
            else:
                sign = 0
                handle.append(line)

        # new_path = path.with_stem(f"{path.stem}_tagged")
        # with open(new_path, "w", encoding="utf-8") as file:
        #     file.writelines(handle)
        # return new_path

        # 直接覆盖原文件
        with open(path, "w", encoding="utf-8") as file:
            file.writelines(handle)
        return path
    except Exception as e:
        print(f"处理文件{file_path}时出错: {e}")
        return None


if __name__ == "__main__":
    test_file = "en.md"
    test_tag = "Lcard"
    result = add_tag(test_file, test_tag)
    if result:
        print(f"标签添加成功，文件路径: {result}")
    else:
        print("标签添加失败")