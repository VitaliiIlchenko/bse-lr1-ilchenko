import time
import random

class SmartDocAI:
    """
    Система для автоматичного розпізнавання та обробки документів.
    Згенеровано для Лабораторної роботи №1 (проєкт SmartDoc AI).
    """
    def __init__(self):
        # Вимоги з нашого SRS
        self.supported_formats = ['.pdf', '.jpg', '.png']
        self.max_size_mb = 20

    def validate_and_upload(self, filename, size_mb):
        """Метод для завантаження та валідації файлу (User Story #2)"""
        print(f"\n[*] Спроба завантаження: {filename}...")
        time.sleep(0.7)
        
        # Перевірка формату
        ext = filename[filename.rfind('.'):].lower()
        if ext not in self.supported_formats:
            print(f"[!] ПОМИЛКА: Формат {ext} не підтримується системою.")
            return False
            
        # Перевірка розміру (Обмеження з SRS)
        if size_mb > self.max_size_mb:
            print(f"[!] ПОМИЛКА: Файл занадто великий ({size_mb}MB). Ліміт: {self.max_size_mb}MB.")
            return False
            
        print(f"[+] Файл успішно завантажено. Розмір: {size_mb} MB.")
        return True

    def process_with_ai(self):
        """Емуляція роботи AI-моделі (User Story #3)"""
        print("[*] Запуск AI-двигуна для розпізнавання тексту...")
        time.sleep(2.0)  # Імітація обчислень
        
        # Генерація "розпізнаних" даних
        extracted_data = {
            "Тип документа": "Invoice (Рахунок-фактура)",
            "ID документа": f"ID-{random.randint(1000, 9999)}",
            "Дата": "04.04.2026",
            "Сума до сплати": f"{random.randint(500, 25000)}.00 UAH",
            "Точність ШІ": f"{random.uniform(94.5, 99.9):.2f}%"
        }
        
        print("[+] Дані успішно витягнуто та структуровано:")
        for key, value in extracted_data.items():
            print(f"    > {key}: {value}")
        return extracted_data

def run_simulation():
    """Головний сценарій роботи програми"""
    print("="*40)
    print("   SMARTDOC AI: СИСТЕМА РОЗПІЗНАВАННЯ   ")
    print("="*40)
    
    app = SmartDocAI()
    
    # Сценарій 1: Успішна обробка (відповідає Acceptance Criteria в Jira)
    if app.validate_and_upload("invoice_scan_04.pdf", 4.2):
        app.process_with_ai()
    
    # Сценарій 2: Помилка формату
    app.validate_and_upload("vacation_photo.exe", 1.5)
    
    print("\n" + "="*40)
    print("       РОБОТУ ПРОГРАМИ ЗАВЕРШЕНО       ")
    print("="*40)

if __name__ == "__main__":
    run_simulation()