import sys
import os # เพิ่ม os เข้ามาเพื่ออ่านค่า Secrets
from linebot import LineBotApi
from linebot.models import TextMessage
from linebot.exceptions import LineBotApiError

try:
    # 1. อ่านค่าจาก "ตู้เซฟ" (GitHub Secrets)
    YOUR_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_ACCESS_TOKEN')
    YOUR_USER_ID = os.environ.get('LINE_USER_ID')

    # 2. อ่าน "ประเภทข้อความ" จากคำสั่ง (ที่เราจะสั่งใน .yml)
    # sys.argv[0] คือชื่อไฟล์, sys.argv[1] คือค่าแรกที่ส่งมา
    message_type = sys.argv[1] 

    if not YOUR_CHANNEL_ACCESS_TOKEN or not YOUR_USER_ID:
        print("Error: LINE_ACCESS_TOKEN or LINE_USER_ID not set.")
        sys.exit(1) # ออกจากโปรแกรมทันทีถ้าไม่มีกุญแจ

    line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)

    # 3. เลือกข้อความที่จะส่ง
    if message_type == "clock_in":
        message_text = "⏰ ได้เวลาเข้างาน! (08:55 น.)\nอย่าลืม Clock-In นะครับ"
        print("Sending Clock-In message...")
    elif message_type == "clock_out":
        message_text = "🌙 ได้เวลาเลิกงาน! (18:00 น.)\nอย่าลืม Clock-Out ครับ"
        print("Sending Clock-Out message...")
    else:
        message_text = "Test message from GitHub Actions."
        print("Sending test message...")

    # 4. ส่งข้อความ
    line_bot_api.push_message(YOUR_USER_ID, TextMessage(text=message_text))
    print("Message sent successfully!")

except LineBotApiError as e:
    print(f"Error sending message: {e}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)