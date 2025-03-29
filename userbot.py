"""Пример простого User-Bot для Telegram"""
import time
import logging
from pyrogram import Client, filters
from config import phone_number, api_id, api_hash, admin_id


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("userbot.log", mode="w")],
)
logger = logging.getLogger(__name__)

usb = Client("userbot", api_id=api_id, api_hash=api_hash, phone_number=phone_number)
start_time = time.time()


@usb.on_message(filters.command("ping", prefixes="//"))
async def ping(client, msg):
    """Ping function"""
    logger.info(
        "Получена команда //ping от пользователя %d (%s)",
        msg.from_user.id, msg.from_user.username
    )

    if await check_for_admin(msg.from_user.id):
        await msg.delete()

        bot_info = await client.get_me()
        bot_username = bot_info.username
        bot_id = bot_info.id

        sent_time = time.time()
        sent_message = await msg.reply_text("🚀Pong!🏓")
        received_time = time.time()
        ping_time = (received_time - sent_time) * 1000

        await sent_message.edit_text(
            f"🚀Pong! 🏓\n"
            f"🤖 Юзер-Бот аккаунта: @{bot_username} (ID: {bot_id})\n"
            f"⚡Скорость отклика Telegram: {ping_time:.2f} мс\n"
            f"⏱ Время с момента запуска бота: {await custom_format_time(time.time() - start_time)}"
        )

        logger.info(
            "Ответ на команду //ping отправлен пользователю %d", msg.from_user.id
        )
    else:
        await msg.delete()
        await msg.reply_text("У вас нет разрешения на выполнение команды //ping.")
        logger.warning(
            "%d (%s) пытался выполнить команду //ping.",
            msg.from_user.id, msg.from_user.username
        )


async def check_for_admin(chat_id):
    """Checking administrator rights"""
    return chat_id == admin_id


async def custom_format_time(seconds):
    """A block for managing the date and time format"""
    days = int(seconds // (24 * 3600))
    hours = int((seconds % (24 * 3600)) // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    formatted_time = f"{days}д {hours}ч {minutes}м {seconds}с"
    return formatted_time


if __name__ == "__main__":
    logger.info("Бот запущен.")
    usb.run()
    logger.info("Бот завершил свою работу.")
