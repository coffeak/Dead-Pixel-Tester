import tkinter as tk
from tkinter import messagebox

colors = ["white", "black", "red", "green", "blue"]

class DeadPixelTester:
    def __init__(self, master):
        self.master = master
        self.master.title("Dead Pixel Tester")
        self.master.geometry("450x250")
        self.master.resizable(False, False)

        self.label = tk.Label(master, text="Welcome to Dead Pixel Tester", font=("Arial", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start Test", command=self.start_test, font=("Arial", 13), width=20)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Exit", command=master.quit, font=("Arial", 13), width=20)
        self.quit_button.pack(pady=5)

        self.footer = tk.Label(master, text="Developed by coffeak.com", font=("Arial", 10), fg="gray")
        self.footer.pack(side="bottom", pady=10)

    def start_test(self):
        self.master.withdraw()  # Hide main window
        self.test_window = tk.Toplevel()
        self.test_window.attributes('-fullscreen', True)
        self.test_window.configure(bg=colors[0])
        self.current_index = 0

        self.test_window.bind("<Button-1>", self.next_color)
        self.test_window.bind("<Escape>", lambda e: self.end_test())

        # Branding in test screen
        self.footer_label = tk.Label(self.test_window, text="Developed by coffeak.com", font=("Arial", 12), bg=colors[0], fg="gray")
        self.footer_label.pack(side="bottom", pady=15)

    def next_color(self, event):
        self.current_index += 1
        if self.current_index >= len(colors):
            self.end_test()
        else:
            new_color = colors[self.current_index]
            self.test_window.configure(bg=new_color)
            self.footer_label.configure(bg=new_color)

    def end_test(self):
        self.test_window.destroy()
        self.master.deiconify()
        messagebox.showinfo("Test Completed", "The dead pixel test is finished.\nIf you noticed any abnormal pixels, your screen may have dead or stuck pixels.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DeadPixelTester(root)
    root.mainloop()
