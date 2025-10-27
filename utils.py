"""
Utility functions for CyberDefense application
"""

import os
import hashlib
from urllib.parse import urlparse
import re


def center_window(window, width, height, parent=None):
    """Center a window on screen or relative to parent"""
    window.update_idletasks()
    
    if parent:
        x = parent.winfo_rootx() + (parent.winfo_width() // 2) - (width // 2)
        y = parent.winfo_rooty() + (parent.winfo_height() // 2) - (height // 2)
    else:
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
    
    window.geometry(f"{width}x{height}+{x}+{y}")


def normalize_url(candidate):
    """Normalize a URL by adding protocol if missing"""
    if not candidate:
        return ""
    if not re.match(r"^https?://", candidate, re.IGNORECASE):
        candidate = "http://" + candidate
    try:
        parsed = urlparse(candidate)
        return candidate if parsed.netloc else ""
    except Exception:
        return ""


def generate_app_details_from_filename(filename):
    """Generate consistent app details based on filename hash"""
    app_name = filename.replace('.apk', '').replace('_', ' ').title()
    
    # Generate random but consistent details based on filename
    hash_obj = hashlib.md5(filename.encode())
    hash_int = int(hash_obj.hexdigest()[:8], 16)
    
    # Generate SDK version (25-30)
    sdk = str(25 + (hash_int % 6))
    
    # Generate size (5-20 MB)
    size_mb = 5 + (hash_int % 16)
    size = f"{size_mb}.{hash_int % 10} MB"
    
    return app_name, sdk, size, hash_int


def create_sample_apks(sample_dir="sample_apks"):
    """Create sample APK files for testing"""
    if not os.path.exists(sample_dir):
        os.makedirs(sample_dir)
    
    # Import here to avoid circular imports
    from config import SAFE_APKS, MALWARE_APKS, SUSPICIOUS_APKS, ADDITIONAL_APKS
    
    all_apks = SAFE_APKS + MALWARE_APKS + SUSPICIOUS_APKS + ADDITIONAL_APKS
    
    for apk in all_apks:
        apk_path = os.path.join(sample_dir, apk)
        if not os.path.exists(apk_path):
            with open(apk_path, 'w') as f:
                f.write("Dummy APK file for testing")


def determine_app_category(filename):
    """Determine if an APK is safe, malware, or suspicious based on filename"""
    filename_lower = filename.lower()
    
    # Import here to avoid circular imports
    from config import SAFE_APKS, MALWARE_APKS, SUSPICIOUS_APKS
    
    # Check for safe apps
    safe_keywords = ["amazon", "prime", "calculator", "youtube", "whatsapp", "facebook", "google", "learning"]
    if any(safe in filename_lower for safe in safe_keywords):
        return "safe"
    
    # Check for malware apps
    malware_keywords = ["malware", "광주버스", "internet", "scanner", "trojan", "keylogger", "spyware", "amazan"]
    if any(malware in filename_lower for malware in malware_keywords):
        return "malware"
    
    # Check for suspicious apps
    suspicious_keywords = ["money", "bank", "help", "health", "social"]
    if any(suspicious in filename_lower for suspicious in suspicious_keywords):
        return "suspicious"
    
    return "generic"


def create_link(parent, text, command, **kwargs):
    """Create a clickable link label"""
    import tkinter as tk
    from config import COLORS, FONTS
    
    label = tk.Label(
        parent,
        text=text,
        bg=kwargs.get('bg', COLORS['primary_bg']),
        fg=kwargs.get('fg', COLORS['link_blue']),
        cursor="hand2",
        font=kwargs.get('font', FONTS['link']),
    )
    label.bind("<Button-1>", lambda _e: command())
    return label


def create_clickable_email(parent, email, **kwargs):
    """Create a clickable email link"""
    import tkinter as tk
    import webbrowser
    from config import COLORS, FONTS
    
    label = tk.Label(
        parent,
        text=email,
        bg=kwargs.get('bg', COLORS['primary_bg']),
        fg=COLORS['link_blue'],
        cursor="hand2",
        font=kwargs.get('font', FONTS['body']),
        underline=True
    )
    
    def open_email():
        try:
            webbrowser.open(f"mailto:{email}")
        except Exception as e:
            print(f"Could not open email client: {e}")
    
    label.bind("<Button-1>", lambda _e: open_email())
    label.bind("<Enter>", lambda _e: label.config(fg="#1a73e8"))  # Darker blue on hover
    label.bind("<Leave>", lambda _e: label.config(fg=COLORS['link_blue']))  # Original blue on leave
    
    return label


def create_clickable_phone(parent, phone, **kwargs):
    """Create a clickable phone number link"""
    import tkinter as tk
    import webbrowser
    from config import COLORS, FONTS
    
    label = tk.Label(
        parent,
        text=phone,
        bg=kwargs.get('bg', COLORS['primary_bg']),
        fg=COLORS['link_blue'],
        cursor="hand2",
        font=kwargs.get('font', FONTS['body']),
        underline=True
    )
    
    def dial_phone():
        try:
            # Clean phone number for tel: protocol
            clean_phone = phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
            webbrowser.open(f"tel:{clean_phone}")
        except Exception as e:
            print(f"Could not open phone dialer: {e}")
    
    label.bind("<Button-1>", lambda _e: dial_phone())
    label.bind("<Enter>", lambda _e: label.config(fg="#1a73e8"))  # Darker blue on hover
    label.bind("<Leave>", lambda _e: label.config(fg=COLORS['link_blue']))  # Original blue on leave
    
    return label


def create_decorative_bar(canvas, x, y, w, h, color):
    """Create a decorative rounded bar on canvas"""
    r = h / 2
    canvas.create_oval(x, y, x + h, y + h, fill=color, outline="")
    canvas.create_rectangle(x + r, y, x + w - r, y + h, fill=color, outline="")
    canvas.create_oval(x + w - h, y, x + w, y + h, fill=color, outline="")
