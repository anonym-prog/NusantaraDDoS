# NusantaraDDoS - HTTP Flood Multithread

Tool DDoS sederhana untuk pengujian beban server. Berjalan di Termux tanpa root.

## Instalasi
```bash
git clone https://github.com/username/NusantaraDDoS.git
cd NusantaraDDoS
bash install.sh


### **2. install.sh**
```bash
#!/bin/bash
pkg update -y && pkg upgrade -y
pkg install python -y
pip install requests colorama
echo "[+] Instalasi selesai. Jalankan: python ddos.py <URL> <threads> <durasi>"
