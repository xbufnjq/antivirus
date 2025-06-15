# 🛡️ Anti-Guardian — Python Antivirus Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

> **Anti-Guardian** is a lightweight antivirus scanner built in Python. It detects and isolates trojans and malicious scripts using signature-based and behavior-based scanning. This project was created as part of a cybersecurity-focused startup portfolio for Harvard CS.

---

## 🚀 Features

- 🔍 Recursive directory scan
- ✅ Signature-based detection (MD5 + code patterns)
- 🧠 Behavior analysis of Python scripts
- 📂 Quarantine system to isolate threats
- 📝 Scan logging
- 🔒 Modular and extensible design

---

## 📦 Installation

> No dependencies required. Works out of the box.

```bash
git clone https://github.com/yourusername/anti-guardian.git
cd anti-guardian
python3 anti_guardian.py /path/to/scan
