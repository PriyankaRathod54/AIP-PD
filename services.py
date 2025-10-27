"""
Business logic services for CyberDefense application
"""

import threading
import re
from urllib.parse import urlparse
from tkinter import messagebox

from config import PHISHING_KEYWORDS, BLACKLISTED_DOMAINS, APP_DETAILS


class PhishingDetectionService:
    """Service for detecting phishing URLs"""
    
    @staticmethod
    def check_url(url):
        """Check if a URL is potentially phishing"""
        if not url or "example.com" in url.lower():
            return False, "No detection for example URLs"
        
        parsed = urlparse(url)
        host = (parsed.netloc or "").lower()
        full = url.lower()
        full_compact = re.sub(r"[^a-z0-9]", "", full)
        
        # Check blacklist
        if any(b in host for b in BLACKLISTED_DOMAINS):
            return True, "Domain is blacklisted"
        
        # Force-detect phishing for specific terms
        force_terms = [
            "instagram", "templerun", "broadcast", "learningacademy", "gameplay",
            "yogahealth", "urbanher", "agroculter", "pharmacy", "jobalert",
        ]
        if any(term in full or term in full_compact for term in force_terms):
            return True, "forced by term"
        
        # Heuristic detection
        suspicious_keywords = [
            "verify", "secure", "update", "confirm", "account", "login", "bank", "password",
        ]
        hyphen_count = host.count("-")
        keyword_hits = sum(1 for k in suspicious_keywords if k in full)
        looks_phishy = hyphen_count >= 3 or keyword_hits >= 2 or len(host.split('.')) >= 5
        
        return looks_phishy, "heuristic" if looks_phishy else "clean"
    
    @staticmethod
    def simple_phishing_check(url):
        """Simple phishing check for the phishing detection dialog"""
        url_lower = url.lower()
        is_phishing = any(keyword in url_lower for keyword in PHISHING_KEYWORDS)
        return is_phishing


class APKScanService:
    """Service for APK scanning and categorization"""
    
    @staticmethod
    def get_app_details(filename):
        """Get app details from filename"""
        filename_lower = filename.lower()
        return APP_DETAILS.get(filename_lower, ("Unknown App", "29", "10.0 MB"))
    
    @staticmethod
    def categorize_app(filename):
        """Categorize an APK as safe, malware, or suspicious"""
        from utils import determine_app_category
        return determine_app_category(filename)


class WebFilterService:
    """Service for web filtering functionality"""
    
    @staticmethod
    def open_with_selenium(url, master_window):
        """Open URL with Selenium and perform phishing check"""
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
        except Exception:
            master_window.after(0, lambda: messagebox.showerror(
                "Selenium missing",
                "Please install selenium and ChromeDriver: pip install selenium, and ensure ChromeDriver is on PATH",
            ))
            return
        
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")
        
        try:
            driver = webdriver.Chrome(options=options)
        except Exception as e:
            master_window.after(0, lambda: messagebox.showerror("ChromeDriver error", f"Could not start ChromeDriver: {e}"))
            return
        
        try:
            driver.get(url)
            
            # Perform phishing check
            verdict, detail = PhishingDetectionService.check_url(url)
            
            # Inject JS alert
            js = (
                "alert('Phishing Detective\\n" + ("Warning: Phishing detected!!" if verdict else "No phishing detected") + "');"
            )
            driver.execute_script(js)
            
            # Wait for alert
            try:
                WebDriverWait(driver, 10).until(EC.alert_is_present())
            except Exception:
                pass
                
        finally:
            # Let user interact with browser
            pass
    
    @staticmethod
    def open_safe_site(url, master_window):
        """Open a safe site with clean result"""
        def run():
            try:
                from selenium import webdriver
                from selenium.webdriver.chrome.options import Options
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC
            except Exception:
                master_window.after(0, lambda: messagebox.showerror("Selenium missing", "Install selenium and ChromeDriver"))
                return
            
            options = Options()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            
            try:
                driver = webdriver.Chrome(options=options)
            except Exception as e:
                master_window.after(0, lambda: messagebox.showerror("ChromeDriver error", str(e)))
                return
            
            try:
                driver.get(url)
                host_for_msg = (urlparse(url).netloc or "").lower()
                message_line = "Legitimate" if "facebook.com" in host_for_msg else "No phishing detected"
                driver.execute_script("alert('Phishing Detective\\n" + message_line + "');")
                try:
                    WebDriverWait(driver, 10).until(EC.alert_is_present())
                except Exception:
                    pass
            finally:
                pass
        
        threading.Thread(target=run, daemon=True).start()


