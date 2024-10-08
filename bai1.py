import tkinter as tk
from tkinter import messagebox, font
import math

# Class chính cho ứng dụng
class QuadraticEquationSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Giải phương trình bậc hai")
        self.root.geometry("400x300")
        self.root.configure(bg="#f2f2f2")

        # Font chữ
        self.custom_font = font.Font(family="Arial", size=12)

        # Tạo LabelFrame để nhóm các trường nhập liệu
        input_frame = tk.LabelFrame(root, text="Nhập liệu", padx=10, pady=10, bg="#ffffff")
        input_frame.pack(padx=10, pady=10)

        self.label_a = tk.Label(input_frame, text="Nhập a:", font=self.custom_font, bg="#ffffff")
        self.label_a.grid(row=0, column=0, padx=5, pady=5)
        self.entry_a = tk.Entry(input_frame, font=self.custom_font)
        self.entry_a.grid(row=0, column=1, padx=5, pady=5)

        self.label_b = tk.Label(input_frame, text="Nhập b:", font=self.custom_font, bg="#ffffff")
        self.label_b.grid(row=1, column=0, padx=5, pady=5)
        self.entry_b = tk.Entry(input_frame, font=self.custom_font)
        self.entry_b.grid(row=1, column=1, padx=5, pady=5)

        self.label_c = tk.Label(input_frame, text="Nhập c:", font=self.custom_font, bg="#ffffff")
        self.label_c.grid(row=2, column=0, padx=5, pady=5)
        self.entry_c = tk.Entry(input_frame, font=self.custom_font)
        self.entry_c.grid(row=2, column=1, padx=5, pady=5)

        self.solve_button = tk.Button(root, text="Giải phương trình", command=self.solve_quadratic, font=self.custom_font, bg="#4CAF50", fg="white")
        self.solve_button.pack(pady=10)

        # Hiển thị kết quả
        self.result_label = tk.Label(root, text="Kết quả: ", font=self.custom_font, bg="#f2f2f2")
        self.result_label.pack(pady=10)

        # Nút reset
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_fields, font=self.custom_font, bg="#f44336", fg="white")
        self.reset_button.pack(pady=5)

    def solve_quadratic(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())
            
            if a == 0:
                raise ValueError("Giá trị của a không được bằng 0.")

            # Tính delta
            delta = b**2 - 4*a*c
            if delta > 0:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                result = f"Có 2 nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}"
            elif delta == 0:
                x = -b / (2 * a)
                result = f"Có 1 nghiệm: x = {x:.2f}"
            else:
                result = "Phương trình vô nghiệm."
            
            self.result_label.config(text=result)
        except ValueError as ve:
            messagebox.showerror("Lỗi nhập liệu", str(ve))

    def reset_fields(self):
        self.entry_a.delete(0, tk.END)  
        self.entry_b.delete(0, tk.END) 
        self.entry_c.delete(0, tk.END)  
        self.result_label.config(text="Kết quả: ")  

# Tạo cửa sổ chính
if __name__ == "__main__":
    root = tk.Tk()
    app = QuadraticEquationSolver(root)  # Tạo đối tượng ứng dụng
    root.mainloop()
