import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk



class NextGenFirewallGUI:
    def __init__(self,root):
        self.root = root
        self.root.title("Sun City Firewalls LLC")
        self.root.set_theme("breeze")
        #self.root.tk_setPalette(background='#000000')
        tabControl = ttk.Notebook(self.root)

        self.tabs = {
            'Firewall': ttk.Frame(tabControl),
            'VPN': ttk.Frame(tabControl),
            'AI Tuning': ttk.Frame(tabControl),
            'Advanced Protection': ttk.Frame(tabControl),
            'Settings': ttk.Frame(tabControl),
        }

        for name, tab in self.tabs.items():
            tabControl.add(tab, text=name)

        style = ttk.Style()
        style.configure("TNotebook.Tab", foreground='#008996')
        tabControl.pack(expand=1, fill="both")

        self.setupFirewallTab()
        self.setupVPN()
        self.setupAITuning()
        self.setupAdvancedProtection()
        self.setupSettings()

        self.panicButton = False

        self.firewallRules = []

        self.root.mainloop()

        app_frame = ttk.Frame(self.root, width=100, height = 300, borderwidth = 5, relief = tk.RIDGE)
        app_frame.pack_propagate(False)
        app_frame.pack(side = 'left')

    def setupFirewallTab(self):
        tab = self.tabs['Firewall']
        #ttk.Label(
        app_frame = ttk.Frame(self.root, width=100, height=300, borderwidth=5,relief=tk.RIDGE)
        app_frame.pack_propagate(False)
        app_frame.pack(side = 'left')
        button = ttk.Button(app_frame, text = 'Firewall')
        button.pack()
        button = ttk.Button(app_frame, text = 'VPN')
        button.pack()
        button = ttk.Button(app_frame, text = 'HELP')
        button.pack()

    #def setupSettings(self):
def main():
    root = ThemedTk(theme="breeze", themebg=True)
    app = NextGenFirewallGUI(root)

if __name__ == "__main__":
    main()