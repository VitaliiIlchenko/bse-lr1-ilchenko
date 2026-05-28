import unittest
from main import SmartDocAI

class TestSmartDocAI(unittest.TestCase):
    def setUp(self):
        """Arrange: Ініціалізація об'єкта перед кожним тестом"""
        self.ai = SmartDocAI()

    def test_case_1_valid_pdf(self):
        """Позитивний тест: Валідний PDF (EP)"""
        # Act
        result, msg = self.ai.validate_file("invoice.pdf", 10)
        # Assert
        self.assertTrue(result)
        self.assertEqual(msg, "Файл валідний")

    def test_case_2_valid_png(self):
        """Позитивний тест: Підтримувана картинка (EP)"""
        # Act
        result, _ = self.ai.validate_file("image.png", 5)
        # Assert
        self.assertTrue(result)

    def test_case_3_invalid_format(self):
        """Негативний тест: Формат .exe (EP)"""
        # Act
        result, msg = self.ai.validate_file("virus.exe", 1)
        # Assert
        self.assertFalse(result)
        self.assertIn("не підтримується", msg)

    def test_case_4_no_extension(self):
        """Негативний тест: Файл без розширення (EP)"""
        # Act
        result, msg = self.ai.validate_file("data_file", 2)
        # Assert
        self.assertFalse(result)
        self.assertIn("відсутнє розширення", msg)

    def test_case_5_boundary_max(self):
        """BVA: Точно 20МБ (Граничне значення)"""
        # Act
        result, _ = self.ai.validate_file("doc.pdf", 20)
        # Assert
        self.assertTrue(result)

    def test_case_6_boundary_over(self):
        """BVA: 20.1МБ (За межею)"""
        # Act
        result, msg = self.ai.validate_file("big.pdf", 20.1)
        # Assert
        self.assertFalse(result)
        self.assertEqual(msg, "Файл занадто великий (макс. 20МБ)")

    def test_case_7_boundary_min(self):
        """BVA: Мінімально валідне значення 0.1МБ"""
        # Act
        result, _ = self.ai.validate_file("small.pdf", 0.1)
        # Assert
        self.assertTrue(result)

    def test_case_8_zero_size(self):
        """Обробка винятків: Нульовий розмір (BVA)"""
        # Assert
        with self.assertRaises(ValueError):
            # Act
            self.ai.validate_file("empty.pdf", 0)

    def test_case_9_legal_type(self):
        """Логічна перевірка: Визначення типу документа"""
        # Act
        doc_type = self.ai.get_document_type("legal_contract_v2.pdf")
        # Assert
        self.assertEqual(doc_type, "Юридичний документ")

    def test_case_10_priority_price(self):
        """Логічна перевірка: Розрахунок ціни з пріоритетом"""
        # (база 5.0 + 2.0 за розмір > 10) * 1.5 націнка = 10.5
        # Act
        price = self.ai.calculate_processing_fee(15, is_priority=True)
        # Assert
        self.assertEqual(price, 10.5)

if __name__ == '__main__':
    unittest.main()
