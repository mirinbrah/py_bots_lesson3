import asyncio
import logging
from config import TOKEN

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# базовые логи
logging.basicConfig(level=logging.INFO)

# Память бота
message_history = {}
MAX_HISTORY_SIZE = 20

# Создаем роутер
router = Router()


#Хэндлеры

@router.message(CommandStart())
async def cmd_start(message: Message):
    """Отправляет приветственное сообщение по команде /start."""
    await message.answer(
        "Привет! Я бот на aiogram, который запоминает последние сообщения.\n"
        "Добавьте меня в группу, и я смогу показать последние 3 сообщения по команде /last3"
    )


@router.message(Command("last3"))
async def cmd_last_three(message: Message):
    """Отправляет последние 3 сообщения по команде /last3."""
    chat_id = message.chat.id
    if chat_id not in message_history or not message_history[chat_id]:
        await message.answer("Я еще не видел сообщений в этом чате.")
        return

    last_messages = message_history[chat_id][:3]
    if not last_messages:
        await message.answer("История пока пуста.")
        return

    response_text = "Вот последние сообщения, которые я видел:\n"
    for i, msg in enumerate(last_messages, 1):
        response_text += f"{i}. «{msg}»\n"
    await message.answer(response_text)


@router.message()
async def store_any_message(message: Message):
    """Этот обработчик ловит ВСЕ сообщения, которые не являются командами."""
    if not message.text:
        return

    chat_id = message.chat.id
    message_text = message.text

    if chat_id not in message_history:
        message_history[chat_id] = []

    message_history[chat_id].insert(0, message_text)
    message_history[chat_id] = message_history[chat_id][:MAX_HISTORY_SIZE]
    logging.info(f"Сохранено сообщение в чате {chat_id}: '{message_text}'")


async def main():
    """Основная асинхронная функция для запуска бота."""
    print("Бот запускается...")

    # Создаем объект бота, передавая ему токен из файла config.py
    bot = Bot(token=TOKEN)

    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)
    print("Бот остановлен.")


if __name__ == "__main__":
    asyncio.run(main())