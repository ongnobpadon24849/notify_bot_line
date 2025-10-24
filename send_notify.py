import sys
import os
from linebot import LineBotApi
from linebot.models import TextMessage
from linebot.exceptions import LineBotApiError
from datetime import datetime
from zoneinfo import ZoneInfo # ใช้สำหรับจัดการ Timezone (UTC+7)

CLOCK_IN_TIME = "08:50"
CLOCK_OUT_TIME = "18:00"

DAYS_TH = [
    "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", 
    "วันศุกร์", "วันเสาร์", "วันอาทิตย์"
]
MONTHS_TH_ABBR = [
    "", "ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", 
    "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."
]

try:
    YOUR_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_ACCESS_TOKEN')
    YOUR_USER_ID = os.environ.get('LINE_USER_ID')

    message_type = sys.argv[1] 

    if not YOUR_CHANNEL_ACCESS_TOKEN or not YOUR_USER_ID:
        print("Error: LINE_ACCESS_TOKEN or LINE_USER_ID not set.")
        sys.exit(1)

    tz_bangkok = ZoneInfo("Asia/Bangkok")
    now = datetime.now(tz=tz_bangkok)
    
    day_of_week = DAYS_TH[now.weekday()]
    year_be = str(now.year + 543)[2:]
    current_date_thai = f"{now.day} {MONTHS_TH_ABBR[now.month]} {year_be}"

    line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)

    if message_type == "clock_in":
        message_text = f"""☀️ สวัสดีเช้า{day_of_week}!
วันนี้ ({current_date_thai})

อย่าลืม Clock-In ({CLOCK_IN_TIME} น.) นะครับ

ลุยงานกันเลย! 🚀"""
        print("Sending Clock-In message...")

    elif message_type == "clock_out":
        message_text = f"""🌙 {day_of_week} สิ้นสุด!
 
 วันนี้ ({current_date_thai})
 ทำงานได้เยี่ยมมากครับ

 อย่าลืม Clock-Out ({CLOCK_OUT_TIME} น.) นะครับ

 พักผ่อนครับ! 😴"""
        print("Sending Clock-Out message...")
        
    else:
        message_text = "Test message from scheduled job."
        print("Sending test message...")

    line_bot_api.push_message(YOUR_USER_ID, TextMessage(text=message_text))
    print("Message sent successfully!")

except LineBotApiError as e:
    print(f"Error sending message: {e}")
    sys.exit(1)
except IndexError:
    print("Error: No message_type provided (e.g., 'clock_in' or 'clock_out').")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)