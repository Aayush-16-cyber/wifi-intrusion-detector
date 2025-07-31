# 🔐 Wi-Fi Intrusion Detector

A smart Python tool that detects intruders on your Wi-Fi network by scanning connected devices, alerting via sound, logging unknown MAC addresses, and allowing real-time authorization — all from your terminal!

---

## 🚀 Features

- 🔎 Real-time network scanning (using ARP packets)
- ✅ Automatically identifies authorized devices
- ⚠️ Alerts when unknown devices (intruders) are detected
- 🔊 Plays sound notification for intruders
- 📝 Logs intruder MAC & IP addresses with timestamp
- 🧠 Interactive approval system to authorize new MACs

---

## 🖥 Requirements

- Python 3.10+
- Windows OS (due to `winsound` module)
- Required Python library:
  ```bash
  pip install scapy


## 📁 Project Structure

wifi-intrusion-detector/
- detector.py # Main script
- authorized_macs.txt # List of trusted MAC addresses
- intruder_log.txt # Auto-generated log for unknown MACs
- README.md # Project documentation
- LICENSE # MIT License file


---

## ⚙️ How to Use

1. ✅ Add your own device MAC(s) to `authorized_macs.txt` (one per line)
2. 🔌 Connect to your Wi-Fi
3. ▶️ Run the script:
   ```bash
   python detector.py
4. 🧠 If an unknown MAC is detected, you'll be asked:
   ```bash
   Press 'A' to authorize this MAC, or Enter to skip
