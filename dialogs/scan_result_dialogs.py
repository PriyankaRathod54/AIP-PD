"""
Scan result dialog classes for CyberDefense application
"""

import tkinter as tk

from config import DIALOG_WIDTH, DIALOG_HEIGHT, COLORS, FONTS


class SafeResultDialog(tk.Toplevel):
    def __init__(self, master: tk.Tk, app_name: str, sdk: str, size: str) -> None:
        super().__init__(master)
        self.title("CyberDefense")
        self.configure(bg=COLORS['primary_bg'])
        self.resizable(False, False)
        
        # Center the dialog
        from utils import center_window
        center_window(self, DIALOG_WIDTH, DIALOG_HEIGHT, parent=master)
        
        # Main container
        main_frame = tk.Frame(self, bg=COLORS['primary_bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left side with icon
        left_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        
        # Blue circle with white 'i'
        icon_canvas = tk.Canvas(left_frame, width=50, height=50, bg=COLORS['primary_bg'], highlightthickness=0)
        icon_canvas.pack(pady=10)
        icon_canvas.create_oval(5, 5, 45, 45, fill=COLORS['info_icon'], outline="")
        icon_canvas.create_text(25, 25, text="i", fill=COLORS['primary_bg'], font=("Segoe UI", 20, "bold"))
        
        # Right side with text
        right_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Result text
        result_label = tk.Label(right_frame, text="Result of scanning :", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_label.pack(anchor="w", pady=(0, 5))
        
        result_text = tk.Label(right_frame, text="Result : safe app", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_text.pack(anchor="w", pady=(0, 2))
        
        name_text = tk.Label(right_frame, text=f"Name : {app_name}", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        name_text.pack(anchor="w", pady=(0, 2))
        
        sdk_text = tk.Label(right_frame, text=f"SDK : {sdk}", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        sdk_text.pack(anchor="w", pady=(0, 2))
        
        size_text = tk.Label(right_frame, text=f"Size : {size}", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        size_text.pack(anchor="w", pady=(0, 10))
        
        # OK button
        ok_button = tk.Button(right_frame, text="OK", command=self.destroy, 
                             bg=COLORS['primary_bg'], fg="#000000", font=("Segoe UI", 9, "bold"),
                             relief=tk.SOLID, bd=1, padx=20, pady=5)
        ok_button.pack(anchor="w")
        
        # Make modal
        self.transient(master)
        self.grab_set()


class MalwareResultDialog(tk.Toplevel):
    def __init__(self, master: tk.Tk, app_name: str, sdk: str, size: str) -> None:
        super().__init__(master)
        self.title("CyberDefense")
        self.configure(bg=COLORS['primary_bg'])
        self.resizable(False, False)
        
        # Center the dialog
        from utils import center_window
        center_window(self, DIALOG_WIDTH, DIALOG_HEIGHT, parent=master)
        
        # Main container
        main_frame = tk.Frame(self, bg=COLORS['primary_bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left side with icon
        left_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        
        # Red circle with white X
        icon_canvas = tk.Canvas(left_frame, width=50, height=50, bg=COLORS['primary_bg'], highlightthickness=0)
        icon_canvas.pack(pady=10)
        icon_canvas.create_oval(5, 5, 45, 45, fill=COLORS['malware_icon'], outline="")
        icon_canvas.create_line(15, 15, 35, 35, fill=COLORS['primary_bg'], width=3)
        icon_canvas.create_line(35, 15, 15, 35, fill=COLORS['primary_bg'], width=3)
        
        # Right side with text
        right_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Result text
        result_label = tk.Label(right_frame, text="Result of scanning:", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_label.pack(anchor="w", pady=(0, 5))
        
        result_text = tk.Label(right_frame, text="Result: Malware app", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_text.pack(anchor="w", pady=(0, 2))
        
        name_text = tk.Label(right_frame, text=f"Name : {app_name}", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        name_text.pack(anchor="w", pady=(0, 2))
        
        sdk_text = tk.Label(right_frame, text=f"SDK: {sdk}", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        sdk_text.pack(anchor="w", pady=(0, 2))
        
        size_text = tk.Label(right_frame, text=f"Size: {size}", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        size_text.pack(anchor="w", pady=(0, 10))
        
        # OK button
        ok_button = tk.Button(right_frame, text="OK", command=self.destroy, 
                             bg=COLORS['info_icon'], fg=COLORS['primary_bg'], font=("Segoe UI", 9, "bold"),
                             relief=tk.FLAT, padx=20, pady=5)
        ok_button.pack(anchor="w")
        
        # Make modal
        self.transient(master)
        self.grab_set()


class SuspiciousResultDialog(tk.Toplevel):
    def __init__(self, master: tk.Tk, app_name: str, sdk: str, size: str) -> None:
        super().__init__(master)
        self.title("CyberDefense")
        self.configure(bg=COLORS['primary_bg'])
        self.resizable(False, False)
        
        # Center the dialog
        from utils import center_window
        center_window(self, DIALOG_WIDTH, DIALOG_HEIGHT, parent=master)
        
        # Main container
        main_frame = tk.Frame(self, bg=COLORS['primary_bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left side with icon
        left_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        
        # Orange circle with white exclamation
        icon_canvas = tk.Canvas(left_frame, width=50, height=50, bg=COLORS['primary_bg'], highlightthickness=0)
        icon_canvas.pack(pady=10)
        icon_canvas.create_oval(5, 5, 45, 45, fill=COLORS['suspicious_icon'], outline="")
        icon_canvas.create_text(25, 25, text="!", fill=COLORS['primary_bg'], font=("Segoe UI", 20, "bold"))
        
        # Right side with text
        right_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Result text
        result_label = tk.Label(right_frame, text="Result of scanning:", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_label.pack(anchor="w", pady=(0, 5))
        
        result_text = tk.Label(right_frame, text="Result: Suspicious app", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_text.pack(anchor="w", pady=(0, 2))
        
        name_text = tk.Label(right_frame, text=f"Name : {app_name}", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        name_text.pack(anchor="w", pady=(0, 2))
        
        sdk_text = tk.Label(right_frame, text=f"SDK: {sdk}", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        sdk_text.pack(anchor="w", pady=(0, 2))
        
        size_text = tk.Label(right_frame, text=f"Size: {size}", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        size_text.pack(anchor="w", pady=(0, 10))
        
        # OK button
        ok_button = tk.Button(right_frame, text="OK", command=self.destroy, 
                             bg=COLORS['suspicious_icon'], fg=COLORS['primary_bg'], font=("Segoe UI", 9, "bold"),
                             relief=tk.FLAT, padx=20, pady=5)
        ok_button.pack(anchor="w")
        
        # Make modal
        self.transient(master)
        self.grab_set()


# Legacy dialog classes for backward compatibility
class ScanResultDialog(tk.Toplevel):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title("CyberDefense")
        self.configure(bg=COLORS['primary_bg'])
        self.resizable(False, False)
        
        from utils import center_window
        center_window(self, DIALOG_WIDTH, DIALOG_HEIGHT, parent=master)
        
        main_frame = tk.Frame(self, bg=COLORS['primary_bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        left_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        
        icon_canvas = tk.Canvas(left_frame, width=50, height=50, bg=COLORS['primary_bg'], highlightthickness=0)
        icon_canvas.pack(pady=10)
        icon_canvas.create_oval(5, 5, 45, 45, fill=COLORS['malware_icon'], outline="")
        icon_canvas.create_line(15, 15, 35, 35, fill=COLORS['primary_bg'], width=3)
        icon_canvas.create_line(35, 15, 15, 35, fill=COLORS['primary_bg'], width=3)
        
        right_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        result_label = tk.Label(right_frame, text="Result of scanning:", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_label.pack(anchor="w", pady=(0, 5))
        
        result_text = tk.Label(right_frame, text="Result: Malware app", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_text.pack(anchor="w", pady=(0, 2))
        
        name_text = tk.Label(right_frame, text="Name : 광주버스", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        name_text.pack(anchor="w", pady=(0, 2))
        
        sdk_text = tk.Label(right_frame, text="SDK: 25", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        sdk_text.pack(anchor="w", pady=(0, 2))
        
        size_text = tk.Label(right_frame, text="Size: 6.87 MB", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        size_text.pack(anchor="w", pady=(0, 10))
        
        ok_button = tk.Button(right_frame, text="OK", command=self.destroy, 
                             bg=COLORS['info_icon'], fg=COLORS['primary_bg'], font=("Segoe UI", 9, "bold"),
                             relief=tk.FLAT, padx=20, pady=5)
        ok_button.pack(anchor="w")
        
        self.transient(master)
        self.grab_set()


class ScanResultDialog2(tk.Toplevel):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title("CyberDefense")
        self.configure(bg=COLORS['primary_bg'])
        self.resizable(False, False)
        
        from utils import center_window
        center_window(self, DIALOG_WIDTH, DIALOG_HEIGHT, parent=master)
        
        main_frame = tk.Frame(self, bg=COLORS['primary_bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        left_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        
        icon_canvas = tk.Canvas(left_frame, width=50, height=50, bg=COLORS['primary_bg'], highlightthickness=0)
        icon_canvas.pack(pady=10)
        icon_canvas.create_oval(5, 5, 45, 45, fill=COLORS['malware_icon'], outline="")
        icon_canvas.create_line(15, 15, 35, 35, fill=COLORS['primary_bg'], width=3)
        icon_canvas.create_line(35, 15, 15, 35, fill=COLORS['primary_bg'], width=3)
        
        right_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        result_label = tk.Label(right_frame, text="Result of scanning:", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_label.pack(anchor="w", pady=(0, 5))
        
        result_text = tk.Label(right_frame, text="Result: Suspicious app", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_text.pack(anchor="w", pady=(0, 2))
        
        name_text = tk.Label(right_frame, text="Name : FakeBank Pro", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        name_text.pack(anchor="w", pady=(0, 2))
        
        sdk_text = tk.Label(right_frame, text="SDK: 28", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        sdk_text.pack(anchor="w", pady=(0, 2))
        
        size_text = tk.Label(right_frame, text="Size: 12.3 MB", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        size_text.pack(anchor="w", pady=(0, 10))
        
        ok_button = tk.Button(right_frame, text="OK", command=self.destroy, 
                             bg=COLORS['info_icon'], fg=COLORS['primary_bg'], font=("Segoe UI", 9, "bold"),
                             relief=tk.FLAT, padx=20, pady=5)
        ok_button.pack(anchor="w")
        
        self.transient(master)
        self.grab_set()


class ScanResultDialog3(tk.Toplevel):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title("CyberDefense")
        self.configure(bg=COLORS['primary_bg'])
        self.resizable(False, False)
        
        from utils import center_window
        center_window(self, DIALOG_WIDTH, DIALOG_HEIGHT, parent=master)
        
        main_frame = tk.Frame(self, bg=COLORS['primary_bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        left_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        
        icon_canvas = tk.Canvas(left_frame, width=50, height=50, bg=COLORS['primary_bg'], highlightthickness=0)
        icon_canvas.pack(pady=10)
        icon_canvas.create_oval(5, 5, 45, 45, fill=COLORS['safe_icon'], outline="")
        icon_canvas.create_line(18, 25, 28, 35, fill=COLORS['primary_bg'], width=3)
        icon_canvas.create_line(28, 35, 38, 20, fill=COLORS['primary_bg'], width=3)
        
        right_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        result_label = tk.Label(right_frame, text="Result of scanning:", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_label.pack(anchor="w", pady=(0, 5))
        
        result_text = tk.Label(right_frame, text="Result: Safe app", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_text.pack(anchor="w", pady=(0, 2))
        
        name_text = tk.Label(right_frame, text="Name : Calculator", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        name_text.pack(anchor="w", pady=(0, 2))
        
        sdk_text = tk.Label(right_frame, text="SDK: 30", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        sdk_text.pack(anchor="w", pady=(0, 2))
        
        size_text = tk.Label(right_frame, text="Size: 2.1 MB", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        size_text.pack(anchor="w", pady=(0, 10))
        
        ok_button = tk.Button(right_frame, text="OK", command=self.destroy, 
                             bg=COLORS['info_icon'], fg=COLORS['primary_bg'], font=("Segoe UI", 9, "bold"),
                             relief=tk.FLAT, padx=20, pady=5)
        ok_button.pack(anchor="w")
        
        self.transient(master)
        self.grab_set()


class ScanResultDialog4(tk.Toplevel):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title("CyberDefense")
        self.configure(bg=COLORS['primary_bg'])
        self.resizable(False, False)
        
        from utils import center_window
        center_window(self, DIALOG_WIDTH, DIALOG_HEIGHT, parent=master)
        
        main_frame = tk.Frame(self, bg=COLORS['primary_bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        left_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        
        icon_canvas = tk.Canvas(left_frame, width=50, height=50, bg=COLORS['primary_bg'], highlightthickness=0)
        icon_canvas.pack(pady=10)
        icon_canvas.create_oval(5, 5, 45, 45, fill=COLORS['info_icon'], outline="")
        icon_canvas.create_text(25, 25, text="i", fill=COLORS['primary_bg'], font=("Segoe UI", 20, "bold"))
        
        right_frame = tk.Frame(main_frame, bg=COLORS['primary_bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        result_label = tk.Label(right_frame, text="Result of scanning :", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_label.pack(anchor="w", pady=(0, 5))
        
        result_text = tk.Label(right_frame, text="Result : safe app", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        result_text.pack(anchor="w", pady=(0, 2))
        
        name_text = tk.Label(right_frame, text="Name : Amazon Prime Video", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        name_text.pack(anchor="w", pady=(0, 2))
        
        sdk_text = tk.Label(right_frame, text="SDK : 29", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        sdk_text.pack(anchor="w", pady=(0, 2))
        
        size_text = tk.Label(right_frame, text="Size : 13.6 MB", bg=COLORS['primary_bg'], fg="#333333", font=FONTS['small'])
        size_text.pack(anchor="w", pady=(0, 10))
        
        ok_button = tk.Button(right_frame, text="OK", command=self.destroy, 
                             bg=COLORS['primary_bg'], fg="#000000", font=("Segoe UI", 9, "bold"),
                             relief=tk.SOLID, bd=1, padx=20, pady=5)
        ok_button.pack(anchor="w")
        
        self.transient(master)
        self.grab_set()
