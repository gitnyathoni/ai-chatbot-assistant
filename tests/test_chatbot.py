import pytest
from src.chatbot import Chatbot
def test_history_tracking():
    bot = Chatbot.__new__(Chatbot)
    bot.history = []
    bot.model = "gpt-4"
    assert bot.history == []
