import qrcode
from io import BytesIO
from aiogram.types import InputFile

async def generate_qr(link: str) -> InputFile:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)
    return InputFile(img_buffer)

def register_handlers_qr(dp: Dispatcher):
    dp.register_message_handler(generate_qr)