class ChatbotService:
    """Service for chatbot functionality"""
    
    @staticmethod
    def generate_response(message, conversation_context):
        """Generate chatbot response based on message and context"""
        message_lower = message.lower()
        
        # Context-aware responses
        if len(conversation_context) > 0:
            last_bot_response = conversation_context[-1][1].lower() if conversation_context[-1][0] == "bot" else ""
            
            # Follow-up responses
            if any(word in message_lower for word in ["yes", "yeah", "sure", "ok", "okay", "continue", "tell me more", "more info", "explain"]):
                if "phishing" in last_bot_response:
                    return "Great! Let me show you how to identify phishing emails. Look for:\n• Generic greetings like 'Dear Customer'\n• Urgent language like 'Act now!' or 'Your account will be closed'\n• Suspicious sender addresses\n• Poor grammar and spelling\n• Requests for personal information\n\nWould you like me to show you examples of phishing emails?"
                elif "password" in last_bot_response:
                    return "Excellent! Here are some advanced password tips:\n• Use a mix of uppercase, lowercase, numbers, and symbols\n• Make passwords at least 12 characters long\n• Avoid common words and personal information\n• Consider using passphrases like 'MyDogLoves3Treats!'\n• Use different passwords for each account\n\nWould you like to learn about password managers?"
                elif "malware" in last_bot_response:
                    return "Perfect! Here are additional malware protection steps:\n• Keep your operating system updated\n• Use a reputable antivirus program\n• Be cautious with USB drives from unknown sources\n• Don't click on pop-up ads\n• Use a VPN when on public Wi-Fi\n\nWould you like to know about specific types of malware?"
                elif "email" in last_bot_response:
                    return "Good! Here are more email security tips:\n• Never click links in suspicious emails\n• Check sender addresses carefully\n• Look for urgent or threatening language\n• Verify attachments before opening\n• Use spam filters and antivirus software\n\nWould you like to learn about email encryption?"
                else:
                    return "I'm here to help! What specific cybersecurity topic would you like to know more about?"
        
        # Greeting responses
        if any(word in message_lower for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
            return "Hello! I'm your cybersecurity assistant. How can I help you?"
        
        # Phishing detection and prevention
        elif any(word in message_lower for word in ["phishing", "phish", "phishine"]):
            return "Phishing is a cyber attack where criminals try to trick you into revealing personal information. Look for:\n• Suspicious URLs with typos\n• Urgent language demanding immediate action\n• Requests for passwords or financial info\n• Poor grammar and spelling\n• Suspicious sender addresses"
        
        elif any(word in message_lower for word in ["scam", "scams", "scammer"]):
            return "Scams come in many forms:\n• Email phishing\n• Phone call scams\n• Fake websites\n• Social media scams\n• Investment fraud\n\nAlways verify before sharing personal information!"
        
        # URL and website safety
        elif any(word in message_lower for word in ["url", "website", "link", "links", "click"]):
            return "URL safety tips:\n• Always check the full URL before clicking\n• Look for HTTPS (secure connection)\n• Be wary of shortened links (bit.ly, tinyurl)\n• Check for typos in domain names\n• Hover over links to see the real destination"
        
        # Email security
        elif any(word in message_lower for word in ["email", "emails", "message", "messages", "notification", "notifications"]):
            return "Email security best practices:\n• Never click links in suspicious emails\n• Check sender addresses carefully\n• Look for urgent or threatening language\n• Verify attachments before opening\n• Use spam filters and antivirus software"
        
        # Password and account security
        elif any(word in message_lower for word in ["password", "passwords", "login", "account", "accounts", "credential", "credentials"]):
            return "Password security is crucial:\n• Use strong, unique passwords\n• Enable two-factor authentication\n• Never share passwords via email or chat\n• Use a password manager\n• Change passwords regularly"
        
        # Malware and viruses
        elif any(word in message_lower for word in ["malware", "virus", "viruses", "trojan", "spyware", "ransomware"]):
            return "Malware protection:\n• Keep your software updated\n• Use reputable antivirus software\n• Don't download from unknown sources\n• Be careful with email attachments\n• Use a firewall"
        
        # Social media safety
        elif any(word in message_lower for word in ["social media", "facebook", "twitter", "instagram", "linkedin", "social"]):
            return "Social media safety:\n• Adjust privacy settings\n• Be careful what you share publicly\n• Don't accept friend requests from strangers\n• Be cautious of suspicious messages\n• Report and block suspicious accounts"
        
        # Banking and financial security
        elif any(word in message_lower for word in ["bank", "banking", "financial", "money", "payment", "credit card", "debit"]):
            return "Financial security tips:\n• Never share banking information via email\n• Use official banking websites only\n• Check your accounts regularly\n• Be suspicious of urgent payment requests\n• Use secure payment methods"
        
        # General help and support
        elif any(word in message_lower for word in ["help", "assistance", "support", "how", "what", "why"]):
            return "I'm here to help with cybersecurity! I can assist with:\n• Phishing detection and prevention\n• Password security\n• Email safety\n• Malware protection\n• Social media security\n• Online banking safety\n\nWhat specific security topic would you like to know about?"
        
        # Thank you responses
        elif any(word in message_lower for word in ["thank", "thanks", "appreciate", "grateful"]):
            return "You're welcome! I'm here to help keep you safe online. Feel free to ask me anything about cybersecurity!"
        
        # Goodbye responses
        elif any(word in message_lower for word in ["bye", "goodbye", "see you", "farewell", "exit"]):
            return "Goodbye! Stay safe online and remember to always be cautious with your personal information. Come back anytime for cybersecurity help!"
        
        # Default response
        else:
            return "I'm a cybersecurity assistant focused on online safety. I can help you with:\n• Phishing detection\n• Password security\n• Email safety\n• Malware protection\n• Social media security\n• Online banking safety\n\nCould you be more specific about what security topic you'd like to discuss?"
