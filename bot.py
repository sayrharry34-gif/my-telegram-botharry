import asyncio
import random
import logging
from telethon import TelegramClient
import config  # သင်ဆောက်ထားတဲ့ config.py ဖိုင်ကို ခေါ်သုံးခြင်း

# Logging စနစ်ကို စတင်ခြင်း
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Spam စာသားများ (အပြည့်အစုံ)
MESSAGES_LIST = [
    "/spawn", "ကတ်ကျပါတော့ 🃏", "Rare လေးတွေ လိုချင်တယ်ဗျာ ✨", "ဒီတစ်ခါ ဘာထွက်မလဲ စိတ်လှုပ်ရှားလိုက်တာ 🤩",
    "ကတ်လေးရေ.. ကျေးဇူးပြုပြီး ကျပေးပါ 🙏", "စောင့်ရတာ အရမ်းပင်ပန်းပြီ.. ကတ်လေးရေ 😅",
    "Rare ကတ်လေးတွေ လိုချင်လွန်းလို့ပါ 💖", "ကတ်လေးရေ.. ထွက်စမ်းပါဦး 💫",
    "အကောင့်ထဲကို ကတ်လေးတွေ ရောက်လာပါစေ 🍀", "ဒီနေ့တော့ ကံကောင်းပါစေဗျာ 🤞",
    "ကတ်စုနေတာကြာပြီ.. Rare လေး လိုတယ် 🧿", "ဒီတစ်ခါတော့ အလန်းကြီး ထွက်ပါစေ 🌟",
    "ကတ်ကောင်းမှ ကတ်ကောင်း ✅", "Rare လေး ပိုင်ဆိုင်ဖို့ အသင့်ပဲ 💎",
    "နောက်ထပ် တစ်ကတ်လောက်တော့ ထပ်ကျပေးပါ 🆙", "ကတ်စက်လေးက စိတ်ဆိုးနေတာလား 🤔"
]

async def send_spam(acc):
    try:
        # Client ကို session file နာမည်ဖြင့် စတင်ခြင်း
        client = TelegramClient(acc['name'], acc['id'], acc['hash'])
        await client.start()
        logger.info(f"✅ {acc['name']} Login အောင်မြင်သည်")
        
        while True:
            try:
                # config.py ထဲက SPAM_TARGET_CHAT ကို ခေါ်သုံးခြင်း
                msg = random.choice(MESSAGES_LIST)
                await client.send_message(config.SPAM_TARGET_CHAT, msg)
                logger.info(f"📤 {acc['name']} ပို့ပြီးပြီ: {msg}")
                await asyncio.sleep(random.uniform(15, 30)) # 15-30 စက္ကန့် စောင့်ခြင်း
            except Exception as e:
                logger.error(f"❌ {acc['name']} Error: {e}")
                await asyncio.sleep(60)
    except Exception as e:
        logger.error(f"❌ {acc['name']} စတင်၍မရပါ: {e}")

async def main():
    # အကောင့် ၇ ခုလုံးကို တစ်ပြိုင်နက် Run ပေးခြင်း
    await asyncio.gather(*[send_spam(acc) for acc in config.ACCOUNTS])

if __name__ == '__main__':
    asyncio.run(main())
