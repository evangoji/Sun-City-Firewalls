import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk



class NextGenFirewallGUI:
    def __init__(self,root):
        self.root = root
        self.root.title("Sun City Firewalls LLC")
        self.root.set_theme("breeze")
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

        #self.setupFirewall()
        #self.setupVPN()
        self.setupAITuning()
        #self.setupAdvancedProtection()
        #self.setupSettings()

        self.panicButton = False
        self.darkMode = False

        self.firewallRules = []

        self.root.mainloop()

        app_frame = ttk.Frame(self.root, width=100, height = 300, borderwidth = 5, relief = tk.RIDGE)
        app_frame.pack_propagate(False)
        app_frame.pack(side = 'left')

    def setupAITuning(self):
        tab = self.tabs['AI Auto Tuning']
        ttk.Label(tab, text="AI Auto Tuning", font=("Helvetica", 18, "bold"), foreground="#FF0000").pack(pady=20)

        snort_frame = ttk.Frame(tab)
        snort_frame.pack(pady=10)
        ttk.Label(snort_frame, text="Snort", font=("Helvetica", 12, "bold")).pack(anchor=tk.W)
        snort_switch = ttk.Checkbutton(snort_frame, text="Enable Snort", command=self.run_snort)
        snort_switch.pack(side=tk.LEFT)
        ttk.Button(snort_frame, text="View Logs", command=lambda: self.view_logs("Snort Logs")).pack(side=tk.LEFT)

        nmap_frame = ttk.Frame(tab)
        nmap_frame.pack(pady=10)
        ttk.Label(nmap_frame, text="Nmap", font=("Helvetica", 12, "bold")).pack(anchor=tk.W)
        nmap_switch = ttk.Checkbutton(nmap_frame, text="Enable Nmap", command=self.run_nmap)
        nmap_switch.pack(side=tk.LEFT)
        ttk.Button(nmap_frame, text="View Results", command=lambda: self.view_logs("Nmap Results")).pack(side=tk.LEFT)

        # Replaced the previous code for Wireshark with the new run_wireshark method
        wireshark_frame = ttk.Frame(tab)
        wireshark_frame.pack(pady=10)
        ttk.Label(wireshark_frame, text="Wireshark", font=("Helvetica", 12, "bold")).pack(anchor=tk.W)
        wireshark_switch = ttk.Checkbutton(wireshark_frame, text="Enable Wireshark", command=self.run_wireshark)
        wireshark_switch.pack(side=tk.LEFT)
        ttk.Button(wireshark_frame, text="View Capture", command=lambda: self.view_logs("Wireshark Capture")).pack(side=tk.LEFT)

        tcpdump_frame = ttk.Frame(tab)
        tcpdump_frame.pack(pady=10)
        ttk.Label(tcpdump_frame, text="Tcpdump", font=("Helvetica", 12, "bold")).pack(anchor=tk.W)
        tcpdump_switch = ttk.Checkbutton(tcpdump_frame, text="Enable Tcpdump", command=self.run_tcpdump)
        tcpdump_switch.pack(side=tk.LEFT)
        ttk.Button(tcpdump_frame, text="View Capture", command=lambda: self.view_logs("Tcpdump Capture")).pack(side=tk.LEFT)

    #def setupSettings(self):
def main():
    root = ThemedTk(theme="breeze", themebg=True)
    app = NextGenFirewallGUI(root)

if __name__ == "__main__":
    main()