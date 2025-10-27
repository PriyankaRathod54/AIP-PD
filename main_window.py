"""
Main window class for CyberDefense application
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser
import os

from config import WINDOW_WIDTH, WINDOW_HEIGHT, COLORS, FONTS
from utils import center_window, create_link, create_decorative_bar, create_sample_apks, determine_app_category, generate_app_details_from_filename
from services import APKScanService
from dialogs import AboutWindow, ContactWindow, PhishingDetectionDialog, ChatbotDialog, SafeResultDialog, MalwareResultDialog, SuspiciousResultDialog


class CyberDefenseApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("CyberDefense")
        self.configure(bg=COLORS['primary_bg'])
        self.minsize(900, 560)

        # Center window on screen
        center_window(self, WINDOW_WIDTH, WINDOW_HEIGHT)

        # Root layout: a canvas for background artwork and a frame overlay for content
        self.background_canvas = tk.Canvas(self, bg=COLORS['primary_bg'], highlightthickness=0)
        self.background_canvas.pack(fill=tk.BOTH, expand=True)
        self.background_canvas.bind("<Configure>", self._redraw_background)

        # Overlay content frame (absolute placement for design control)
        self.overlay = tk.Frame(self.background_canvas, bg=COLORS['primary_bg'])
        self.background_canvas.create_window(0, 0, anchor="nw", window=self.overlay)
        self.overlay.bind("<Configure>", self._sync_overlay_size)

        self._build_top_links()
        self._build_title_and_buttons()
        self._build_left_illustration()

    # ---------- UI Construction ----------
    def _build_top_links(self) -> None:
        container = tk.Frame(self.overlay, bg=COLORS['primary_bg'])
        container.place(relx=0.72, rely=0.03)

        create_link(container, "About", self._on_about).grid(row=0, column=0, padx=(0, 18))
        create_link(container, "Contact", self._on_contact).grid(row=0, column=1, padx=(0, 18))
        create_link(container, "Exit", self._on_exit).grid(row=0, column=2)

        brand = tk.Label(
            self.overlay,
            text="CyberDefense",
            bg=COLORS['primary_bg'],
            fg=COLORS['accent_purple'],
            font=FONTS['brand'],
        )
        brand.place(relx=0.08, rely=0.06, anchor="w")

    def _build_title_and_buttons(self) -> None:
        title = tk.Label(
            self.overlay,
            text="CYBER-DEFENSE TOOL",
            bg=COLORS['primary_bg'],
            fg=COLORS['accent_blue'],
            font=FONTS['title'],
        )
        title.place(relx=0.56, rely=0.20, anchor="center")

        subtitle_line = tk.Frame(self.overlay, bg=COLORS['accent_blue'], height=3, width=220)
        subtitle_line.place(relx=0.56, rely=0.25, anchor="center")

        # Buttons stack
        buttons = [
            ("Web Surfing With Filter", self._on_web_filter),
            ("Scan Android App", self._on_scan_android),
            ("Phishing Detection", self._on_about_phishing),
            ("Chatbot", self._on_talk_with_bot),
        ]

        button_container = tk.Frame(self.overlay, bg=COLORS['primary_bg'])
        button_container.place(relx=0.56, rely=0.55, anchor="center")

        for i, (text, command) in enumerate(buttons):
            pill = tk.Button(
                button_container,
                text=text,
                command=command,
                bg=COLORS['button_bg'],
                activebackground=COLORS['button_active'],
                fg=COLORS['text_dark'],
                relief=tk.FLAT,
                font=FONTS['button'],
                padx=28,
                pady=10,
                bd=0,
            )
            pill.grid(row=i, column=0, pady=12, sticky="ew")
            pill.update_idletasks()
            pill.configure(width=28)
            

    def _build_left_illustration(self) -> None:
        # A simple mock illustration block to suggest the phone + login card
        phone_frame = tk.Frame(self.overlay, bg=COLORS['illustration_bg'], width=230, height=390)
        phone_frame.place(relx=0.18, rely=0.58, anchor="center")
        phone_inner = tk.Frame(phone_frame, bg=COLORS['illustration_inner'], width=190, height=320)
        phone_inner.place(relx=0.5, rely=0.52, anchor="center")

        # Lock icon approximation
        lock_canvas = tk.Canvas(phone_inner, width=70, height=70, bg=COLORS['illustration_inner'], highlightthickness=0)
        lock_canvas.place(relx=0.5, rely=0.3, anchor="center")
        lock_canvas.create_rectangle(15, 35, 55, 58, outline="#ffffff", width=3)
        lock_canvas.create_arc(18, 12, 52, 50, start=0, extent=180, style=tk.ARC, outline="#ffffff", width=3)
        lock_canvas.create_oval(32, 42, 38, 48, outline="#ffffff", width=3)

        # Floating login card
        card = tk.Frame(self.overlay, bg=COLORS['primary_bg'], highlightbackground="#cfd6e6", highlightthickness=2)
        card.place(relx=0.31, rely=0.48, anchor="center")

        tk.Label(card, text="username", font=FONTS['small'], bg=COLORS['primary_bg'], fg=COLORS['text_light']).grid(row=0, column=0, padx=14, pady=(12, 4), sticky="w")
        tk.Entry(card, width=22, font=FONTS['small'], relief=tk.FLAT, highlightthickness=1, highlightbackground="#d0d0d0").grid(row=1, column=0, padx=14, pady=(0, 10))
        tk.Label(card, text="password", font=FONTS['small'], bg=COLORS['primary_bg'], fg=COLORS['text_light']).grid(row=2, column=0, padx=14, pady=(4, 4), sticky="w")
        tk.Entry(card, width=22, show="•", font=FONTS['small'], relief=tk.FLAT, highlightthickness=1, highlightbackground="#d0d0d0").grid(row=3, column=0, padx=14, pady=(0, 12))
        tk.Button(card, text="LOGIN", relief=tk.FLAT, bg=COLORS['accent_blue'], fg=COLORS['primary_bg'], font=("Segoe UI", 9, "bold"), padx=10, pady=4).grid(row=4, column=0, pady=(0, 12))

    # ---------- Background Drawing ----------
    def _redraw_background(self, event=None) -> None:
        c = self.background_canvas
        c.delete("all")

        width = c.winfo_width()
        height = c.winfo_height()

        # Gentle curved bottom-right blob
        c.create_oval(
            width * 0.45,
            height * 0.55,
            width * 1.15,
            height * 1.25,
            fill=COLORS['background_blob'],
            outline="",
        )

        # Top-right white sweep
        c.create_polygon(
            [
                (width * 0.45, 0),
                (width, 0),
                (width, height * 0.18),
                (width * 0.60, height * 0.28),
            ],
            fill=COLORS['background_sweep'],
            outline="",
        )

        # Decorative rounded bars
        create_decorative_bar(c, width * 0.62, height * 0.12, width * 0.20, 22, COLORS['decorative_bar'])
        create_decorative_bar(c, width * 0.14, height * 0.14, width * 0.18, 18, COLORS['decorative_bar'])
        create_decorative_bar(c, width * 0.78, height * 0.62, width * 0.16, 22, COLORS['decorative_bar'])
        create_decorative_bar(c, width * 0.08, height * 0.70, width * 0.22, 22, COLORS['decorative_bar'])

        # Ensure overlay is on top and full size
        c.create_window(0, 0, anchor="nw", window=self.overlay, tags=("overlay",))
        c.tag_raise("overlay")
        self._sync_overlay_size()

    def _sync_overlay_size(self, event=None) -> None:
        # Resize overlay to match canvas size for reliable absolute placement
        self.overlay.update_idletasks()
        self.background_canvas.itemconfig("overlay", width=self.background_canvas.winfo_width(), height=self.background_canvas.winfo_height())

    # ---------- Actions ----------
    def _on_about(self) -> None:
        AboutWindow(self)

    def _on_contact(self) -> None:
        ContactWindow(self)

    def _on_exit(self) -> None:
        self.destroy()

    def _on_web_filter(self) -> None:
        try:
            webbrowser.open("https://www.google.com", new=2)
        except Exception:
            messagebox.showerror("Browser Error", "Unable to open the default web browser.")

    def _on_scan_android(self) -> None:
        # Create sample APK files if they don't exist
        create_sample_apks()
        
        # Open file dialog to select APK file
        file_path = filedialog.askopenfilename(
            title="Select APK file",
            filetypes=[("APK files", "*.apk"), ("All files", "*.*")],
            initialdir=os.path.join(os.getcwd(), "sample_apks")
        )
        
        if file_path:
            # Show scan result based on file name with specific details
            filename = os.path.basename(file_path).lower()
            
            # Get app details
            app_details = APKScanService.get_app_details(filename)
            name, sdk, size = app_details
            
            # Determine category
            category = determine_app_category(filename)
            
            if category == "safe":
                SafeResultDialog(self, name, sdk, size)
            elif category == "malware":
                MalwareResultDialog(self, name, sdk, size)
            elif category == "suspicious":
                SuspiciousResultDialog(self, name, sdk, size)
            else:
                # For generic apps, generate random details and random result
                app_name, sdk, size, hash_int = generate_app_details_from_filename(filename)
                result_type = hash_int % 3
                
                if result_type == 0:
                    SafeResultDialog(self, app_name, sdk, size)
                elif result_type == 1:
                    SuspiciousResultDialog(self, app_name, sdk, size)
                else:
                    MalwareResultDialog(self, app_name, sdk, size)
    def _on_about_phishing(self) -> None:
        PhishingDetectionDialog(self)

    def _on_talk_with_bot(self) -> None:
        """Open the chatbot dialog"""
        ChatbotDialog(self)
        
