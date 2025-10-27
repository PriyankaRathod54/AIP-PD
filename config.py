"""
Configuration settings for CyberDefense application
"""

# Window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 650

# Color scheme
COLORS = {
    'primary_bg': '#ffffff',
    'accent_blue': '#0078D4',
    'accent_purple': '#5c2d91',
    'text_dark': '#333333',
    'text_light': '#666666',
    'button_bg': '#f0f0f0',
    'button_active': '#e0e0e0',
    'illustration_bg': '#f5f7fa',
    'illustration_inner': '#e6e9f0',
    'background_blob': '#f0f7ff',
    'background_sweep': '#f8f9fa',
    'decorative_bar': '#e1e5eb'
}

# Font settings
FONTS = {
    'brand': ('Segoe UI', 18, 'bold'),
    'title': ('Segoe UI', 24, 'bold'),
    'button': ('Segoe UI', 10, 'normal'),
    'normal': ('Segoe UI', 9, 'normal'),
    'small': ('Segoe UI', 8, 'normal')
}

# Other constants
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB in bytes
SUPPORTED_EXTENSIONS = ['.apk']

# Phishing detection
PHISHING_KEYWORDS = [
    'login', 'signin', 'account', 'verify', 'banking',
    'password', 'update', 'security', 'alert', 'suspended',
    'limited', 'verify', 'confirm', 'billing', 'invoice',
    'payment', 'urgent', 'action', 'required', 'immediately'
]

# Blacklisted domains
BLACKLISTED_DOMAINS = [
    'example-malicious.com',
    'phishing-site.org',
    'fake-login.net',
    'scam-website.xyz',
    'malware-download.biz'
]

# Sample app details for demonstration
APP_DETAILS = {
    'safe_app.apk': ('Safe App', 'API 28', '12.5 MB'),
    'malware_app.apk': ('Malware App', 'API 25', '8.2 MB'),
    'suspicious_app.apk': ('Suspicious App', 'API 29', '15.7 MB'),
}

# Contact information
CONTACTS = [
    {
        'name': 'Support Team',
        'email': 'support@cyberdefense.com',
        'phone': '+1 (555) 123-4567',
        'department': 'Technical Support'
    },
    {
        'name': 'Security Team',
        'email': 'security@cyberdefense.com',
        'phone': '+1 (555) 987-6543',
        'department': 'Security Operations'
    },
    {
        'name': 'General Inquiries',
        'email': 'info@cyberdefense.com',
        'phone': '+1 (555) 000-0000',
        'department': 'Customer Service'
    }
]

# Popular websites for web filter
POPULAR_SITES = [
    {
        'name': 'Google',
        'url': 'https://www.google.com',
        'category': 'Search Engine'
    },
    {
        'name': 'YouTube',
        'url': 'https://www.youtube.com',
        'category': 'Video Sharing'
    },
    {
        'name': 'Wikipedia',
        'url': 'https://www.wikipedia.org',
        'category': 'Encyclopedia'
    },
    {
        'name': 'GitHub',
        'url': 'https://www.github.com',
        'category': 'Development'
    },
    {
        'name': 'LinkedIn',
        'url': 'https://www.linkedin.com',
        'category': 'Professional'
    },
    {
        'name': 'Twitter',
        'url': 'https://www.twitter.com',
        'category': 'Social Media'
    }
]
