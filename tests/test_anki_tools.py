# test_anki_tools.py
import pytest
import tempfile
from pathlib import Path
import sys
import os
# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import anki_tools

@pytest.fixture
def test_file():
    # 准备测试文件
    temp_dir = tempfile.TemporaryDirectory()
    file_path = Path(temp_dir.name) / "test.md"
    
    test_content = """# 标题
    
<!--ID: 1234567890-->
内容行1

内容行2



结尾行"""
    file_path.write_text(test_content, encoding='utf-8')
    
    yield file_path  # 提供测试文件给测试函数
    
    # 清理
    temp_dir.cleanup()

def test_remove_anki_id(test_file):
    pattern = r'<!--ID: \d+-->\n'
    result_file = anki_tools.remove_anki_id(test_file, pattern)
    
    assert result_file.exists()
    content = result_file.read_text(encoding='utf-8')
    assert '<!--ID:' not in content

def test_normalize_empty_lines(test_file):
    result_file = anki_tools.normalize_empty_lines(test_file)
    
    assert result_file.exists()
    content = result_file.read_text(encoding='utf-8')
    assert '\n\n\n\n' not in content  # 不应该有三个连续空行，也就是四个换行符