"""
Dialog classes for CyberDefense application
"""

from .about_window import AboutWindow
from .contact_window import ContactWindow
from .web_filter_dialog import WebFilterDialog, WebFilterSitesWindow
from .scan_result_dialogs import (
    SafeResultDialog, 
    MalwareResultDialog, 
    SuspiciousResultDialog,
    ScanResultDialog,
    ScanResultDialog2,
    ScanResultDialog3,
    ScanResultDialog4
)
from .phishing_detection_dialog import PhishingDetectionDialog
from .chatbot_dialog import ChatbotDialog

__all__ = [
    'AboutWindow',
    'ContactWindow', 
    'WebFilterDialog',
    'WebFilterSitesWindow',
    'SafeResultDialog',
    'MalwareResultDialog',
    'SuspiciousResultDialog',
    'ScanResultDialog',
    'ScanResultDialog2', 
    'ScanResultDialog3',
    'ScanResultDialog4',
    'PhishingDetectionDialog',
    'ChatbotDialog'
]
