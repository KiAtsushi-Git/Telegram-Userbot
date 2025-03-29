# Telegram Userbot

Этот репозиторий содержит простой Telegram userbot, который использует библиотеку Pyrogram для взаимодействия с Telegram. Бот отвечает на команду `//ping`, предоставляя информацию о своем статусе.

## Требования

- Python 3.8+ (рекомендуется)
- Библиотеки:
  - pyrogram 2.0.106
  - tgcrypto (необязательно, но рекомендуется для лучшей производительности)
  - logging

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/KiAtsushi-Git/Telegram-Userbot
   cd Telegram-Userbot
   ```

2. Установите необходимые библиотеки:
   ```bash
   pip install -r requirements.txt
   ```

3. Получите свои [Telegram API данные](https://my.telegram.org/auth) — `API ID` и `API Hash`.

4. Настройте конфигурацию бота в файле `config.py`:
   - `phone_number`: Ваш номер телефона в международном формате (например, `+71234567890`).
   - `api_id`: Ваш API ID, который вы получили от Telegram.
   - `api_hash`: Ваш API hash, который вы получили от Telegram.
   - `admin_id`: Ваш Telegram user ID (только этот пользователь может использовать команду `//ping`).

Пример конфигурации:
```python
### Telegram API config
phone_number = "account phone number, like: +71234567890"
api_id = 123456789
api_hash = "api_hash"

### Userbot config
admin_id = 123456789
```

5. Запустите бота:
   ```bash
   python userbot.py
   ```

## Команды бота

### `//ping`
Бот ответит информацией о времени отклика и времени работы бота.

Пример ответа:
```
🚀Pong! 🏓
🤖 Юзер-Бот аккаунта: @username (ID: 123456)
⚡Скорость отклика Telegram: 42.76 мс
⏱ Время с момента запуска бота: 1д 2ч 15м 10с
```

Команду может использовать только администратор (пользователь, указанный в `config.py`). Остальные пользователи получат сообщение о том, что у них нет прав на выполнение команды.

## Логирование

Логи сохраняются в файле `userbot.log` и выводятся в консоль. Уровень логирования установлен на `INFO`, но его можно изменить в блоке `logging.basicConfig()` в файле `userbot.py`.

---
### Автор

| **Name** | Faraday |
|-------------------|---------|
| **Old**          | 15      |
| **Country** | Russian |
| **Nickname** | KiAtsushi |
| **Email** | [kiatsushi@ki.ru.net](mailto:kiatsushi@ki.ru.net) |
| **Telegram** | [@KiAtsushi](https://t.me/KiAtsushi) |
