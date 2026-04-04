import time
import random

class SmartDocAI:
    def __init__(self):
        self.supported_formats = ['.pdf', '.jpg', '.png']
        self.is_ready = True

    def upload_document(self, filename, file_size_mb):
        print(f"[*] Завантаження файлу: {filename} ({file_size_mb} MB)...")
        
        if file_size_mb > 20:
            print("[!] Помилка: Розмір файлу перевищує ліміт у 20 МБ.")
            return False
            
        ext = filename[filename.rfind('.'):].lower()
        if ext not in self.supported_formats:
            print(f"[!] Помилка: Формат {ext} не підтримується.")
            return False
            
        print("[+] Файл успішно завантажено. Передача до AI-моделі...\n")
        return True

    def extract_data(self):
        print("[*] AI аналізує документ...")
        time.sleep(1.5) # Симуляція часу обробки
        
        # Симуляція витягнутих даних
        extracted_data = {
            "Компанія": "ТОВ 'Роги та Копита'",
            "Дата": "04.04.2026",
            "Загальна сума": f"{random.randint(1000, 50000)}.00 грн",
            "Статус": "Успішно розпізнано"
        }
        
        print("[+] Дані успішно витягнуто:")
        for key, value in extracted_data.items():
            print(f"    - {key}: {value}")
        return extracted_data

def start_project():
    print("=== Вітаємо у системі SmartDoc AI ===\n")
    ai_system = SmartDocAI()
    
    # Тестовий сценарій (User Story 2 та 3 з нашого беклогу)
    test_file = "invoice_april.pdf"
    file_size = 5.2
    
    if ai_system.upload_document(test_file, file_size):
        ai_system.extract_data()
        
    print("\n=== Роботу програми завершено ===")

if __name__ == "__main__":
    start_project()