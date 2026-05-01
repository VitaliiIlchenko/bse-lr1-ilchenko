class SmartDocAI:
    def __init__(self):
        # Список дозволених форматів
        self.supported_formats = ['.pdf', '.jpg', '.png']
        self.max_size_mb = 20

    def validate_file(self, filename, size_mb):
        """
        Метод 1: Валідація файлу.
        Перевіряє формат та розмір.
        """
        if size_mb <= 0:
            # Обробка виняткових ситуацій
            raise ValueError("Розмір файлу не може бути нульовим або від'ємним")

        # Пошук розширення
        if '.' not in filename:
            return False, "Файл не має розширення"
        
        extension = filename[filename.rfind('.'):].lower()
        
        # Перевірка формату через цикл
        is_supported = False
        for fmt in self.supported_formats:
            if extension == fmt:
                is_supported = True
                break
        
        if not is_supported:
            return False, f"Формат {extension} не підтримується"

        # Перевірка граничного значення розміру
        if size_mb > self.max_size_mb:
            return False, "Файл занадто великий (макс. 20МБ)"

        return True, "Файл валідний"

    def calculate_processing_fee(self, size_mb, is_priority=False):
        """
        Метод 2: Розрахунок вартості обробки.
        Використовує умовні конструкції.
        """
        base_price = 5.0
        if size_mb > 10:
            base_price += 2.0  # Доплата за великий файл
        
        if is_priority:
            base_price *= 1.5  # Націнка за терміновість
            
        return round(base_price, 2)

    def get_document_type(self, filename):
        """
        Метод 3: Визначення типу документа за ключовими словами.
        """
        name = filename.lower()
        if "invoice" in name or "check" in name:
            return "Фінансовий документ"
        elif "contract" in name:
            return "Юридичний документ"
        else:
            return "Загальний документ"
