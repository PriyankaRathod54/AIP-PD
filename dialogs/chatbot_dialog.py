"""
Chatbot dialog for CyberDefense application
"""

import tkinter as tk
from tkinter import messagebox
import random

from config import COLORS, FONTS
from services import ChatbotService


class ChatbotDialog(tk.Toplevel):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title("Phishing Chatbot")
        self.configure(bg=COLORS['primary_bg'])
        self.resizable(True, True)
        
        # Center the dialog
        from utils import center_window
        center_window(self, 600, 550, parent=master)
        
        # Menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear Chat", command=self._clear_chat)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)
        
        # Options menu
        options_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=options_menu)
        
        # Font submenu
        font_menu = tk.Menu(options_menu, tearoff=0)
        options_menu.add_cascade(label="Font", menu=font_menu)
        font_menu.add_command(label="Default", command=lambda: self._change_font("Segoe UI"))
        font_menu.add_command(label="Times", command=lambda: self._change_font("Times New Roman"))
        font_menu.add_command(label="System", command=lambda: self._change_font("System"))
        font_menu.add_command(label="Helve", command=lambda: self._change_font("Helvetica"))
        font_menu.add_command(label="Fixedsys", command=lambda: self._change_font("Fixedsys"))
        
        # Color Theme submenu
        color_menu = tk.Menu(options_menu, tearoff=0)
        options_menu.add_cascade(label="Color Theme", menu=color_menu)
        color_menu.add_command(label="Light", command=lambda: self._change_color_theme("Light"))
        color_menu.add_command(label="Dark", command=lambda: self._change_color_theme("Dark"))
        color_menu.add_command(label="Blue", command=lambda: self._change_color_theme("Blue"))
        color_menu.add_command(label="Green", command=lambda: self._change_color_theme("Green"))
        
        # Other menu
        other_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Other", menu=other_menu)
        other_menu.add_command(label="About", command=self._show_about)
        
        # Main chat display area
        self.chat_frame = tk.Frame(self, bg=COLORS['chat_bg'], relief=tk.SOLID, bd=1)
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=25)
        
        # Chat text widget with scrollbar
        self.chat_text = tk.Text(self.chat_frame, bg=COLORS['chat_bg'], fg=COLORS['primary_bg'], 
                                font=FONTS['chat'], state=tk.DISABLED,
                                wrap=tk.WORD, relief=tk.FLAT, bd=0)
        self.chat_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar for chat
        scrollbar = tk.Scrollbar(self.chat_frame, orient=tk.VERTICAL, command=self.chat_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_text.config(yscrollcommand=scrollbar.set)
        
        # Message input area
        input_frame = tk.Frame(self, bg=COLORS['primary_bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Message entry field
        self.message_entry = tk.Entry(input_frame, font=("Segoe UI", 14), 
                                     bg="#f0f0f0", relief=tk.SOLID, bd=1)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.message_entry.bind("<Return>", self._send_message)
        
        # Send button
        send_button = tk.Button(input_frame, text="Send", 
                              font=("Segoe UI", 10, "bold"),
                              bg=COLORS['chat_bg'], fg=COLORS['primary_bg'], 
                              relief=tk.FLAT, padx=20, pady=5,
                              command=self._send_message)
        send_button.pack(side=tk.RIGHT)
        
        # Status bar
        status_frame = tk.Frame(self, bg=COLORS['primary_bg'])
        status_frame.pack(fill=tk.X, padx=10, pady=(0, 5))
        
        self.status_label = tk.Label(status_frame, text="No messages sent.", 
                                   font=("Segoe UI", 8), 
                                   bg=COLORS['primary_bg'], fg="#808080", anchor="w")
        self.status_label.pack(side=tk.LEFT)
        
        # System status (green text)
        self.system_status = tk.Label(status_frame, text="2MB 1.23", 
                                     font=("Segoe UI", 8), 
                                     bg=COLORS['primary_bg'], fg="#00aa00", anchor="w")
        self.system_status.pack(side=tk.LEFT, padx=(20, 0))
        
        # Initialize message count
        self.message_count = 0
        
        # Initialize conversation context
        self.conversation_context = []
        
        # Initialize with default bot message
        self._add_message("Bot", "Hi there", "#e0e0e0")
        
        # Add some helpful tips after a short delay
        self.after(2000, self._show_initial_tips)
        
        # Make modal
        self.transient(master)
        self.grab_set()
    
    def _send_message(self, event=None):
        """Send a message to the chatbot"""
        message = self.message_entry.get().strip()
        if not message:
            return
        
        # Add user message to chat
        self._add_message("You", message, COLORS['primary_bg'])
        
        # Store conversation context
        self.conversation_context.append(("user", message))
        
        # Generate bot response with context awareness
        response = ChatbotService.generate_response(message, self.conversation_context)
        self._add_message("Bot", response, "#e0e0e0")
        
        # Store bot response in context
        self.conversation_context.append(("bot", response))
        
        # Clear input and update status
        self.message_entry.delete(0, tk.END)
        self.message_count += 1
        self.status_label.config(text=f"{self.message_count} messages sent.")
        
        # Update system status with some dynamic info
        memory_usage = f"{random.randint(1, 5)}MB {random.uniform(1.0, 2.5):.2f}"
        self.system_status.config(text=memory_usage)
    
    def _add_message(self, sender, message, color):
        """Add a message to the chat display"""
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_text.config(state=tk.DISABLED)
        self.chat_text.see(tk.END)
    
    def _clear_chat(self):
        """Clear all chat messages"""
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.delete(1.0, tk.END)
        self.chat_text.config(state=tk.DISABLED)
        self.message_count = 0
        self.conversation_context = []
        self.status_label.config(text="No messages sent.")
        self.system_status.config(text="2MB 1.23")
        # Add default bot message back
        self._add_message("Bot", "Hi there", "#e0e0e0")
    
    def _change_font(self, font_name):
        """Change the font of the chat text"""
        self.chat_text.config(font=(font_name, 10))
    
    def _change_color_theme(self, theme):
        """Change the color theme of the chatbot"""
        if theme == "Dark":
            self.chat_frame.config(bg="#1a1a1a")
            self.chat_text.config(bg="#1a1a1a", fg=COLORS['primary_bg'])
        elif theme == "Blue":
            self.chat_frame.config(bg="#1e3a8a")
            self.chat_text.config(bg="#1e3a8a", fg=COLORS['primary_bg'])
        elif theme == "Green":
            self.chat_frame.config(bg="#166534")
            self.chat_text.config(bg="#166534", fg=COLORS['primary_bg'])
        else:  # Light
            self.chat_frame.config(bg="#f0f0f0")
            self.chat_text.config(bg="#f0f0f0", fg="#000000")
    
    def _show_settings(self):
        """Show settings dialog"""
        messagebox.showinfo("Settings", "Chatbot settings coming soon!")
    
    def _show_initial_tips(self):
        """Show initial helpful tips"""
        if self.message_count == 0:  # Only show if no messages have been sent yet
            self._add_message("Bot", "I can help you with cybersecurity topics like phishing, passwords, malware, and online safety. What would you like to know?", "#e0e0e0")
    
    def _show_about(self):
        """Show about dialog"""
        messagebox.showinfo("About", "Phishing Chatbot v1.0\nCybersecurity Assistant")
