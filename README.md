# 🎴 Anki 笔记处理工具

![版本](https://img.shields.io/badge/版本-0.3.0-blue) ![Python版本](https://img.shields.io/badge/Python-3.10-green) ![许可证](https://img.shields.io/badge/许可证-MIT-orange)

📝 一个强大的工具，用于处理和优化 Anki 笔记文件。让你的笔记更加整洁有序！

## ✨ 主要功能

- 🧹 **移除 Anki ID 标记** - 清理笔记中不需要的 ID 标记
- 📏 **规范化空行** - 自动调整文档空行，保持格式一致
- 🏷️ **添加标签** - 在段落后自动添加标签，便于分类管理
- 🖱️ **拖放操作** - 简单拖放文件即可处理，无需复杂操作

## 🛠️ 技术栈

- 💻 Python 3.10+
- 🎨 CustomTkinter - 美观的现代GUI框架
- 🔄 TkinterDnD2 - 拖放功能支持

## 📥 安装

### 方法一：下载可执行文件

1. 前往 [Releases](https://github.com/yourusername/tool_for_anki/releases) 页面
2. 下载最新的 `Anki笔记处理工具.zip` 文件
3. 解压后直接运行 `Anki笔记处理工具.exe`

### 方法二：从源码安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/tool_for_anki.git
cd tool_for_anki

# 安装依赖
pip install -r requirements.txt

# 运行应用
python main.py
```

## 📚 使用方法

### 启动应用

```bash
python main.py
```

### 使用界面

1. 🔄 **标准化笔记**：
   - 切换到"标准化"选项卡
   - 将文件拖放到指定区域
   - 点击"标准化文件"按钮

2. 🏷️ **添加标签**：
   - 切换到"添加标签"选项卡
   - 输入想要添加的标签（不需要输入#符号）
   - 将文件拖放到指定区域
   - 点击"添加标签"按钮

## 🔍 功能说明

### 移除 Anki ID

移除形如 `<!--ID: 1234567890-->` 的 Anki ID 标记。

### 规范化空行

调整文档中的空行，使文档格式统一：
- 单个空行会被调整为两个空行
- 多个连续空行会被规范为两个空行

### 添加标签

在两个空行后的段落自动添加标签，格式为 `#标签名`。

## 📁 项目结构

```
tool_for_anki/
├── tool_for_anki/          # 主包
│   ├── core/               # 核心功能
│   │   ├── anki_tools.py   # Anki笔记处理
│   │   └── add_tag.py      # 标签添加功能
│   └── gui/                # 图形界面
│       └── app.py          # GUI应用
├── tests/                  # 测试文件
├── main.py                 # 程序入口
└── README.md               # 说明文档
```

## 🧪 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_anki_tools.py
```

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详情请参阅 LICENSE 文件。

## 💖 致谢

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - 提供现代化GUI组件
- [TkinterDnD2](https://github.com/pmgagne/tkinterdnd2) - 提供拖放功能支持
- 所有贡献者和用户

---

📌 **注意**：此工具仅处理本地Anki笔记文件，不直接与Anki数据库交互。

---

💡 如有问题或建议，欢迎 [提交Issue](https://github.com/yourusername/tool_for_anki/issues)