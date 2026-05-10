# 🛡️ Windows Keyword-Based Site Blocker

A powerful, lightweight Python script that monitors your active windows in real-time. If it detects a specific forbidden keyword in a browser tab or window title, it instantly terminates all running web browser processes.

---

## ✨ Features

* **Real-Time Monitoring:** Scans window titles every 0.2 seconds to ensure no forbidden content is accessed.
* **Deep Detection:** Unlike simple URL blockers, this scans the **Window Title**, catching keywords even if they are embedded in search queries or page titles.
* **Stealth Mode:** Designed to run silently in the background.
* **Multi-Browser Support:** Automatically targets Chrome, Edge, Firefox, Opera, and Brave.
* **Low Resource Usage:** Optimized with `time.sleep` intervals to ensure it doesn't drain your CPU.

---

## 🚀 Installation

### 1. Requirements
This script is designed for **Windows** environments and requires **Python 3.x**.

### 2. Clone the Repository
git clone https://github.com/yourusername/site-blocker-python.git
cd site-blocker-python

---

## ⚙️ Configuration

Open the script and modify the `YASAKLI_KELIME` variable to set your desired forbidden keyword:

# --- SETTINGS ---
YASAKLI_KELIME = "your_forbidden_word"  # Change this to whatever you want to block

---

## 🛠️ Usage

You can run the script in two ways:

### Standard Mode (Console Visible)
python main.py

### Background Mode (Console Hidden)
pythonw main.py

---

## 📜 How it Works (Technical Details)

1. **Windows API Integration:** Uses `ctypes.windll.user32` to access the list of all visible windows.
2. **Title Analysis:** Iterates through every open window and checks if the forbidden string exists in its title (case-insensitive).
3. **Process Termination:** If a match is found, it triggers a `taskkill` command via `os.system` to force-close the browsers listed in the `TARAYICILAR` array.

---

## ⚠️ Disclaimer
This tool is for personal productivity and educational purposes. Use it at your own risk. The developer is not responsible for any unsaved data loss caused by the sudden termination of browser processes.

## 📄 License
This project is licensed under the MIT License.
