import customtkinter as ctk
import json
import os

# 基础配置
DATA_FILE = "data.json"
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MemoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("现代备忘录")
        self.geometry("400x500")

        # 顶部布局
        self.entry = ctk.CTkEntry(self, placeholder_text="输入任务内容...")
        self.entry.pack(pady=20, padx=20, fill="x")

        self.add_button = ctk.CTkButton(self, text="添加", command=self.add_item)
        self.add_button.pack(pady=5, padx=20, fill="x")

        # 任务列表容器
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="待办事项")
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.items = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.items = json.load(f)
                for item in self.items:
                    self.create_item_ui(item)

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.items, f, ensure_ascii=False)

    def add_item(self):
        text = self.entry.get()
        if text:
            self.items.append(text)
            self.create_item_ui(text)
            self.save_data()
            self.entry.delete(0, "end")

    def create_item_ui(self, text):
        # 创建条目容器
        frame = ctk.CTkFrame(self.scrollable_frame)
        frame.pack(fill="x", pady=5)

        label = ctk.CTkLabel(frame, text=text, anchor="w")
        label.pack(side="left", padx=10, fill="x", expand=True)

        btn = ctk.CTkButton(frame, text="删除", width=50, fg_color="red", 
                            command=lambda: self.delete_item(frame, text))
        btn.pack(side="right", padx=5)

    def delete_item(self, frame, text):
        frame.destroy()
        self.items.remove(text)
        self.save_data()

if __name__ == "__main__":
    app = MemoApp()
    app.mainloop()