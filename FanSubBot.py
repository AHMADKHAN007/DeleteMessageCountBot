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


@bot.on_message(filters.chat(userid) & filters.text & filters.regex('/check'))
async def handle_check(client, message):
    limit = int(message.text.strip().split()[1])
    async for mes in bot.get_chat_history(chat_id=bot_user_id, limit=limit):
        if mes.text:
            counter.increment()
        else:
            counter_del.increment()
    await bot.send_message(chat_id=userid,
                           text=f'count_del: {counter_del.get_count()}\nhas_text: {counter.get_count()}')

bot.run()
