from BotConfig import bot, userid, bot_user_id
from pyrogram import filters



class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count

class Counter_del:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count


# ایجاد یک نمونه از کلاس Counter
counter = Counter()
counter_del = Counter_del()



@bot.on_message(filters.chat(userid) & filters.text & filters.regex('/del'))
async def handle_check(client, message):
    limit = int(message.text.strip().split()[1])
    with open('del.txt', 'w', encoding='utf-8') as file:
        async for mes in bot.get_chat_history(chat_id=bot_user_id, limit=limit):
            file.write(f'id: {mes.id}\nDate: {mes.date}\n---------------\n')
    await bot.send_document(chat_id=userid, document='del.txt')

bot.run()
