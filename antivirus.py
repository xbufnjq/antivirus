import os
import sys
import hashlib
import shutil
import datetime

# === Сигнатуры и вредоносные паттерны ===
MD5_SIGNATURES = {
    "e99a18c428cb38d5f260853678922e03": "Test Trojan",
    "44d88612fea8a8f36de82e1278abb02f": "EICAR Test File"
}

SUSPICIOUS_KEYWORDS = [
    "eval(",
    "exec(",
    "os.system(",
    "subprocess.",
    "socket.",
    "base64.b64decode(",
    "requests.get(",
    "urllib.request.urlopen(",
    "compile(",
]

QUARANTINE_FOLDER = "quarantine"
LOG_FILE = "scan_log.txt"

# === Утилиты ===

def calculate_md5(filepath):
    try:
        with open(filepath, "rb") as f:
            md5 = hashlib.md5()
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
            return md5.hexdigest()
    except Exception as e:
        return None

def log(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"[{datetime.datetime.now()}] {message}\n")

def quarantine(file_path):
    if not os.path.exists(QUARANTINE_FOLDER):
        os.makedirs(QUARANTINE_FOLDER)
    try:
        filename = os.path.basename(file_path)
        dest_path = os.path.join(QUARANTINE_FOLDER, filename)
        shutil.move(file_path, dest_path)
        log(f"Файл {file_path} перемещён в карантин.")
        return dest_path
    except Exception as e:
        log(f"Ошибка карантина: {e}")
        return None

# === Проверки ===

def scan_file(filepath):
    results = []

    # Проверка по MD5
    md5 = calculate_md5(filepath)
    if md5 in MD5_SIGNATURES:
        results.append(f"MD5-сигнатура: {MD5_SIGNATURES[md5]}")

    try:
        with open(filepath, "r", errors='ignore') as f:
            content = f.read()
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in content:
                    results.append(f"Подозрительная конструкция: {keyword}")
    except Exception:
        pass

    return results

def scan_directory(path):
    infected = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            threats = scan_file(full_path)
            if threats:
                infected[full_path] = threats
    return infected

# === Главная точка входа ===

def main():
    print("🛡️  Anti-Guardian: Python Antivirus")
    print("Автор: Harvard Startup Candidate\n")

    if len(sys.argv) != 2:
        print("Использование: python anti_guardian.py <директория>")
        return

    path = sys.argv[1]
    if not os.path.isdir(path):
        print("❌ Указанный путь не существует или не является директорией.")
        return

    log(f"Сканирование начато в: {path}")
    threats = scan_directory(path)

    if not threats:
        print("✅ Угроз не найдено.")
        log("Сканирование завершено: угроз не найдено.")
    else:
        print("\n⚠️ Обнаружены угрозы:")
        for file, detections in threats.items():
            print(f"\n[!] Файл: {file}")
            for item in detections:
                print(f"  - {item}")
            quarantined_path = quarantine(file)
            if quarantined_path:
                print(f"  → Перемещено в карантин: {quarantined_path}")
        log(f"Сканирование завершено: обнаружено {len(threats)} заражённых файлов.")

if __name__ == "__main__":
    main()
