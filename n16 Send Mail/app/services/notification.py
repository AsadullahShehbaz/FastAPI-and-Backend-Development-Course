from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema
from fastapi_mail import FastMail,ConnectionConfig, MessageType
from pydantic import EmailStr
from app.config import notification_settings
from app.utils import TEMPLATE_DIR


class NotificationService:
    def __init__(self,tasks : BackgroundTasks):
        # Connect with server
        self.fastmail = FastMail(ConnectionConfig(
            **notification_settings.model_dump(),
            TEMPLATE_FOLDER=TEMPLATE_DIR
        ))
        self.tasks = tasks 
    async def send_mail(self,
                        recipient: list[EmailStr],
                        subject: str,
                        body: str):
        self.tasks.add_task(
            self.fastmail.send_message,
            message= MessageSchema(
            recipients=recipient,
            subject=subject,
            body=body,
            subtype=MessageType.plain 
            )
    )

    async def send_mail_with_template(self,
                            recipient: list[EmailStr],
                            subject: str,
                            context: dict,
                            template_name: str):
            self.tasks.add_task(
                self.fastmail.send_message,
                message= MessageSchema(
                    recipients=recipient,
                    subject=subject,
                    template_body=context,
                    subtype=MessageType.html
                ),
                template_name=template_name
        )
        
        

