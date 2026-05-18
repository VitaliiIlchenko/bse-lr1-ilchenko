class SmartDocAI:
    # Константи класу 
    MAX_SIZE_MB = 20
    LARGE_FILE_THRESHOLD_MB = 10
    BASE_PRICE = 5.0
    LARGE_FILE_SURCHARGE = 2.0
    PRIORITY_MULTIPLIER = 1.5

    def __init__(self):
        # Використовуємо set для швидкого пошуку форматів
        self.supported_formats = {'.pdf', '.jpg', '.png'}  

    def _get_extension(self, filename):
        """Допоміжний приватний метод для виділення розширення (Extract Method)"""
        if '.' not in filename:
            return None
        return filename[filename.rfind('.'):].lower()

    def validate_file(self, filename, size_mb):
        """Валідація файлу (Рефакторинг: SRP, Extract Method)"""
        if size_mb <= 0:
            raise ValueError("Розмір файлу не може бути нульовим або від'ємним")

        extension = self._get_extension(filename)
        if not extension or extension not in self.supported_formats:
            return False, f"Формат {extension} не підтримується або відсутнє розширення"

        if size_mb > self.MAX_SIZE_MB:
            return False, f"Файл занадто великий (макс. {self.MAX_SIZE_MB}МБ)"

        return True, "Файл валідний"

    def calculate_processing_fee(self, size_mb, is_priority=False):
        """Розрахунок вартості (Рефакторинг: Simplify Conditional через Guard Clauses)"""
        price = self.BASE_PRICE
        if size_mb > self.LARGE_FILE_THRESHOLD_MB:
            price += self.LARGE_FILE_SURCHARGE
        
        if is_priority:
            price *= self.PRIORITY_MULTIPLIER
            
        return round(price, 2)

    def get_document_type(self, filename):
        """Визначення типу документа за ключовими словами"""
        name = filename.lower()
        if "invoice" in name or "check" in name:
            return "Фінансовий документ"
        if "contract" in name:
            return "Юридичний документ"
        return "Загальний документ"
