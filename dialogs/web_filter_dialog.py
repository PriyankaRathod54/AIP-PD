"""
Web filter dialog classes for CyberDefense application
"""

import tkinter as tk
import threading
from urllib.parse import urlparse

from config import COLORS, FONTS, POPULAR_SITES
from utils import normalize_url
from services import WebFilterService


class WebFilterDialog(tk.Toplevel):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title("Web Surfing With Filter")
        self.configure(bg=COLORS['primary_bg'])
        self.resizable(False, False)

        tk.Label(self, text="Enter a URL to open:", bg=COLORS['primary_bg'], fg=COLORS['text_dark'], font=("Segoe UI", 11, "bold")).grid(row=0, column=0, padx=16, pady=(14, 4), sticky="w")
        self.url_var = tk.StringVar(value="https://www.facebook.com")
        entry = tk.Entry(self, textvariable=self.url_var, width=52)
        entry.grid(row=1, column=0, padx=16, pady=(6, 8))
        entry.focus_set()

        btns = tk.Frame(self, bg=COLORS['primary_bg'])
        btns.grid(row=2, column=0, padx=16, pady=(6, 14), sticky="e")
        tk.Button(btns, text="Cancel", command=self.destroy).pack(side=tk.RIGHT, padx=(0, 8))
        tk.Button(btns, text="Open", command=self._on_open).pack(side=tk.RIGHT)

        self.grab_set()
        self.transient(master)

    def _on_open(self) -> None:
        url = normalize_url(self.url_var.get().strip())
        if not url:
            from tkinter import messagebox
            messagebox.showerror("Invalid URL", "Please enter a valid http/https URL.")
            return
        self.destroy()
        threading.Thread(target=WebFilterService.open_with_selenium, args=(url, self.master), daemon=True).start()


class WebFilterSitesWindow(tk.Toplevel):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title("Web Surfing With Filter")
        self.configure(bg=COLORS['primary_bg'])
        self.minsize(760, 520)

        header = tk.Frame(self, bg=COLORS['primary_bg'])
        header.pack(fill=tk.X, padx=18, pady=(16, 8))
        tk.Label(header, text="Web Surfing With Filter", bg=COLORS['primary_bg'], fg="#2b2a6b", font=("Segoe UI", 18, "bold")).pack(side=tk.LEFT)
        tk.Button(header, text="Custom URL", command=lambda: WebFilterDialog(self)).pack(side=tk.RIGHT)

        body = tk.Frame(self, bg=COLORS['primary_bg'])
        body.pack(fill=tk.BOTH, expand=True, padx=18, pady=8)

        tk.Label(body, text="Quick check on popular sites", bg=COLORS['primary_bg'], fg="#6b6b6b", font=FONTS['body']).pack(anchor="w", pady=(0, 10))

        grid = tk.Frame(body, bg=COLORS['primary_bg'])
        grid.pack(fill=tk.BOTH, expand=True)

        for i, (name, url) in enumerate(POPULAR_SITES):
            row = tk.Frame(grid, bg=COLORS['primary_bg'])
            row.grid(row=i, column=0, sticky="ew", pady=6)
            tk.Label(row, text=name, bg=COLORS['primary_bg'], fg="#2b2a6b", font=("Segoe UI", 12, "bold")).pack(side=tk.LEFT)
            tk.Label(row, text=url, bg=COLORS['primary_bg'], fg="#6b6b6b", font=FONTS['small']).pack(side=tk.LEFT, padx=(8, 0))
            tk.Button(row, text="Open & Check", command=lambda u=url: self._open_safe(u)).pack(side=tk.RIGHT)

        footer = tk.Frame(self, bg=COLORS['primary_bg'])
        footer.pack(fill=tk.X, padx=18, pady=(4, 12))
        tk.Button(footer, text="Close", command=self.destroy).pack(side=tk.RIGHT)

        self.transient(master)
        self.grab_set()

    def _open_safe(self, url: str) -> None:
        WebFilterService.open_safe_site(url, self)

    def _notify(self, fn) -> None:
        try:
            self.after(0, fn)
        except Exception:
            pass
