"""
Main entry point for CyberDefense application
"""

from main_window import CyberDefenseApp


def main() -> None:
    """Main function to start the CyberDefense application"""
    app = CyberDefenseApp()
    app.mainloop()


if __name__ == "__main__":
    main()