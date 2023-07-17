import os
import qrcode

url = input("input some Message_text or URL: ")
code = qrcode.make(url)
code.save("Url-message-Qrcode.png")

os.startfile(os.path.join(os.getcwd(), "Url-message-Qrcode.png"))