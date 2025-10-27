"""
About window dialog for CyberDefense application
"""

import tkinter as tk

from config import WINDOW_WIDTH, WINDOW_HEIGHT, COLORS, FONTS
from utils import center_window, create_link
# Import moved to avoid circular dependency


class AboutWindow(tk.Toplevel):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title("CyberDefense - About")
        self.configure(bg=COLORS['primary_bg'])
        self.minsize(900, 560)

        # Center relative to master
        center_window(self, WINDOW_WIDTH, WINDOW_HEIGHT, parent=master)

        self.background_canvas = tk.Canvas(self, bg=COLORS['primary_bg'], highlightthickness=0)
        self.background_canvas.pack(fill=tk.BOTH, expand=True)
        self.background_canvas.bind("<Configure>", self._redraw_background)

        self.overlay = tk.Frame(self.background_canvas, bg=COLORS['primary_bg'])
        self.background_canvas.create_window(0, 0, anchor="nw", window=self.overlay, tags=("overlay",))

        self._build_header(master)
        self._build_left_illustration()
        self._build_content()

        # Focus on about window
        self.transient(master)
        self.grab_set()

    # ----- Header with brand and links -----
    def _build_header(self, master: tk.Tk) -> None:
        brand = tk.Label(self.overlay, text="CyberDefense", bg=COLORS['primary_bg'], fg=COLORS['accent_purple'], font=FONTS['brand'])
        brand.place(relx=0.16, rely=0.10, anchor="w")

        links = tk.Frame(self.overlay, bg=COLORS['primary_bg'])
        links.place(relx=0.73, rely=0.06)

        create_link(links, "Home", self._on_home).grid(row=0, column=0, padx=(0, 18))
        create_link(links, "Contact", self._on_contact).grid(row=0, column=1, padx=(0, 18))
        create_link(links, "Exit", self.destroy).grid(row=0, column=2)

    # ----- Illustration -----
    def _build_left_illustration(self) -> None:
        # Big illustration placeholder on left
        illo = tk.Canvas(self.overlay, width=430, height=430, bg=COLORS['primary_bg'], highlightthickness=0)
        illo.place(relx=0.25, rely=0.56, anchor="center")

        # Phone body
        illo.create_rectangle(130, 80, 310, 360, fill="#e9e8ff", outline="")
        illo.create_rectangle(150, 110, 290, 330, fill="#4f5fb8", outline="")

        # Unlocked padlock
        illo.create_rectangle(200, 240, 240, 280, outline="#ffffff", width=3)
        illo.create_arc(196, 205, 244, 255, start=0, extent=180, style=tk.ARC, outline="#ffffff", width=3)
        illo.create_line(240, 220, 260, 200, fill="#ff6f61", width=5)  # open shackle

        # Shield
        illo.create_polygon(310, 240, 350, 260, 340, 315, 310, 335, 280, 315, 270, 260, fill="#ffb44c", outline="")
        illo.create_polygon(310, 248, 338, 263, 331, 308, 310, 321, 289, 308, 282, 263, fill="#3650a6", outline="")
        illo.create_polygon(310, 255, 320, 270, 310, 300, 300, 270, fill="#ff6f61", outline="")

    # ----- Right content -----
    def _build_content(self) -> None:
        # Title lines
        cyber = tk.Label(self.overlay, text="CYBER", bg=COLORS['primary_bg'], fg="#ff6f61", font=("Segoe UI", 30, "bold"))
        cyber.place(relx=0.63, rely=0.22, anchor="center")

        divider = tk.Frame(self.overlay, bg="#f28aa0", height=4, width=160)
        divider.place(relx=0.63, rely=0.27, anchor="center")

        defense = tk.Label(self.overlay, text="DEFENSE", bg=COLORS['primary_bg'], fg="#2b2a6b", font=("Segoe UI", 34, "bold"))
        defense.place(relx=0.63, rely=0.33, anchor="center")

        # Paragraph text
        paragraph = (
            "We developed CyberDefense using Python, machine learning, JS, and other technologies. "
            "This tool aims to detect and prevent users from visiting phishing URLs as well it has "
            "a chatbot to guide you about phishing. Besides detecting phishing, it also detects "
            "harmful mobile apps by checking their permission requirements."
        )
        text = tk.Label(self.overlay, text=paragraph, wraplength=420, justify="left", bg=COLORS['primary_bg'], fg=COLORS['text_dark'], font=FONTS['body'])
        text.place(relx=0.63, rely=0.48, anchor="center")

        # Bullet points
        bullets_title = tk.Label(self.overlay, text="This tool consists of three phases:", bg=COLORS['primary_bg'], fg=COLORS['text_dark'], font=("Segoe UI", 12, "bold"))
        bullets_title.place(relx=0.63, rely=0.60, anchor="center")

        bullets = [
            "Use of a web filter (extension) to protect the web.",
            "Phishing detection and information gathering chatbot for given URL.",
            "Detection of Harmful mobile apks.",
        ]

        bullets_frame = tk.Frame(self.overlay, bg=COLORS['primary_bg'])
        bullets_frame.place(relx=0.63, rely=0.74, anchor="center")

        for i, line in enumerate(bullets):
            dot = tk.Canvas(bullets_frame, width=10, height=10, bg=COLORS['primary_bg'], highlightthickness=0)
            dot.grid(row=i, column=0, padx=(0, 8), pady=6, sticky="n")
            dot.create_oval(2, 2, 8, 8, fill="#2b2a6b", outline="")
            tk.Label(bullets_frame, text=line, bg=COLORS['primary_bg'], fg=COLORS['text_dark'], font=FONTS['body'], wraplength=420, justify="left").grid(row=i, column=1, sticky="w")

    # ----- Background -----
    def _redraw_background(self, _event=None) -> None:
        c = self.background_canvas
        c.delete("all")
        w, h = c.winfo_width(), c.winfo_height()

        # soft right-bottom blob
        c.create_oval(w * 0.45, h * 0.55, w * 1.15, h * 1.25, fill=COLORS['background_blob'], outline="")
        # keep overlay sized
        c.create_window(0, 0, anchor="nw", window=self.overlay, tags=("overlay",))
        c.tag_raise("overlay")
        self.overlay.update_idletasks()
        c.itemconfig("overlay", width=w, height=h)

    # ----- Actions -----
    def _on_home(self) -> None:
        self.destroy()
    
    def _on_contact(self) -> None:
        from .contact_window import ContactWindow
        ContactWindow(self.master)
