"""
Определение стадий диалога
Соответствует стадиям из dialogue_patterns.json
"""
from enum import Enum


class DialogueStage(str, Enum):
    """Стадии диалога"""
    GREETING = "greeting"                      # Приветствие, начало диалога
    VIEW_MY_BOOKING = "view_my_booking"        # Просмотр своих записей