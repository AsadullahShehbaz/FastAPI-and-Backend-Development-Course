import asyncio

from fastapi_mail import FastMail,ConnectionConfig,MessageSchema, MessageType
from app.config import notification_settings

# Connect with server
fastmail = FastMail(ConnectionConfig(
    **notification_settings.model_dump()
))

# Send mail 

async def send_mail():
    await fastmail.send_message(
        message= MessageSchema(
            recipients=["asadullahcreative@gmail.com"],
            subject="Asadullah AI Products",
            body="Your Product has been submitted",
            subtype=MessageType.plain 
        )
    )
    print("Email sent!")

asyncio.run(send_mail())