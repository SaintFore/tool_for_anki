import customtkinter
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path
from anki_tools import remove_anki_id_and_normalize
from add_tag import add_tag


class App(customtkinter.CTk, TkinterDnD.DnDWrapper):
    def __init__(self):
        super().__init__()
        self.TkdndVersion = TkinterDnD._require(self)  # 初始化DnD功能

        self.title("Anki 笔记处理工具")
        self.geometry("600x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tab_view = TabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


class TabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # 创建标签页
        self.add("添加标签")
        self.add("标准化")

        # 配置标签页网格
        for tab_name in ["添加标签", "标准化"]:
            self.tab(tab_name).grid_columnconfigure(0, weight=1)
            self.tab(tab_name).grid_rowconfigure(0, weight=1)

        # 创建标准化处理框架
        self.normalize_frame = FileProcessingFrame(
            self.tab("标准化"),
            title="将文件拖放到下方区域",
            button_text="标准化文件",
            process_function=self._normalize_files
        )
        self.normalize_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # 创建添加标签处理框架
        self.tag_frame = FileProcessingFrame(
            self.tab("添加标签"),
            title="将文件拖放到下方区域",
            button_text="添加标签",
            process_function=self._add_tags_to_files,
            extra_widget_creator=self._create_tag_widgets
        )
        self.tag_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def _normalize_files(self, file_paths):
        """标准化文件的业务逻辑"""
        results = []
        for path in file_paths:
            try:
                new_path = remove_anki_id_and_normalize(path)
                results.append((True, f"处理成功: {Path(path).name}"))
            except Exception as e:
                results.append((False, f"处理失败: {Path(path).name} - {str(e)}"))
        return results

    def _add_tags_to_files(self, file_paths):
        """添加标签的业务逻辑"""
        tag = self.tag_entry.get().strip()
        if not tag:
            return [(False, "请输入标签!")]
        
        results = []
        for path in file_paths:
            try:
                new_path = add_tag(path, tag)
                results.append((True, f"已添加标签 #{tag}: {Path(path).name}"))
            except Exception as e:
                results.append((False, f"处理失败: {Path(path).name} - {str(e)}"))
        return results
    
    def _create_tag_widgets(self, parent_frame):
        """创建标签输入部分"""
        # 标签输入框标签
        self.tag_label = customtkinter.CTkLabel(
            parent_frame, text="请输入要添加的标签："
        )
        self.tag_label.pack(pady=(10, 0))
        
        # 标签输入框
        self.tag_entry = customtkinter.CTkEntry(parent_frame, width=200)
        self.tag_entry.pack(pady=(5, 10))
        
        return (self.tag_label, self.tag_entry)


class FileProcessingFrame(customtkinter.CTkFrame):
    """通用的文件处理框架"""
    def __init__(self, master, title, button_text, process_function, extra_widget_creator=None):
        super().__init__(master)
        
        self.process_function = process_function
        self.file_paths = []
        
        # 配置网格
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        # 创建标题标签
        self.title_label = customtkinter.CTkLabel(self, text=title)
        self.title_label.grid(row=0, column=0, padx=20, pady=(10, 0))
        
        # 额外的小部件（如有）
        if extra_widget_creator:
            self.extra_widgets_frame = customtkinter.CTkFrame(self, fg_color="transparent")
            self.extra_widgets_frame.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
            self.extra_widgets = extra_widget_creator(self.extra_widgets_frame)
        
        # 创建拖放区域
        self.drop_area = customtkinter.CTkTextbox(self, height=150)
        self.drop_area.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.drop_area.insert("1.0", "拖放文件到这里...")
        
        # 配置拖放功能
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind("<<Drop>>", self.drop_callback)
        
        # 显示状态信息
        self.status_label = customtkinter.CTkLabel(self, text="文件路径将显示在这里")
        self.status_label.grid(row=3, column=0, padx=20, pady=5)
        
        # 处理按钮
        self.process_button = customtkinter.CTkButton(
            self, text=button_text, command=self.process_files
        )
        self.process_button.grid(row=4, column=0, padx=20, pady=10)
    
    def drop_callback(self, event):
        """处理文件拖放事件"""
        # 清空之前的内容
        self.drop_area.delete("1.0", "end")
        
        # 获取文件路径
        file_paths = event.data
        self.file_paths = file_paths.split(" ") if " " in file_paths else [file_paths]
        
        # 显示拖放的文件
        for path in self.file_paths:
            self.drop_area.insert("end", f"{Path(path).stem}\n")
        
        # 更新状态标签
        if len(self.file_paths) == 1:
            self.status_label.configure(text=f"文件路径: {self.file_paths[0]}")
        else:
            self.status_label.configure(text=f"已选择 {len(self.file_paths)} 个文件")
    
    def process_files(self):
        """处理文件"""
        if not self.file_paths:
            self.status_label.configure(text="请先拖放文件!")
            return
        
        # 调用处理函数
        results = self.process_function(self.file_paths)
        
        # 显示结果
        self.drop_area.delete("1.0", "end")
        success_count = 0
        
        for success, message in results:
            if success:
                success_count += 1
                self.drop_area.insert("end", f"✓ {message}\n")
            else:
                self.drop_area.insert("end", f"✗ {message}\n")
        
        # 更新状态
        self.status_label.configure(text=f"处理完成: 成功 {success_count}/{len(results)} 个文件")


def run():
    """运行应用程序"""
    app = App()
    app.mainloop()