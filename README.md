# NeonChat 💬

Foydalanuvchi bilan kundalik odatiy suhbatlar uchun AI kutubxona.

## Kalit so'zlar
`chat`, `conversation`, `message`, `send`, `history`, `persona`, `dialogue`, `response`, `hook`, `language`

## O'rnatish
```bash
pip install neonchat
```

## Ishlatish

```python
from NeonChat import NeonChat

chat = NeonChat(persona="assistant", language="uz")

# Xabar yuborish
response = chat.send("Salom!")
print(response["content"])

# Suhbat tarixini ko'rish
history = chat.history_get(limit=5)
for msg in history:
    print(f"[{msg['role']}]: {msg['content']}")

# Hook qo'shish
def on_reply(msg):
    print(f"Yangi javob: {msg['content']}")

chat.on_message(on_reply)
chat.send("Bugun qanday yordam bera olasiz?")
```

## Real misol

```python
from NeonChat import NeonChat

bot = NeonChat(persona="customer_support", language="uz")

print("Suhbat boshlandi. 'chiqish' deb yozing.")
while True:
    user_input = input("Siz: ")
    if user_input.lower() == "chiqish":
        break
    resp = bot.send(user_input)
    print(f"Bot: {resp['content']}")

print(f"Jami xabarlar: {len(bot.history)}")
```
