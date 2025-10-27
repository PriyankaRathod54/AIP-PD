"""
Standalone contact window - no extra empty window
"""

import tkinter as tk
from config import WINDOW_WIDTH, WINDOW_HEIGHT, COLORS, FONTS, CONTACTS
from utils import center_window, create_link, create_clickable_email, create_clickable_phone


class StandaloneContactWindow(tk.Tk):
    """Standalone contact window that doesn't require a parent"""
    
    def __init__(self):
        super().__init__()
        self.title("CyberDefense - Contact")
        self.configure(bg=COLORS['primary_bg'])
        self.minsize(900, 560)

        # Center the window
        center_window(self, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.canvas = tk.Canvas(self, bg=COLORS['primary_bg'], highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self._redraw_bg)

        self.overlay = tk.Frame(self.canvas, bg=COLORS['primary_bg'])
        self.canvas.create_window(0, 0, anchor="nw", window=self.overlay, tags=("overlay",))

        self._build_header()
        self._build_layout()

    def _build_header(self) -> None:
        brand = tk.Label(self.overlay, text="CyberDefense", bg=COLORS['primary_bg'], fg=COLORS['accent_purple'], font=FONTS['brand'])
        brand.place(relx=0.07, rely=0.08, anchor="w")

        links = tk.Frame(self.overlay, bg=COLORS['primary_bg'])
        links.place(relx=0.55, rely=0.08)

        create_link(links, "Home", self.destroy).grid(row=0, column=0, padx=(0, 24))
        create_link(links, "About", self._on_about).grid(row=0, column=1, padx=(0, 24))
        create_link(links, "Exit", self.destroy).grid(row=0, column=2)

    def _build_layout(self) -> None:
        # Left text block
        title = tk.Label(self.overlay, text="Contact us", bg=COLORS['primary_bg'], fg="#2b2a6b", font=("Segoe UI", 36, "bold"))
        title.place(relx=0.27, rely=0.23, anchor="center")
        subtitle = tk.Label(self.overlay, text="We are here to help you", bg=COLORS['primary_bg'], fg="#7a7a7a", font=FONTS['subtitle'])
        subtitle.place(relx=0.27, rely=0.30, anchor="center")

        # Developer contacts list
        block = tk.Frame(self.overlay, bg=COLORS['primary_bg'])
        block.place(relx=0.27, rely=0.60, anchor="center")

        for i, (name, email, phone) in enumerate(CONTACTS):
            # Name label
            name_lbl = tk.Label(block, text=name, bg=COLORS['primary_bg'], fg="#2b2a6b", font=("Segoe UI", 16, "bold"))
            name_lbl.grid(row=i * 3, column=0, sticky="w", pady=(0, 2))
            
            # Email label (clickable)
            email_frame = tk.Frame(block, bg=COLORS['primary_bg'])
            email_frame.grid(row=i * 3 + 1, column=0, sticky="w", pady=(0, 2))
            
            email_prefix = tk.Label(email_frame, text="📧 ", bg=COLORS['primary_bg'], fg="#8c8c8c", font=FONTS['body'])
            email_prefix.pack(side=tk.LEFT)
            
            email_lbl = create_clickable_email(email_frame, email)
            email_lbl.pack(side=tk.LEFT)
            
            # Phone label (clickable)
            phone_frame = tk.Frame(block, bg=COLORS['primary_bg'])
            phone_frame.grid(row=i * 3 + 2, column=0, sticky="w", pady=(0, 14))
            
            phone_prefix = tk.Label(phone_frame, text="📞 ", bg=COLORS['primary_bg'], fg="#8c8c8c", font=FONTS['body'])
            phone_prefix.pack(side=tk.LEFT)
            
            phone_lbl = create_clickable_phone(phone_frame, phone)
            phone_lbl.pack(side=tk.LEFT)

        # Instructions
        instructions = tk.Label(
            self.overlay,
            text="Click on the blue underlined emails to open your email client\nClick on the blue underlined phone numbers to dial",
            bg=COLORS['primary_bg'],
            fg="#2b2a6b",
            font=("Segoe UI", 12),
            justify="center"
        )
        instructions.place(relx=0.27, rely=0.85, anchor="center")

        # Right illustration panel
        illo = tk.Canvas(self.overlay, width=430, height=360, bg="#e9ebff", highlightthickness=0)
        illo.place(relx=0.70, rely=0.55, anchor="center")
        # Simple person with headset illustration (abstract)
        illo.create_oval(260, 90, 320, 150, fill="#2b2a6b", outline="")  # hair
        illo.create_oval(230, 120, 300, 190, fill="#ffcc99", outline="")  # face
        illo.create_rectangle(200, 190, 330, 300, fill="#ffb44c", outline="")  # body
        illo.create_line(180, 150, 230, 155, fill="#2b2a6b", width=6)  # headset band
        illo.create_oval(215, 155, 235, 175, fill="#2b2a6b", outline="")  # earcup
        illo.create_line(235, 170, 260, 185, fill="#2b2a6b", width=4)  # mic boom
        illo.create_rectangle(160, 300, 360, 325, fill="#6fa8ff", outline="")  # laptop base
        illo.create_oval(245, 307, 275, 322, fill="#cde2ff", outline="")  # trackpad

    def _redraw_bg(self, _e=None) -> None:
        c = self.canvas
        c.delete("bg")
        w, h = c.winfo_width(), c.winfo_height()
        c.create_oval(w * 0.45, h * 0.55, w * 1.15, h * 1.25, fill="#ff8791", outline="", tags="bg")
        c.create_window(0, 0, anchor="nw", window=self.overlay, tags=("overlay",))
        c.tag_raise("overlay")
        self.overlay.update_idletasks()
        c.itemconfig("overlay", width=w, height=h)
    
    def _on_about(self) -> None:
        # Simple about dialog
        import tkinter.messagebox as messagebox
        messagebox.showinfo("About", "CyberDefense Contact Window\nEnhanced with clickable emails and phone numbers!")


def main():
    """Run the standalone contact window"""
    app = StandaloneContactWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
