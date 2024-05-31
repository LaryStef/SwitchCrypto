from flask_mail import Message

from . import mail


def send_email_code(code: str, recipient: str) -> None:
    recipients = ["timurkotov1999@gmail.com"]   # just for tests

    print(code)
    print(recipient)    
    message = Message(f"Registration on CryptoDeal", recipients=recipients)
    message.html = f"""
        <h2>Secret code: {code}<h2>
        <p style="font-size: 14px; color: black">Don't reply to this email<p>
        <p style="font-size: 14px; color: black">Support on Support@cryptodeal.com<p>
    """
    mail.send(message)
