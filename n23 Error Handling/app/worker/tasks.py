from asgiref.sync import async_to_sync
from celery import Celery
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import EmailStr
from app.config import db_settings,notification_settings
from app.utils import TEMPLATE_DIR

fastmail = FastMail(ConnectionConfig(
            **notification_settings.model_dump(),
            TEMPLATE_FOLDER=TEMPLATE_DIR
        ))

# Create celery app
app = Celery("api-tasks",broker=db_settings.REDIS_URL(9),backend=db_settings.REDIS_URL(8))
send_message = async_to_sync(fastmail.send_message)

# Register task 
@app.task(name="send email")
def send_mail(recipient: list[EmailStr],subject: str,body: str):
    send_message(
            message= MessageSchema(
            recipients=recipient,
            subject=subject,
            body=body,
            subtype=MessageType.plain 
            )
    )
    return "Email Sent!"


@app.task(name="send email with template")
def send_mail_with_template(
                            recipient: list[EmailStr],
                            subject: str,
                            context: dict,
                            template_name: str):
           
                send_message(
                message= MessageSchema(
                    recipients=recipient,
                    subject=subject,
                    template_body=context,
                    subtype=MessageType.html
                ),
                template_name=template_name
        )

import time

@app.task
def background_task(name: str, data: dict):
    time.sleep(5)       # gives us time to watch it run
    return name


if __name__ == "__main__":
        result = send_mail.delay(recipient=["asadullahcreative@gmail.com"],subject="Celery Task",body="None")
        print(result.get())
        print(result.status)