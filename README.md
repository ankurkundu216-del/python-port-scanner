# Python Port Scanners

A collection of lightweight network port scanners built in Python to demonstrate TCP connection handshakes, network protocols, and low-level packet crafting using Scapy.

---

## 🛠️ Features

### 1. TCP Connect Scanner (`socket_prog.py`)
- Uses Python's built-in `socket` library.
- Performs a complete 3-way TCP handshake (`SYN` → `SYN-ACK` → `ACK`).
- Standard user execution — **no root permissions required**.

### 2. TCP SYN Stealth Scanner (`syn_scanner.py`)
- Uses `Scapy` for custom Layer 3/4 packet crafting.
- Performs a half-open stealth scan (`SYN` → `SYN-ACK` → `RST`).
- Fast and accurate — **requires root/sudo permissions**.

---

## ⚙️ Prerequisites & Setup

Ensure you are running Linux (Ubuntu/Debian recommended) with Python 3.

```bash
# Update package list and install Scapy
sudo apt update && sudo apt install python3-scapy -y

---

## 🚀 How to Run

### Run the TCP Connect Scanner
```bash
python3 socket_prog.py

---

## Run the Stealth SYN Scanner
```bash
sudo python3 syn_scanner.py
