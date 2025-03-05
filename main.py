import gi
gi.require_version(Gtk, 3.0)
from gi.repository import Gtk, Gdk
import subprocess
import sys

PROGRAM_LIST = [
    - Win11 Debloat Script by Raphire,
    - UltraUXThemePatcher,
    - Mica for Everyone .NET Core 3.1,
    - StartAllBack,
    - ExplorerBlurMica,
    - Windhawk,
    - Seelen UI
]

class InstallationGUI(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=Windows Customization Suite)
        self.set_default_size(600, 400)
        self.set_resizable(False)
        self.center_window()
        self.create_main_screen()

    def center_window(self):
        screen = self.get_screen()
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        window_width = 600
        window_height = 400
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.move(x, y)

    def create_main_screen(self):
        self.clear_window()

        main_frame = Gtk.VBox(spacing=10)
        main_frame.set_border_width(20)

        header_frame = Gtk.VBox()

        header_label = Gtk.Label()
        header_label.set_markup(<span weight=bold font_desc=Segoe UI 16>Windows Customization Script\n(Windows 10/11 Only)</span>)
        header_label.set_justify(Gtk.Justification.CENTER)
        header_frame.pack_start(header_label, False, False, 5)

        main_frame.pack_start(header_frame, False, False, 0)

        program_text = \n.join(PROGRAM_LIST)
        list_frame = Gtk.VBox()
        list_frame.set_margin_top(15)

        program_label = Gtk.Label(label=program_text)
        program_label.set_property(monospace, True)
        program_label.set_justify(Gtk.Justification.LEFT)
        program_label.set_alignment(0, 0.5)
        list_frame.pack_start(program_label, False, False, 0)
        main_frame.pack_start(list_frame, False, False, 0)


        btn_frame = Gtk.HBox(spacing=10)
        btn_frame.set_halign(Gtk.Align.END)
        btn_frame.set_margin_top(20)

        cancel_button = Gtk.Button(label=Cancel)
        cancel_button.connect(clicked, self.on_cancel_clicked)
        cancel_button.get_style_context().add_class(destructive-action)
        btn_frame.pack_start(cancel_button, False, False, 10)

        continue_button = Gtk.Button(label=Continue)
        continue_button.connect(clicked, self.on_continue_clicked)
        continue_button.get_style_context().add_class(suggested-action)
        btn_frame.pack_start(continue_button, False, False, 10)

        main_frame.pack_start(btn_frame, False, False, 0)

        self.add(main_frame)
        self.show_all()

    def check_winget(self):
        try:
            subprocess.run(
                [winget, --version],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
            self.show_winget_status(True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.show_winget_status(False)

    def show_winget_status(self, installed):
        self.clear_window()

        main_frame = Gtk.VBox(spacing=10)
        main_frame.set_border_width(20)

        header_frame = Gtk.VBox()

        header_label = Gtk.Label()
        header_label.set_markup(<span weight=bold font_desc=Segoe UI 16>System Requirements Check</span>)
        header_label.set_justify(Gtk.Justification.CENTER)
        header_frame.pack_start(header_label, False, False, 5)
        main_frame.pack_start(header_frame, False, False, 0)

        status_frame = Gtk.VBox()
        status_frame.set_margin_top(15)

        status_text = ✓ Winget is installed if installed else ✗ Winget not found!
        status_color_markup = <span weight=bold font_desc=Segoe UI 14 foreground={}>{}</span>.format(#2ecc71 if installed else #e74c3c, status_text)

        status_label = Gtk.Label()
        status_label.set_markup(status_color_markup)
        status_label.set_justify(Gtk.Justification.CENTER)
        status_frame.pack_start(status_label, False, False, 0)
        main_frame.pack_start(status_frame, False, False, 0)


        btn_frame = Gtk.HBox(spacing=10)
        btn_frame.set_halign(Gtk.Align.END)
        btn_frame.set_margin_top(20)

        if installed:
            start_install_button = Gtk.Button(label=Start Installation)
            start_install_button.connect(clicked, self.on_start_installation_clicked)
            start_install_button.get_style_context().add_class(suggested-action)
            btn_frame.pack_start(start_install_button, False, False, 10)
        else:
            install_winget_button = Gtk.Button(label=Install Winget)
            install_winget_button.connect(clicked, self.on_install_winget_clicked)
            install_winget_button.get_style_context().add_class(destructive-action)
            btn_frame.pack_start(install_winget_button, False, False, 10)

            go_back_button = Gtk.Button(label=Go Back)
            go_back_button.connect(clicked, self.on_go_back_clicked)
            go_back_button.get_style_context().add_class(secondary-action)
            btn_frame.pack_start(go_back_button, False, False, 10)

        main_frame.pack_start(btn_frame, False, False, 0)
        self.add(main_frame)
        self.show_all()


    def clear_window(self):
        for widget in self.get_children():
            self.remove(widget)

    def install_winget(self):
        ps_script = '''
        $progressPreference = silentlyContinue
        Invoke-WebRequest -Uri [https://aka.ms/getwinget](https://aka.ms/getwinget) -OutFile winget.msixbundle
        Add-AppxPackage winget.msixbundle
        '''
        subprocess.run([powershell, -Command, ps_script], shell=True)
        self.check_winget()

    def start_installation(self):
        print(Starting installation process...)
        self.destroy()

    def on_cancel_clicked(self, button):
        Gtk.main_quit()

    def on_continue_clicked(self, button):
        self.check_winget()

    def on_install_winget_clicked(self, button):
        self.install_winget()

    def on_go_back_clicked(self, button):
        self.create_main_screen()

    def on_start_installation_clicked(self, button):
        self.start_installation()


css = b"""
.program-list {
    font-family: Consolas;
    font-size: 12px;
    color: #cccccc;
}

.destructive-action {
    background-color: #e74c3c;
    color: white;
    border-radius: 5px;
    padding: 5px 10px;
}

.destructive-action:hover {
    background-color: #c0392b;
}

.suggested-action {
    background-color: #2ecc71;
    color: white;
    border-radius: 5px;
    padding: 5px 10px;
}

.suggested-action:hover {
    background-color: #27ae60;
}

.secondary-action {
    background-color: #3498db;
    color: white;
    border-radius: 5px;
    padding: 5px 10px;
}

.secondary-action:hover {
    background-color: #2980b9;
}
"""

if __name__ == __main__:
    app = InstallationGUI()

    style_provider = Gtk.CssProvider()
    style_provider.load_from_data(css)
    screen = Gdk.Screen.get_default()
    Gtk.StyleContext.add_provider_for_screen(
        screen,
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_USER
    )

    Gtk.main()
