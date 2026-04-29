# helpers.py - полная версия
import time
import random

class Helpers:
    
    @staticmethod
    def generate_unique_email():
        """Генерирует уникальный email"""
        timestamp = int(time.time())
        return f"test_user_{timestamp}@example.com"
    
    @staticmethod
    def generate_random_email():
        """Генерирует email со случайным числом"""
        random_num = random.randint(100000, 999999)
        return f"user_{random_num}@test.com"