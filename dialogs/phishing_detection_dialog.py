"""
Phishing detection dialog for CyberDefense application
"""

import tkinter as tk

from config import COLORS, FONTS
from services import PhishingDetectionService


class PhishingDetectionDialog(tk.Toplevel):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title("Phishing Detection - CyberDefense")
        self.configure(bg=COLORS['phishing_bg'])  # Light lavender background
        self.resizable(False, False)
        
        # Center the dialog
        from utils import center_window
        center_window(self, 900, 530, parent=master)
        
        # Main title
        title_label = tk.Label(self, text="Phishing Detection", 
                              font=("Segoe UI", 24, "bold"), 
                              bg=COLORS['phishing_bg'], fg="#000000")
        title_label.pack(pady=20)
        
        # URL Input Section
        url_frame = tk.Frame(self, bg=COLORS['phishing_bg'])
        url_frame.pack(pady=5, padx=40, fill=tk.X)
        
        url_label = tk.Label(url_frame, text="Enter the URL to check:", 
                            font=("Segoe UI", 14), 
                            bg=COLORS['phishing_bg'], fg="#000000")
        url_label.pack(side=tk.LEFT)
        
        self.url_entry = tk.Entry(url_frame, font=("Segoe UI", 14), width=50, 
                                 relief=tk.SOLID, bd=1, fg="#808080")
        self.url_entry.pack(side=tk.LEFT, padx=(10, 10))
        self.url_entry.insert(0, "https://www.example.com")
        
        # Bind events for placeholder behavior
        self.url_entry.bind("<FocusIn>", self._on_entry_focus_in)
        self.url_entry.bind("<FocusOut>", self._on_entry_focus_out)
        self.url_entry.bind("<KeyPress>", self._on_entry_key_press)
        
        check_button = tk.Button(url_frame, text="Check", 
                               font=("Segoe UI", 11, "bold"),
                               bg="#8b4c96", fg=COLORS['primary_bg'], 
                               relief=tk.FLAT, padx=20, pady=5,
                               command=self._check_url)
        check_button.pack(side=tk.LEFT)
        
        # URL Phishing Status Section
        status_frame = tk.Frame(self, bg=COLORS['primary_bg'], relief=tk.SOLID, bd=1)
        status_frame.pack(pady=10, padx=40, fill=tk.BOTH, expand=True)
        
        status_title = tk.Label(status_frame, text="URL Phishing Status:", 
                              font=("Segoe UI", 16, "bold", "underline"), 
                              bg=COLORS['primary_bg'], fg="#000000")
        status_title.pack(pady=10)
        
        self.status_label = tk.Label(status_frame, text="Awaiting Input...", 
                                   font=("Segoe UI", 20, "bold"), 
                                   bg=COLORS['primary_bg'], fg="#000000")
        self.status_label.pack(pady=3)
        
        # Bottom section with two boxes
        bottom_frame = tk.Frame(self, bg=COLORS['phishing_bg'])
        bottom_frame.pack(pady=20, padx=40, fill=tk.X)
        
        # Left box - Phishing Detection Tool
        left_box = tk.Frame(bottom_frame, bg=COLORS['primary_bg'], relief=tk.SOLID, bd=1)
        left_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        tool_title = tk.Label(left_box, text="Phishing Detection Tool", 
                             font=("Segoe UI", 16, "bold"), 
                             bg=COLORS['primary_bg'], fg="#000000")
        tool_title.pack(pady=20, padx=55, anchor="w")
        
        # Tool features
        features = [
            "- Uses ML Model (e.g., Random Forest)",
            "- Extracts 15+ URL Features", 
            "- High Accuracy Rate (98.5%)"
        ]
        
        for feature in features:
            feature_label = tk.Label(left_box, text=feature, 
                                   font=("Segoe UI", 14), 
                                   bg=COLORS['primary_bg'], fg="#000000")
            feature_label.pack(pady=2, padx=35, anchor="w")
        
        # Right box - Model Comparison
        right_box = tk.Frame(bottom_frame, bg=COLORS['primary_bg'], relief=tk.SOLID, bd=1)
        right_box.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        model_title = tk.Label(right_box, text="[Model Comparison Graph Placeholder]", 
                              font=("Segoe UI", 14, "bold"), 
                              bg=COLORS['primary_bg'], fg="#ff0000")
        model_title.pack(pady=15, padx=15, anchor="w")
        
        accuracy_label = tk.Label(right_box, text="Accuracy: 98.5%", 
                                 font=("Segoe UI", 14), 
                                 bg=COLORS['primary_bg'], fg="#ff0000")
        accuracy_label.pack(pady=5, padx=15, anchor="w")
        
        # Make modal
        self.transient(master)
        self.grab_set()
    
    def _on_entry_focus_in(self, event):
        """Handle focus in event for placeholder behavior"""
        if self.url_entry.get() == "https://www.example.com":
            self.url_entry.delete(0, tk.END)
            self.url_entry.config(fg="#000000")
    
    def _on_entry_focus_out(self, event):
        """Handle focus out event for placeholder behavior"""
        if not self.url_entry.get():
            self.url_entry.insert(0, "https://www.example.com")
            self.url_entry.config(fg="#808080")
    
    def _on_entry_key_press(self, event):
        """Handle key press for placeholder behavior"""
        if self.url_entry.get() == "https://www.example.com":
            self.url_entry.delete(0, tk.END)
            self.url_entry.config(fg="#000000")
    
    def _check_url(self) -> None:
        """Check the URL for phishing"""
        url = self.url_entry.get().strip()
        
        if not url or url == "https://www.example.com":
            self.status_label.config(text="Awaiting Input...", fg="#000000")
            return
        
        # Keep sample URL constant - don't show detection for example.com
        if "example.com" in url.lower():
            self.status_label.config(text="Awaiting Input...", fg="#000000")
            return
        
        # Use the phishing detection service
        is_phishing = PhishingDetectionService.simple_phishing_check(url)
        
        if is_phishing:
            self.status_label.config(text="⚠️PHISHING DETECTED", fg="#ff0000")
        else:
            self.status_label.config(text="✅SAFE", fg="#00aa00")
