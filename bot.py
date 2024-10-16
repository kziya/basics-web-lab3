from queue import Queue

from telegram.constants import ChatAction

from chatgpt import generate_chatgpt_response
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN


async def chatgpt_command_reply(update, context):
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    text = update.message.text
    reply = generate_chatgpt_response(text)
    await update.message.reply_text(reply)

async def command_handler(update, context):
    command = update.message.text.lstrip('/')
    responses = {
        "student": "Ziya Karimli IM-11",
        "it": "Backend",
        "contacts": "email: kziya04@icloud.com",
        "chatgpt": "Type any message and I'll respond using ChatGPT."
    }
    response = responses.get(command, "Unknown command. Type /help for a list of available commands.")
    await update.message.reply_text(response)

if __name__ == "__main__":
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler(["student", "it", "contacts","chatgpt"], command_handler))


    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), chatgpt_command_reply)
    application.add_handler(echo_handler)


    print("Starting app")
    application.run_polling()





