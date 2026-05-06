import time
from typing import List, Dict, Optional, Callable


class NeonChat:
    """Human-like conversation engine."""

    def __init__(self, persona: str = "assistant", language: str = "uz"):
        self.persona = persona
        self.language = language
        self.history: List[Dict] = []
        self._hooks: List[Callable] = []

    def send(self, message: str, role: str = "user") -> Dict:
        """Send a message and get response."""
        msg = {"role": role, "content": message, "timestamp": time.time()}
        self.history.append(msg)
        response = self._generate_response(message)
        resp_msg = {"role": "assistant", "content": response, "timestamp": time.time()}
        self.history.append(resp_msg)
        for hook in self._hooks:
            hook(resp_msg)
        return resp_msg

    def _generate_response(self, message: str) -> str:
        greetings = ["salom", "assalomu", "hello", "hi", "привет"]
        if any(g in message.lower() for g in greetings):
            return "Salom! Sizga qanday yordam bera olaman?"
        if "?" in message:
            return f"Savolingiz qabul qilindi. Javob izlamoqda..."
        return f"Tushundim: '{message[:40]}'. Davom etamiz."

    def history_get(self, limit: int = 10) -> List[Dict]:
        return self.history[-limit:]

    def clear(self):
        self.history = []

    def on_message(self, hook: Callable):
        """Register message hook."""
        self._hooks.append(hook)

    def export(self) -> Dict:
        return {"persona": self.persona, "language": self.language, "messages": len(self.history), "history": self.history}
