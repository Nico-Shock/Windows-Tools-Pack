import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import sys

PROGRAM_LIST = [
    "- Win11 Debloat Script by Raphire",
    "- UltraUXThemePatcher",
    "- Mica for Everyone .NET Core 3.1",
    "- StartAllBack",
    "- ExplorerBlurMica",
    "- Windhawk",
    "- Seelen UI"
]

class InstallationGUI:
    def __init__(self):
        """Initialize main application window"""
        self.root = ttk.Window(themename="darkly")
        self.setup_base_gui()
        self.create_main_screen()

    def setup_base_gui(self):
        """Configure base window settings"""
        self.root.title("Windows Customization Suite")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.center_window()

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (400 // 2)
        self.root.geometry(f'+{x}+{y}')

    def create_main_screen(self):
        """Create initial screen with program list"""
        self.clear_window()
        
        # Main content container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        # Header section
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill='x', pady=10)
        
        ttk.Label(
            header_frame,
            text="Windows Customization Script\n(Windows 10/11 Only)",
            font=('Segoe UI', 16, 'bold'),
            justify='center'
        ).pack(pady=5)

        # Program list display
        program_text = "\n".join(PROGRAM_LIST)
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill='both', expand=True, pady=15)
        
        ttk.Label(
            list_frame,
            text=program_text,
            font=('Consolas', 12),
            foreground='#cccccc',
            justify='left'
        ).pack(anchor='w')

        # Button container with swapped positions
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(side='bottom', pady=20, fill='x', expand=False)

        # Cancel button (left side)
        ttk.Button(
            btn_frame,
            text="Cancel",
            command=sys.exit,
            bootstyle=DANGER,
            width=15
        ).pack(side='left', padx=10)

        # Continue button (right side)
        ttk.Button(
            btn_frame,
            text="Continue",
            command=self.check_winget,
            bootstyle=SUCCESS,
            width=15
        ).pack(side='right', padx=10)

    def check_winget(self):
        """Verify Winget installation status"""
        try:
            subprocess.run(
                ["winget", "--version"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
            self.show_winget_status(True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.show_winget_status(False)

    def show_winget_status(self, installed):
        """Display Winget status screen"""
        self.clear_window()

        # Main content container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        # Status header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill='x', pady=10)
        
        ttk.Label(
            header_frame,
            text="System Requirements Check",
            font=('Segoe UI', 16, 'bold'),
            justify='center'
        ).pack()

        # Status message
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill='both', expand=True, pady=15)
        
        status_text = "✓ Winget is installed" if installed else "✗ Winget not found!"
        status_color = "#2ecc71" if installed else "#e74c3c"
        
        ttk.Label(
            status_frame,
            text=status_text,
            font=('Segoe UI', 14, 'bold'),
            foreground=status_color,
            justify='center'
        ).pack(pady=20)

        # Action buttons at bottom
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(side='bottom', pady=20, fill='x', expand=False)

        if installed:
            ttk.Button(
                btn_frame,
                text="Start Installation",
                command=self.start_installation,
                bootstyle=SUCCESS,
                width=20
            ).pack()
        else:
            ttk.Button(
                btn_frame,
                text="Install Winget",
                command=self.install_winget,
                bootstyle=DANGER,
                width=20
            ).pack(side='left', padx=10)

            ttk.Button(
                btn_frame,
                text="Go Back",
                command=self.create_main_screen,
                bootstyle=SECONDARY,
                width=20
            ).pack(side='right', padx=10)

    def clear_window(self):
        """Remove all widgets from current window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def install_winget(self):
        """Install Winget package manager"""
        ps_script = '''
        $progressPreference = 'silentlyContinue'
        Invoke-WebRequest -Uri https://aka.ms/getwinget -OutFile winget.msixbundle
        Add-AppxPackage winget.msixbundle
        '''
        subprocess.run(["powershell", "-Command", ps_script], shell=True)
        self.check_winget()

    def start_installation(self):
        """Start main installation process"""
        print("Starting installation process...")
        self.root.destroy()

if __name__ == "__main__":
    app = InstallationGUI()
    app.root.mainloop()
